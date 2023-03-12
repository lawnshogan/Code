######################### HOW TO RUN THIS SCRIPT ########################

# 1.  Set the values of the following variables at the beginning of the script to the paths and names of your actual data and resources:

#         excelFile: The path and name of the input Excel file.
#         lots: The path and name of the feature class or shapefile containing the base polygons.
#         newFeatures: The path and name of the output feature class or shapefile.
#         outputFileLoc: The file path of the directory where an output table and feature class will be saved.
#         YYYYMMDD: A string or integer value that will be used to create the output file name. (e.g. "20230104" for January 4th, 2023)
#         outputFile: The name of the output file that will be saved in the outputFileLoc directory

# 2.  Set the value of the 'idField' variable to the name of the field in the input Excel file that contains the legal descriptions.

# 3.  Set the value of the 'lotTest' variable to "null" (unless you want to use a different value).

# 4.  Set the value of the 'outputFile' variable to the desired name for the output feature class.

# 5.  Use the 'arcpy.TableToTable_conversion()' function to convert the input Excel file to a table in a new file located 
#     in the 'outputFileLoc' directory, and name the new table "TempTable_One".

# 6.  Use the 'arcpy.CreateFeatureclass_management()' function to create a new feature class in the 'outputFileLoc' directory, 
#     using the 'template' feature class as a guide for the field names and data types. Name the feature class using the value of the 'outputFile' variable.

# 7.  Use a for loop to loop through each field in the 'fields' list. If the name of the current field is equal to the value of the 'idField' variable, 
#     use the 'arcpy.AddField_management()' function to add a new field called "INDEX_NUM" to the inTable table.

# 8.  Define a list of field names called 'cursorFields' and use it to create an update cursor for the 'inTable' table. 
#     Loop through each row in the cursor and perform the tasks listed in the script.

# 9.  When the script is finished running, the output feature class will contain the generated polygons based on the legal descriptions in the input Excel file.



###################################### Getting parameters from tool properties ######################################

import arcpy, math, os, sys
from arcpy import env

excelFile = arcpy.GetParameterAsText(0)
outputFileLoc = arcpy.GetParameterAsText(1)
outputFile = arcpy.GetParameterAsText(2)
YYYYMMDD = arcpy.GetParameterAsText(3)

############################################### Function Definitions ##############################################################

#####test##############################################################################################################################

########################################## Function for building a where clause from a list object ################################

# This function takes three parameters: 'table', 'field', and 'valueList'. 
# The function is used to build a WHERE clause for an ArcGIS Pro selection query.

# The 'table' parameter is the name of a table or feature class. The 'field' parameter is the name of a field in the table. 
# The 'valueList' parameter is a list of values that you want to use to filter the data in the table.

# The function first uses the 'arcpy.AddFieldDelimiters()' function to add the appropriate field delimiters to the 'field' parameter. 
# This is necessary because the field name may contain spaces or special characters
# Adding the delimiters ensures that the field name is correctly interpreted by ArcGIS Pro.

# Next, the function uses the 'arcpy.ListFields()' function to get the data type of the field specified by the 'field' parameter. 
# If the field is a string field, the function will enclose each value in single quotes in the 'valueList' parameter. 
# This is necessary because string values in an ArcGIS Pro selection query must be enclosed in single quotes.

# Finally, the function builds and returns the WHERE clause by concatenating the delimited field name, the string " IN(", the comma-separated list of values, and the string ")". 
# The resulting WHERE clause will look something like this: "field_name IN('value1', 'value2', 'value3')". 
# This WHERE clause can be used to filter the data in the table by selecting only those records where the value in the field field is one of the values in the valueList parameter.

def buildWhereClauseFromList(table, field, valueList):
    fieldDelimited = arcpy.AddFieldDelimiters(arcpy.Describe(table).path, field)
    fieldType = arcpy.ListFields(table, field)[0].type
    if str(fieldType) == 'String':
        valueList = ["'%s'" % value for value in valueList]
    whereClause = "%s IN(%s)" % (fieldDelimited, ', '.join(map(str, valueList)))
    return whereClause



############################## Function for generating polygons based on string type legal descriptions ##########################################

# This function takes five parameters: legalList, tempFeat_1, tempFeat_2, newFeatures, and Sctn, ID, LN, TownRange, legal. 
# The function is used to generate polygons from a list of legal descriptions.

