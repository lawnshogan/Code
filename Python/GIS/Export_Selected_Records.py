import arcpy

# Set the workspace to the GDB location
arcpy.env.workspace = r"G:\Shared drives\SLB Business Intelligence\Data Services\GIS\Projects\Active\2023\SLB Wall Maps\2023\WallMapData.gdb"

# Set the input feature class
in_fc = "USA_Federal_Lands"

# Create a list of unique values in the "Agency" field
unique_values = list(set([row[0] for row in arcpy.da.SearchCursor(in_fc, ["Agency"])]))
test
# Loop through the unique values
for value in unique_values:
    # use the value from the "Agency" field as the output feature class name
    out_fc = value
    # Create a where clause to select the appropriate features
    where_clause = '"Agency" = ' + "'" + value + "'"
    # Use the Select_analysis tool to create a new feature class with the selected features
    arcpy.Select_analysis(in_fc, out_fc, where_clause)
