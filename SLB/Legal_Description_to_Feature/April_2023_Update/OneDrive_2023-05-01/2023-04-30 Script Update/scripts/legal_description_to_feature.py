'''
Module to support toolbox
'''
import os
import csv
import numpy as np
import pandas as pd
import string
from typing import List, Union

import arcpy

import config as cfg
import ld_parser

#<<<<<<<<<<<<<<<     >>>>>>>>>>>>>>>
def get_clean_name(dirty_name:str) -> str:
    '''
    Clean out spaces and punctuation from a string,
    returning a cleaned up name that can be used
    in titles, etc.
    '''
    if len(dirty_name) > 0:
        # Retain any underscores
        clean_name = dirty_name.replace('_', ' ')

        clean_name = clean_name.translate(str.maketrans('', '', string.punctuation))
        # Backfill spaces
        clean_name = clean_name.replace(' ', '_')
        # Clear out double underscores
        clean_name = clean_name.replace('__', '_')
    else:
        raise ValueError('Cannot accept blank names for cleanup')

    return clean_name


def get_excel_data(excel_file:str) -> pd.DataFrame:
    '''
    Get the lease data from the Excel file
    '''
    if os.path.exists(excel_file):
        excel_data = pd.read_excel(excel_file)
    else:
        raise FileNotFoundError('Unable to find lease data Excel file')

    excel_data = excel_data.replace({np.nan:None})

    return excel_data


def get_table_field_objects(tbl_name:str) -> List[arcpy.Field]:
    '''
    Provides a list of field objects for the table, less geometry/gdb
    related fields. Table name needs to be either full path or
    name within context of the workspace.
    '''
    field_list = arcpy.ListFields(tbl_name)
    field_list = [field_obj for field_obj in field_list if field_obj.type not in ['Geometry','GlobalID', 'OID', 'Guid']]
    field_list = [field_obj for field_obj in field_list if field_obj.name.lower() not in ['shape_length','shape_area', 'shape']]

    return field_list


def create_temp_table(gdb:str, tbl_name:str, template:str) -> None:
    '''
    Create the temp table based on the template schema
    '''
    tbl_path = os.path.join(gdb, tbl_name)

    if arcpy.Exists(tbl_path):
        arcpy.Delete_management(tbl_path)

    arcpy.CreateTable_management(gdb, tbl_name)

    field_list = get_table_field_objects(template)

    for field_obj in field_list:
        if field_obj.type == 'String':
            arcpy.AddField_management(
                tbl_path,
                field_name=field_obj.name,
                field_type=field_obj.type,
                field_alias= field_obj.aliasName,
                field_length=field_obj.length
            )
        elif field_obj.type in ['Single', 'Double']:
            arcpy.AddField_management(
                tbl_path,
                field_name=field_obj.name,
                field_type=field_obj.type,
                field_alias= field_obj.aliasName,
                field_scale=field_obj.scale
            )
        elif field_obj.type in ['SmallInteger', 'Integer', 'Date']:
            arcpy.AddField_management(
                tbl_path,
                field_name=field_obj.name,
                field_type=field_obj.type,
                field_alias= field_obj.aliasName
            )


def add_fields(layers:List[str]) -> None:
    '''
    Add PLSS fields
    '''
    for layer in layers:

        arcpy.AddField_management(
            layer,
            field_name="FRSTDIVID",
            field_type="TEXT",
            field_length=22,
            field_alias= "First Division Identifier")

        arcpy.AddField_management(
            layer,
            field_name="SECDIVNO",
            field_type="TEXT",
            field_length=50,
            field_alias= "Second Division Number")

        arcpy.AddField_management(
            layer,
            field_name="ERRORS",
            field_type="TEXT",
            field_length=2500,
            field_alias= "Error Messages")


