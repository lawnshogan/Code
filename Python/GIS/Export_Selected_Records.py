import arcpy

# Set the workspace to the GDB location
arcpy.env.workspace = r"G:\Shared drives\SLB Business Intelligence\Data Services\GIS\Projects\Active\2023\SLB Wall Maps\2023\WallMapData.gdb"

# Set the input feature class
in_fc = "USA_Federal_Lands"

# Create a list of unique values in the "Agency" field
unique_values = list(set([row[0] for row in arcpy.da.SearchCursor(in_fc, ["Agency"])]))


