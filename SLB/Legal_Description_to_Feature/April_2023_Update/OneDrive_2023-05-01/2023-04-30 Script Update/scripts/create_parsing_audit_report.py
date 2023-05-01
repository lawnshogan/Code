'''
'''
import os
import csv

import config as cfg
import legal_description_to_feature as ld
import ld_parser

#<<<<<<<<<<<<<<<     >>>>>>>>>>>>>>>

def main():
    '''Main'''

    # excel_file = r'C:\Projects\CSLB\data\GIS Lease Update_full_list.xlsx'
    excel_file = cfg.EXCEL_INPUT

    lease_data_df = ld.get_excel_data(excel_file)


    temp_file = os.path.join(r'C:\Projects\CSLB', cfg.DATE_TAG + 'check_data.csv')

    header_row = ['Internal ID', 'Transaction Number', 'Meridian', 'Township', 'Range', 'Section#', 'Legal Description', 'Lookups', 'Lots', 'Fractionals', 'Misses']


    with open(temp_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header_row)

        for _, lease_data in lease_data_df.iterrows():
            ld_desc = lease_data['Legal Description']

            if ld_parser._check_for_all_values(ld_desc):
                new_row = [
                    lease_data['Internal ID'],
                    lease_data['Transaction Number'],
                    lease_data['Meridian'],
                    lease_data['Township'],
                    lease_data['Range'],
                    lease_data['Section#'],
                    lease_data['Legal Description'],
                    'ALL - full section',
                    'na',
                    'na',
                    'na'
                    ]
            elif ld_parser._has_exceptions_in_alls(ld_desc):
                new_row = [
                    lease_data['Internal ID'],
                    lease_data['Transaction Number'],
                    lease_data['Meridian'],
                    lease_data['Township'],
                    lease_data['Range'],
                    lease_data['Section#'],
                    lease_data['Legal Description'],
                    'ALL EXCEPTION - TO BE SKIPPED',
                    'na',
                    'na',
                    'na'
                    ]
            else:
                results = ld_parser._parse_for_search_items(ld_desc)
                new_row = [
                    lease_data['Internal ID'],
                    lease_data['Transaction Number'],
                    lease_data['Meridian'],
                    lease_data['Township'],
                    lease_data['Range'],
                    lease_data['Section#'],
                    lease_data['Legal Description'],
                    results['lookups'],
                    results['lots'],
                    results['fractionals'],
                    results['fall_outs']
                    ]

            writer.writerow(new_row)

    print(f'Report location: {temp_file}')

#<<<<<<<<<<<<<<<     >>>>>>>>>>>>>>>
if __name__ == '__main__':
    print('Script started')
    main()
    print('Script completed')