def load_lease_table(lease_data_df:pd.DataFrame, lease_table:str) -> None:
    '''
    '''
    row_count = lease_data_df.shape[0]

    tbl_fields = get_table_field_objects(lease_table)
    field_lookup = {field.name:field.aliasName for field in tbl_fields}
    field_names = [field.name for field in tbl_fields]

    arcpy.AddMessage('Starting insert to lease table')
    with arcpy.da.InsertCursor(lease_table, field_names) as insert_cur:
        count = 0
        err_count = 0
        for _, lease_data in lease_data_df.iterrows():
            insert_row = []
            for field in field_names:
                field_alias = field_lookup[field]
                insert_row.append(lease_data[field_alias])

            try:
                insert_cur.insertRow(insert_row)
            except arcpy.ExecuteError as ex_err:
                arcpy.AddError(f'Unable to insert row: {ex_err}')
                arcpy.AddMessage(f'Error row: {insert_row}')
                err_count += 1
            else:
                count += 1
                if count % 5000 == 0:
                    arcpy.AddMessage(f'\t{count} of {row_count} records inserted')

        arcpy.AddMessage(f'{count} total records inserted from Excel to lease table')
        if err_count:
            arcpy.AddMessage(f'{err_count} records rejected')


def update_lease_table(lease_tbl:str, field_lookup:dict) -> int:
    '''
    Update the least table with the First Div ID if data is sound.
    Else update the error message column.
    '''
    err_count = 0

    cursor_fields = [
        field_lookup['Meridian'],            #0
        field_lookup['Township'],            #1
        field_lookup['Range'],               #2
        field_lookup['Section#'],            #3
        field_lookup['Legal Description'],   #4
        field_lookup['First Division Identifier'],   #5
        field_lookup['Error Messages']       #6
        ]

    with arcpy.da.UpdateCursor(lease_tbl, cursor_fields) as cursor:
        for row in cursor:
            error_msg = ''
            try:
                meridian_num = get_meridian(row[0])
            except ValueError as err:
                # arcpy.AddError(f'Invalid data in meridian value {row[0]}')
                error_msg = error_msg + '; ' + str(err)

            try:
                township_num = get_township(row[1])
            except ValueError as err:
                # arcpy.AddError(f'Invalid data in township value {row[1]}')
                error_msg = error_msg + '; ' + str(err)

            try:
                range_num = get_range(row[2])
            except ValueError as err:
                # arcpy.AddError(f'Invalid data in range value {row[2]}')
                error_msg = error_msg + '; ' + str(err)

            try:
                section_num = get_section(row[3])
            except ValueError as err:
                # arcpy.AddError(f'Invalid data in section value {row[3]}')
                error_msg = error_msg + '; ' + str(err)

            if len(error_msg) > 0:
                error_msg = error_msg[2:] # remove leading '; '
                row[6] = error_msg
                err_count += 1
            else:
                first_div_id = 'CO' + meridian_num + township_num + range_num + '0SN' + section_num + '0'
                row[5] = first_div_id

            cursor.updateRow(row)

    return err_count


def get_filtered_lease_table(lease_tbl:str) -> str:
    '''
    Get the lease table records that have First Div info and create
    temp table with that subset
    '''
    temp_table = 'filtered_lease_table'

    arcpy.MakeTableView_management(
        lease_tbl,
        temp_table,
        where_clause='FRSTDIVID IS NOT NULL',
        workspace=cfg.OUTPUT_GDB
    )

    temp_table = os.path.join(cfg.OUTPUT_GDB, temp_table)

    return temp_table


def _build_lease_tbl_mirror(lease_tbl:str, field_lookup:dict) -> List[list]:
    '''
    For performance reasons, building a dictionary from the lease table.
    To be used in the parsing and insert functions for the feature
    layer.
    '''
    search_fields = list(field_lookup.values())

    tbl_mirror = []

    search_query = "FRSTDIVID IS NOT NULL" # Only copy over records that did not error out
    with arcpy.da.SearchCursor(lease_tbl, search_fields, search_query) as tbl_cursor:
        for tbl_row in tbl_cursor:
            tbl_mirror.append(list(tbl_row))

    del tbl_cursor

    return tbl_mirror