# The 'legalList' parameter is a list of legal descriptions. The 'tempFeat_1' and 'tempFeat_2' parameters are the names of temporary feature classes 
# that will be used as intermediate steps in the process of generating the polygons. The 'newFeatures' parameter is the name of the final output 
# feature class that will contain the generated polygons. The 'Sctn', 'ID', 'LN', 'TownRange', and 'legal' parameters are values that will be added to the 
# output feature class as attributes.

# The function first uses the 'arcpy.Select_analysis()' function to select all the features in the lots feature class where the FRSTDIVID field is equal to the FDI value. 
# It then uses the 'buildWhereClauseFromList()' function (which was defined earlier in the script) to build a WHERE clause based on the 'legalList' parameter. 
# The function then uses the 'arcpy.Select_analysis()' function again to select only those features in the 'tempFeat_1' feature class that meet the criteria specified in the WHERE clause.

# Next, the function uses the 'arcpy.Delete_management()' function to delete the 'tempFeat_1' feature class, and then uses the 'arcpy.Dissolve_management()' function to dissolve the 'tempFeat_2' feature class. 
# It then uses the 'arcpy.AddField_management()' function to add two new fields to the 'tempFeat_1' feature class: 'INDEX_NUM and LEGAL_DESCRIPTION'.

# The function then uses an update cursor to loop through each row in the 'tempFeat_1' feature class and updates the values in the INDEX_NUM and LEGAL_DESCRIPTION fields. 
# It sets the value of the INDEX_NUM field to the 'ID' parameter and the value of the LEGAL_DESCRIPTION field to the 'legal' parameter.

# Finally, the function uses the 'arcpy.Append_management()' function to append the 'tempFeat_1' feature class to the 'newFeatures' feature class, and then uses the 'arcpy.Delete_management()' function to delete the temporary feature classes. 
# It also displays a success message and the values of the 'LN', 'TownRange', 'Sctn', and 'legal' parameters.


def makeFeaturesFromLegalDescriptions(legalList, tempFeat_1, tempFeat_2, newFeatures, Sctn, ID, LN, TownRange, legal):
    try:
        arcpy.Select_analysis(lots, tempFeat_1, '"FRSTDIVID" = ' + "'%s'" %FDI)
        qry = buildWhereClauseFromList(tempFeat_1, "SECDIVNO", legalList)
        arcpy.Select_analysis(tempFeat_1, tempFeat_2, qry)
        arcpy.Delete_management(tempFeat_1, "")
        arcpy.Dissolve_management(tempFeat_2, tempFeat_1)
        arcpy.AddField_management(tempFeat_1, "INDEX_NUM", "LONG")
        arcpy.AddField_management(tempFeat_1, "LEGAL_DESCRIPTION", "TEXT", "", "", 50)
        curFields = ('INDEX_NUM', 'LEGAL_DESCRIPTION')
        with arcpy.da.UpdateCursor(tempFeat_1, curFields) as cursor_2:
            for row in cursor_2:
                row[0] = long(ID)
                row[1] = '%s' % ', '.join(map(str, legal))
                cursor_2.updateRow(row)
        arcpy.Append_management([tempFeat_1], newFeatures, "NO_TEST","","")
        arcpy.Delete_management(tempFeat_1, "")
        arcpy.Delete_management(tempFeat_2, "")
        arcpy.AddMessage("Feature created successfully!")
        arcpy.AddMessage("Lease #: " + str(LN))
        arcpy.AddMessage("Township/Range: " + str(TownRange))
        arcpy.AddMessage("Section: " + str(Sctn))
        arcpy.AddMessage("Legal Description: " + str(legal))
        del cursor_2
    except:
        arcpy.AddWarning("The following feature could not be created.  Please check the following information in the input table: ")
        arcpy.AddWarning("Lease #: " + str(LN))
        arcpy.AddWarning("Township/Range: " + str(TownRange))
        arcpy.AddWarning("Section: " + str(Sctn))
        arcpy.AddWarning("Legal Description: " + str(legal))
        arcpy.AddMessage(" ")
        arcpy.AddWarning("Auto-digitization of legal descriptions starting now!")

######################################## Initialize objects/file paths/tables ####################################################


