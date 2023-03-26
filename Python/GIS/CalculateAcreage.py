# Import necessary modules
import arcpy
from arcpy import env

# Set the workspace environment
env.workspace = "C:/data"
test
# Set the input feature class
input_fc = "parcels.shp"

# Set the field to calculate acreage for
eval_field = "Evaluation"

# Set the field to add the acreage values to
acreage_field = "Total_Acreage"

# Add the acreage field if it doesn't already exist
arcpy.AddField_management(input_fc, acreage_field, "DOUBLE")

# Create a search cursor to iterate through the rows
rows = arcpy.SearchCursor(input_fc)

# Iterate through the rows and calculate the acreage for each unique value in the evaluation field
for row in rows:
  eval_value = row.getValue(eval_field)
  acreage = row.getValue("SHAPE").getArea("GEODESIC", "ACRES")
  row.setValue(acreage_field, acreage)
  rows.updateRow(row)

# Delete the cursor and row objects
del row, rows