def get_plss_features(lease_fc:str, lease_tbl:List[list], field_lookup:dict) -> dict:
    '''
    Update the feature layer with valid lease table entries. Reject and note any
    subsequent entries that may fail the 2nd division id check.
    '''
    search_fields = list(field_lookup.values())
    first_div_idx = search_fields.index(field_lookup['First Division Identifier'])
    legal_desc_idx = search_fields.index(field_lookup['Legal Description'])
    internal_id_id = search_fields.index(field_lookup['Internal ID'])

    plss_fields = ['SHAPE@', 'SECDIVNO']
    insert_fields = search_fields[:]
    insert_fields.extend(plss_fields)

    error_records = []

    count = 0
    with arcpy.da.InsertCursor(lease_fc, insert_fields) as insert_cur:

        # search_query = "FRSTDIVID IS NOT NULL" # Only copy over records that did not error out
        # with arcpy.da.SearchCursor(lease_tbl, search_fields, search_query) as tbl_cursor:
            # for tbl_row in tbl_cursor:
        for tbl_row in lease_tbl:
            count += 1

            if count % 1000 == 0:
                arcpy.AddMessage(f'\t{count} records searched from temp lease table')

            insert_row = list(tbl_row)
            first_div_value = tbl_row[first_div_idx]

            try:
                second_div_list_results = ld_parser.get_2nd_div(tbl_row[legal_desc_idx])
            except ValueError:
                arcpy.AddError(f'Unable to parse legal description: "{tbl_row[legal_desc_idx]}"')
                arcpy.AddMessage('\tSkipping row:')
                arcpy.AddMessage(f'\t {str(tbl_row)}')
                error_records.append(list(tbl_row))
                continue # skip rest of processing for this row; do not include in feature class

            if len(second_div_list_results['fractionals']) > 0:
                arcpy.AddMessage(f"REVIEW: The following fractionals need to be reviewed: {second_div_list_results['fractionals']}")
                arcpy.AddMessage(f'Record: {str(tbl_row)}')

            insert_count = 0

            if second_div_list_results['lookups'][0] == 'ALL':
                plss_query = f"FRSTDIVID = '{first_div_value}'"
                with arcpy.da.SearchCursor(cfg.PLSS, plss_fields, plss_query) as plss_cursor:
                    for plss_row in plss_cursor:
                        new_row = insert_row[:]
                        new_row.extend(list(plss_row))

                        insert_cur.insertRow(new_row)
                        insert_count += 1

            elif len(second_div_list_results['lookups']) == 0:
                arcpy.AddError(f'Unable to parse 2nd division items from legal description: "{tbl_row[legal_desc_idx]}"')
                arcpy.AddMessage('\tSkipping row:')
                arcpy.AddMessage(f'\t {str(tbl_row)}')
                error_records.append(list(tbl_row))
                continue # skip rest of processing for this row; do not include in feature class


            else:
                for second_div_value in second_div_list_results['lookups']:
                    plss_query = f"FRSTDIVID = '{first_div_value}' AND SECDIVNO = '{second_div_value}' "
                    with arcpy.da.SearchCursor(cfg.PLSS, plss_fields, plss_query) as plss_cursor:
                        for plss_row in plss_cursor:
                            new_row = insert_row[:]
                            new_row.extend(list(plss_row))

                            insert_cur.insertRow(new_row)
                            insert_count += 1

            if insert_count == 0:
                arcpy.AddError(f"No PLSS records found for query: {plss_query}, 2nd Div: {second_div_list_results['lookups']}")
                error_records.append(insert_row)

    results = {
        'error_count': len(error_records),
        'error_records': error_records
    }

    return results


def insert_and_merge_data(lease_layer:str, lease_table:str, dissolve_layer:str) -> None:
    '''
    Merges the data from the lease table with the polygons in the dissolve layer
    '''
    search_field_objs = get_table_field_objects(lease_layer)
    search_fields = [field.name for field in search_field_objs]
    insert_fields = search_fields[:]
    insert_fields.append('SHAPE@')

    with arcpy.da.InsertCursor(lease_layer, insert_fields) as insert_cursor:

        with arcpy.da.SearchCursor(dissolve_layer, [cfg.DISSOLVE_FIELD, 'SHAPE@']) as dissolve_cursor:
            for dissolve_row in dissolve_cursor:

                query = f"{cfg.DISSOLVE_FIELD} = '{dissolve_row[0]}'"
                with arcpy.da.SearchCursor(lease_table, search_fields, query) as search_cursor:
                    for search_row in search_cursor:
                        insert_row = list(search_row)
                        insert_row.append(dissolve_row[1]) # Add the shape from the dissolve

                        insert_cursor.insertRow(insert_row)

                        break # Take only the first row of lease data. Assumes rest are the same.


