
###################################### Getting parameters from tool properties ######################################

import arcpy, math, os, sys
from arcpy import env

excelFile = arcpy.GetParameterAsText(0)
outputFileLoc = arcpy.GetParameterAsText(1)
outputFile = arcpy.GetParameterAsText(2)
YYYYMMDD = arcpy.GetParameterAsText(3)

def buildWhereClauseFromList(table, field, valueList):
    fieldDelimited = arcpy.AddFieldDelimiters(arcpy.Describe(table).path, field)
    fieldType = arcpy.ListFields(table, field)[0].type
    if str(fieldType) == 'String':
        valueList = ["'%s'" % value for value in valueList]
    whereClause = "%s IN(%s)" % (fieldDelimited, ', '.join(map(str, valueList)))
    return whereClause


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


arcpy.overwriteOutputs = True        
arcpy.env.overwriteOutput = True


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

test
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