##### 1. This code sets the value of the 'idField' variable to the string "LEG_DESC", the value of the 'lotTest' variable to the string "null", and the value of the 
#####     'outputFile' variable to the value of the 'outputFile' variable, followed by an underscore, followed by the value of the 'YYYYMMDD' variable.

##### 2. It then uses the 'arcpy.TableToTable_conversion()' function to convert the Excel file specified by the 'excelFile' variable 
#####     to a table in a new file located in the 'outputFileLoc' directory, and names the new table "TempTable_One".

##### 3. The code sets the value of the 'inTable' variable to the path of the newly created table, and then sets the value of the 'template' variable to the path of a template feature class in a geodatabase.

##### 4. It then uses the 'arcpy.CreateFeatureclass_management()' function to create a new feature class in the 'outputFileLoc' directory, using the 'template' feature class as a guide for the field names and data types. 
#####     The feature class is named using the value of the 'outputFile' variable.

##### 5. The code sets the value of the 'newFeat' variable to the path of the newly created feature class, and then sets the value of the 'lots' variable to the path 
#####     of a feature class in a geodatabase. It also sets the values of the 'TF1' and 'TF2' variables to the paths of two temporary feature classes in a different geodatabase.

##### 6. Finally, the code sets the value of the idNum variable to 0 and uses the arcpy.ListFields() function to get a list of all the string fields in the inTable table.

idField = "LEG_DESC"
lotTest = "null"
outputFile = str(outputFile) + "_" + str(YYYYMMDD)
arcpy.TableToTable_conversion(excelFile, outputFileLoc, "TempTable_One")
inTable = os.path.join(outputFileLoc, "TempTable_One")
template = r'F:\DRAFTING\ArcGIS Drafting Projects\WTD\NM\_Master Data\WorkingData_John.gdb\TEMPLATE_FOR_AUTO_DIGITIZE_TOOL'
arcpy.CreateFeatureclass_management(outputFileLoc, outputFile, "POLYGON", template, "DISABLED", "DISABLED", template)
newFeat = os.path.join(outputFileLoc, outputFile)
lots = r'F:\DRAFTING\ArcGIS Drafting Projects\WTD\NM\_Master Data\SE_NM_Map.gdb\Lots'
TF1 = r'F:\DRAFTING\ArcGIS Drafting Projects\WTD\NM\_Master Data\WorkingData_John.gdb\Temp_Features_1'
TF2 = r'F:\DRAFTING\ArcGIS Drafting Projects\WTD\NM\_Master Data\WorkingData_John.gdb\Temp_Features_2'
idNum = 0
fields = arcpy.ListFields(inTable, "", "String")

######################################## Setting the ability for the script to overwrite previous outputs of the same name #######################################
arcpy.overwriteOutputs = True        
arcpy.env.overwriteOutput = True

####################################################### Script for execution of tool ####################################################



# 1.  This code is looping through each field in the 'fields' list. 
#     If the name of the current field is equal to the value of the 'idField' variable (which is "LEG_DESC"), the code uses the 'arcpy.AddField_management()' function 
#     to add a new field called "INDEX_NUM" to the inTable table.

# 2.  The code then defines a list of field names called 'cursorFields' and uses it to create an update cursor for the 'inTable' table. 
#     It then loops through each row in the cursor and performs the following tasks:

#     1.  Sets the value of the leaseNumber variable to the value of the sixth field in the row (the "LEASE" field).
#     2.  Creates an empty list called legalDescriptions and an empty list called lotDesc.
#     3.  Sets the value of the strLegal variable to the value of the first field in the row (the "LEG_DESC" field) as a string.
#     4.  Removes all spaces from the value of the "LEG_DESC" field and sets the result to the noSpace variable.
#     5.  Splits the noSpace variable into a list of individual legal descriptions and sets the result to the listLD variable.
#     6.  Sets the value of the SEC variable to the value of the second field in the row (the "SECTION" field) as an integer.
#     7.  Sets the value of the section variable to the value of the SEC variable as a string. If the length of the SEC variable is 1, it adds a "0" to the beginning of the string. If the length is 2, it sets the section variable to the SEC variable as is.

#     8.  Sets the value of the TR variable to the value of the third field in the row (the "TWP_RNG" field).
#     9.  Removes all hyphens, spaces, and commas from the value of the "TWP_RNG" field and sets the result to the twpID variable.
#     10. Replaces the "T" and "R" characters in the twpID variable with nothing, and replaces the "S" character with "0S0".
#     11. Creates a string called `secPart




