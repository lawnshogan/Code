'''
Configured values to use the script outside the Pro toolbox
environment
'''
import os
from datetime import datetime as dt

#<<<<<<<<<<<<<<<     >>>>>>>>>>>>>>>



# Parameters in the toolbox
# EXCEL_INPUT = r'C:\Projects\CSLB\data\GIS Lease Update.xlsx'
# OUTPUT_GDB = r'C:\Users\ckalinski\Documents\ArcGIS\Projects\CSLB-LegalDesc\CSLB-LegalDesc.gdb'
OUTPUT_LYR = 'NewLeaseLayer'
# DATE_TAG = '20230315'

#TODO remove this and un-comment items above...
EXCEL_INPUT = r'C:\Projects\CSLB\data\GIS Lease Update_small test.xlsx'
OUTPUT_GDB = r'C:\Users\CKaya\Documents\ArcGIS\Projects\CSLB-LegalDesc\CSLB-LegalDesc.gdb'
DATE_TAG = dt.now().strftime('%Y%m%d_%H%M')


FC_TEMPLATE = r'C:\Users\CKaya\Documents\ArcGIS\Projects\CSLB-LegalDesc\CSLB-LegalDesc.gdb\schema'

PLSS = r'C:\Users\CKaya\Documents\ArcGIS\Projects\CSLB-LegalDesc\BLM_CO_PLSS_Intersected_Survey_Grid.gdb\BLM_Colorado_PLSS_Intersected___Survey_Grid'

DISSOLVE_FIELD = 'Transaction_Number'

ERROR_FILE = os.path.join(r'C:\Projects\CSLB', f'PLSS_Error_Records_{DATE_TAG}')


#<<<<<<<<<<<<<<<     >>>>>>>>>>>>>>>
# Possible PLSS source if needed
# https://gis.blm.gov/coarcgis/rest/services/cadastral/BLM_CO_PLSS/MapServer
# https://gbp-blm-egis.hub.arcgis.com/search?categories=cadastral&groupIds=97bb25da078444d4a04669405f77643b

# Cadastral
# https://data.colorado.gov/Local-Aggregation/Statewide-Aggregate-Parcels-in-Colorado-2022-Publi/izys-vycy