def get_meridian(meridian_num:Union[int, str]) -> str:
    '''
    Normalize the meridian number.
    '''
    if meridian_num == None:
        raise ValueError('Empty value value in meridian number')

    meridian = str(meridian_num)

    if not meridian.isdigit():
        raise ValueError('Improper value in meridian number')
    elif len(meridian) > 2:
        raise ValueError('meridian greater than two digits presented. Unable to process.')

    if len(meridian) == 1:
        meridian = "0" + meridian

    return meridian


def get_township(township_field:str) -> str:
    '''
    Normalize the township number
    '''
    if township_field == None or len(township_field) == 0:
        raise ValueError('Empty string presented in township data')

    test_string = township_field.lower()
    test_string = test_string.replace(' ', '')

    if 'n' not in test_string and 's' not in test_string:
        raise ValueError('No directional value provided in township data')

    if 'n' in test_string:
        township_direction = 'N'
        test_string = test_string.replace('n', '')
    else:
        township_direction = 'S'
        test_string = test_string.replace('s', '')

    if '.5' in test_string:
        township_fraction = '2'
        test_string = test_string.replace('.5', '')
    else:
        township_fraction = '0'

    if not test_string.isdigit():
        raise ValueError('Unknown characters in township data')

    padding = 3 - len(test_string)
    township_num = '0' * padding
    township_num = township_num + test_string

    # format of ID: NNNFD
        # NNN 3 digits, starting with zero
        # F fractional - either 0, 2
        # D directional - either N or S

    township_id = township_num + township_fraction + township_direction

    return township_id


def get_range(range_field:str) -> str:
    '''
    Normalize the range number
    '''
    if range_field == None or len(range_field) == 0:
        raise ValueError('Empty string presented in range data')

    test_string = range_field.lower()
    test_string = test_string.replace(' ', '')

    if 'e' not in test_string and 'w' not in test_string:
        raise ValueError('No directional value provided in range data')

    if 'e' in test_string:
        range_direction = 'E'
        test_string = test_string.replace('e', '')
    else:
        range_direction = 'W'
        test_string = test_string.replace('w', '')

    if '.5' in test_string:
        range_fraction = '2'
        test_string = test_string.replace('.5', '')
    else:
        range_fraction = '0'

    if not test_string.isdigit():
        raise ValueError('Unknown characters in range data')

    padding = 3 - len(test_string)
    range_num = '0' * padding
    range_num = range_num + test_string

    # format of ID: NNNFD
        # NNN 3 digits, starting with zero
        # F fractional - either 0, 2
        # D directional - either N or S

    range_id = range_num + range_fraction + range_direction

    return range_id


def get_section(section_num:Union[int, str]) -> str:
    '''
    Normalize the section number. Can accept either
    string or integer input
    '''
    if section_num == None:
        raise ValueError('Empty value value in section number')

    section = str(section_num)

    if not section.isdigit():
        raise ValueError('Improper value in section number')
    elif len(section) > 2:
        raise ValueError('Section greater than two digits presented. Unable to process.')

    if len(section) == 1:
        section = "0" + section

    return section


def write_error_file(error_records:List, out_file:str) -> None:
    '''
    Write the error records out to a csv file
    '''
    with open(out_file, 'w', newline='') as csv_file:
        write_file = csv.writer(csv_file)
        write_file.writerows(error_records)