for field in fields:
    if field.name == str(idField):
        arcpy.AddField_management(inTable, "INDEX_NUM", "LONG")
        cursorFields = ('LEG_DESC', 'SECTION', 'TWP_RNG', 'SEC_TWP_ID', 'INDEX_NUM', 'LEASE')
        with arcpy.da.UpdateCursor(inTable, cursorFields) as cursor:
            for row in cursor:
                leaseNumber = str(row[5])
                legalDescriptions = []
                lotDesc = []
                strLegal = str(row[0])
                noSpace = row[0].replace(" ", "")
                listLD = noSpace.split(",")
                SEC = str(int(row[1]))
                section = str(int(SEC))
                if len(str(SEC)) == 1:
                    section = "0" + str(SEC)
                if len(str(SEC)) == 2:
                    section = str(SEC)
                TR = row[2]
                twpID = row[2].replace("-", "")     #### Parsing the twp/rng, section identifier ####
                twpID = twpID.replace(" ", "")
                twpID = twpID.replace("T", "")
                twpID = twpID.replace("R", "")
                twpID = twpID.replace(",", "")
                twpID = twpID.replace("S", "0S0")
                secPart = "0E0SN" + str(section) + "0"
                twpID = twpID.replace("E", secPart)
                FDI = "NM230" + twpID
                row[4] = idNum
                row[3] = FDI
                cursor.updateRow(row)
                for legD in listLD:
                    piece = legD.replace("Lot", "") 
                    piece = piece.replace("s", "")              
                    legalDescriptions.append(str(piece))
                for LD in legalDescriptions:
                    if len(str(LD)) <= 2:
                        lotDesc.append(LD)
                        lotTest = "true"
                    elif len(str(LD)) > 2:
                        arcpy.AddMessage(" ")
                        cont = "true"

