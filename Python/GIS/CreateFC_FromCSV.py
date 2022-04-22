import csv
import arcpy
import sys
import os

# Allow overwriting of outputs
arcpy.env.overwriteOutput = True

# Root Directory - Where the output goes.
root_directory = 'C:\\Users\\shawn\\DataScienceMaster\\Code\\'

# Setup output feature class
print("creating new feature class")

# Define projection
prj = root_directory + "wgs_84.prj"

# Create empty shapefile using arcpy
Output_FC = arcpy.CreateFeatureclass_management(root_directory, "311.shp", "POINT", "", "DISABLED", prj)
print("finished creating new feature class")

# Write the fields from the csv file into the empty shapefile
file_in = root_directory + 'CSV_FILE_TITLE.csv'

# Define the fields from csv you want to include in shapefile
LAT_field = "LATITUDE"
LON_field = "LONGITUDE"
OVERDUE_field = "OVERDUE"
SR_TYPE_field = "SR TYPE"
