# -*- coding: utf-8 -*-

import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [LegalDescriptionToFeature]


class LegalDescriptionToFeature(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Legal Description To Feature"
        self.description = "Legal Description To Feature"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""

        excelFile = arcpy.Parameter(
            displayName="Excel file input",
            name="excelFile",
            datatype="GPDataFile",
            parameterType="Required",
            direction="Input")

        outputFileLoc = arcpy.Parameter(
            displayName="GDB for the output",
            name="outputFileLoc",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")

        outputFile = arcpy.Parameter(
            displayName="Name of output layer",
            name="outputFile",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        dateTag = arcpy.Parameter(
            displayName="Date tag in the format of YYYYMMDD",
            name="dateTag",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        return [excelFile, outputFileLoc, outputFile, dateTag]

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        arcpy.AddMessage('Importing modules for the tool')
        import legal_description_to_feature as tool_script

        excelFile = arcpy.GetParameterAsText(0)
        outputFileLoc = arcpy.GetParameterAsText(1)
        outputFile = arcpy.GetParameterAsText(2)
        dateTag = arcpy.GetParameterAsText(3)

        tool_script.main(excelFile, outputFileLoc, outputFile, dateTag)

        return