################################################ Transcriptions of Legal Descriptions ########################################################

                        #Halves - 4
                        if LD == "E1/2":
                            LegalList = ["NWNE","NENE","SWNE","SENE","NWSE","NESE","SWSE","SESE"]#
                        elif LD == "W1/2":
                            LegalList = ["NWNW","NENW","SWNW","SENW","NWSW","NESW","SWSW","SESW"]#
                        elif LD == "S1/2":
                            LegalList = ["NWSW","NESW","SWSW","SESW","NWSE","NESE","SWSE","SESE"]#
                        elif LD == "N1/2":
                            LegalList = ["NWNW","NENW","SWNW","SENW","NWNE","NENE","SWNE","SENE"]#

                        #Quarters - 4   
                        elif LD == "NW1/4":
                            LegalList = ["NWNW","NENW","SWNW","SENW"]#
                        elif LD == "NE1/4":
                            LegalList = ["NWNE","NENE","SWNE","SENE"]#
                        elif LD == "SW1/4":
                            LegalList = ["NWSW","NESW","SWSW","SESW"]#
                        elif LD == "SE1/4":
                            LegalList = ["NWSE","NESE","SWSE","SESE"]#

                        #Half Quarters - 16  
                        elif LD == "W1/2NW1/4":
                            LegalList = ["NWNW","SWNW"]#
                        elif LD == "E1/2NW1/4":
                            LegalList = ["NENW","SENW"]#
                        elif LD == "N1/2NW1/4":
                            LegalList = ["NWNW","NENW"]#
                        elif LD == "S1/2NW1/4":
                            LegalList = ["SWNW","SENW"]#

                        elif LD == "W1/2NE1/4":
                            LegalList = ["NWNE","SWNE"]#
                        elif LD == "E1/2NE1/4":
                            LegalList = ["NENE","SENE"]#
                        elif LD == "N1/2NE1/4":
                            LegalList = ["NWNE","NENE"]#
                        elif LD == "S1/2NE1/4":
                            LegalList = ["SWNE","SENE"]#

                        elif LD == "W1/2SW1/4":
                            LegalList = ["NWSW","SWSW"]#
                        elif LD == "E1/2SW1/4":
                            LegalList = ["NESW","SESW"]#
                        elif LD == "N1/2SW1/4":
                            LegalList = ["NWSW","NESW"]#
                        elif LD == "S1/2SW1/4":
                            LegalList = ["SWSW","SESW"]#

                        elif LD == "W1/2SE1/4":
                            LegalList = ["NWSE","SWSE"]#
                        elif LD == "E1/2SE1/4":
                            LegalList = ["NESE","SESE"]#
                        elif LD == "N1/2SE1/4":
                            LegalList = ["NWSE","NESE"]#
                        elif LD == "S1/2SE1/4":
                            LegalList = ["SWSE","SESE"]#

                        #Half Halves - 8   
                        elif LD == "W1/2W1/2":
                            LegalList = ["NWNW","SWNW","NWSW","SWSW"]#
                        elif LD == "E1/2W1/2":
                            LegalList = ["NENW","SENW","NESW","SESW"]#
                        elif LD == "W1/2E1/2":
                            LegalList = ["NWNE","SWNE","NWSE","SWSE"]#
                        elif LD == "E1/2E1/2":
                            LegalList = ["NENE","SENE","NESE","SESE"]#

                        elif LD == "N1/2N1/2":
                            LegalList = ["NWNW","NENW","NWNE","NENE"]#
                        elif LD == "S1/2N1/2":
                            LegalList = ["SWNW","SENW","SWNE","SENE"]#
                        elif LD == "N1/2S1/2":
                            LegalList = ["NWSW","NESW","NWSE","NESE"]#
                        elif LD == "S1/2S1/2":
                            LegalList = ["SWSW","SESW","SWSE","SESE"]#

                        #Quarter Quarters - 16
                        elif LD == "NW1/4NW1/4":
                            LegalList = ["NWNW"]#
                        elif LD == "NE1/4NW1/4":
                            LegalList = ["NENW"]#
                        elif LD == "SW1/4NW1/4":
                            LegalList = ["SWNW"]#
                        elif LD == "SE1/4NW1/4":
                            LegalList = ["SENW"]#

                        elif LD == "NW1/4NE1/4":
                            LegalList = ["NWNE"]#
                        elif LD == "NE1/4NE1/4":
                            LegalList = ["NENE"]#
                        elif LD == "SW1/4NE1/4":
                            LegalList = ["SWNE"]#
                        elif LD == "SE1/4NE1/4":
                            LegalList = ["SENE"]#

                        elif LD == "NW1/4SW1/4":
                            LegalList = ["NWSW"]#
                        elif LD == "NE1/4SW1/4":
                            LegalList = ["NESW"]#
                        elif LD == "SW1/4SW1/4":
                            LegalList = ["SWSW"]#
                        elif LD == "SE1/4SW1/4":
                            LegalList = ["SESW"]#

                        elif LD == "NW1/4SE1/4":
                            LegalList = ["NWSE"]#
                        elif LD == "NE1/4SE1/4":
                            LegalList = ["NESE"]#
                        elif LD == "SW1/4SE1/4":
                            LegalList = ["SWSE"]#
                        elif LD == "SE1/4SE1/4":
                            LegalList = ["SESE"]#

                        #All - 1
                        elif LD == "All":
                            LegalList = ["NWNE","NENE","SWNE","SENE","NWSE","NESE","SWSE","SESE","NWNW","NENW","SWNW","SENW","NWSW","NESW","SWSW","SESW","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36"]#
                        else:
                            arcpy.AddWarning("The current legal description was not recognized!  Feature was not created.")
                            arcpy.AddWarning("Lease #: " + str(leaseNumber))
                            arcpy.AddWarning("Township/Range: " + str(TR))
                            arcpy.AddWarning("Section: " + str(section))
                            arcpy.AddWarning("Legal Description: " + str(LD))
                            cont = "false"
                        if cont == "true":
                            strLegal = str(LD)
                            makeFeaturesFromLegalDescriptions(LegalList, TF1, TF2, newFeat, section, idNum, leaseNumber, TR, LD)
                if lotTest == "true":
                    arcpy.AddMessage(" ")
                    strLegal = str(row[0])
                    makeFeaturesFromLegalDescriptions(lotDesc, TF1, TF2, newFeat, section, idNum, leaseNumber, TR, lotDesc)
                    lotTest = "false"
                idNum += 1
        arcpy.JoinField_management(newFeat, "INDEX_NUM", inTable, "INDEX_NUM")
        arcpy.DeleteField_management(newFeat, ["LEG_DESC"])
        del cursor
        arcpy.AddMessage(" ")