def main(excel_file, output_gdb, lease_lyr_name, date_tag):
    '''
    Create new lease layer combination of Excel data and PLSS
    polygons
    '''
    arcpy.env.workspace = output_gdb
    arcpy.overwriteOutputs = True
    arcpy.env.overwriteOutput = True

    lease_lyr_name_tagged = get_clean_name(lease_lyr_name)
    lease_lyr_name_tagged = lease_lyr_name_tagged + "_" + date_tag

    if arcpy.Exists(lease_lyr_name_tagged):
        arcpy.AddError(f'Target new lease layer {lease_lyr_name_tagged} already exists. Rename or delete and rerun the script.')
        return

    if not os.path.exists(excel_file):
        arcpy.AddError('Cannot find Excel file for lease input. Correct and rerun script.')
        return

    arcpy.AddMessage('Creating temp lease layer')
    temp_lyr_name = "Temp_Lease_Layer_" + date_tag
    arcpy.CreateFeatureclass_management(
        out_path=output_gdb,
        out_name=temp_lyr_name,
        geometry_type="POLYGON",
        template=cfg.FC_TEMPLATE,
        spatial_reference=cfg.FC_TEMPLATE)
    temp_lease_lyr_fc = os.path.join(output_gdb, temp_lyr_name)

    # This will overwrite a table by the same name if it exists
    arcpy.AddMessage('Setting up temp lease table')
    temp_tbl_name = "Temp_Lease_Table_" + date_tag
    create_temp_table(output_gdb, temp_tbl_name, cfg.FC_TEMPLATE)
    temp_lease_tbl = os.path.join(output_gdb, temp_tbl_name)

    arcpy.AddMessage('Loading Excel lease data to lease table')
    lease_data_df = get_excel_data(excel_file)
    load_lease_table(lease_data_df, temp_lease_tbl)

    arcpy.AddMessage('Adding PLSS lookup fields to temp table and temp layer')
    layers_to_adjust = [temp_lease_lyr_fc, temp_lease_tbl]
    add_fields(layers_to_adjust)

    # This needed to match Excel column headers to table field names/alias
    tbl_fields = arcpy.ListFields(temp_lease_tbl)
    field_lookup = {field.aliasName:field.name for field in tbl_fields}

    arcpy.AddMessage('Updating table with first division ID')
    update_errors = update_lease_table(temp_lease_tbl, field_lookup)
    if update_errors > 0:
        arcpy.AddWarning(f'{update_errors} errors found in First Div update of lease table')
        arcpy.AddMessage('See the error column of the lease table for details')
    else:
        arcpy.AddMessage('No errors found in First Div update of lease table')

    arcpy.AddMessage('Getting PLSS features from first pass lease data')
    lease_tbl_mirror = _build_lease_tbl_mirror(temp_lease_tbl, field_lookup)

    plss_results = get_plss_features(temp_lease_lyr_fc, lease_tbl_mirror, field_lookup)

    if plss_results['error_count'] > 0:
        arcpy.AddWarning('See PLSS error file for records with no PLSS match')
        write_error_file(plss_results['error_records'], cfg.ERROR_FILE)

    arcpy.AddMessage(f'Performing dissolve on {cfg.DISSOLVE_FIELD} field')
    dissolve_name = "Temp_Dissolve_Lyr_" + date_tag
    arcpy.PairwiseDissolve_analysis(
        in_features = temp_lease_lyr_fc,
        out_feature_class = dissolve_name,
        dissolve_field = cfg.DISSOLVE_FIELD
    )

    arcpy.AddMessage('Creating new lease layer')
    arcpy.CreateFeatureclass_management(
        out_path=output_gdb,
        out_name=lease_lyr_name_tagged,
        geometry_type="POLYGON",
        template=cfg.FC_TEMPLATE,
        spatial_reference=cfg.FC_TEMPLATE)
    lease_lyr_fc = os.path.join(output_gdb, lease_lyr_name_tagged)

    arcpy.AddMessage('Merging data from lease table with dissolve layer')
    insert_and_merge_data(lease_lyr_fc, temp_lease_tbl, dissolve_name)


#<<<<<<<<<<<<<<<     >>>>>>>>>>>>>>>
if __name__ == '__main__':

    arcpy.AddMessage('Starting legal description feature layer creation')

    main(cfg.EXCEL_INPUT, cfg.OUTPUT_GDB, cfg.OUTPUT_LYR, cfg.DATE_TAG )

    arcpy.AddMessage('Script completed')
