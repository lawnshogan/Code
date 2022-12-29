import csv
import xlsxwriter
import arcpy

# Set the input CSV file and output Excel file
csv_file = r"C:\input\file.csv"
xlsx_file = r"C:\output\file.xlsx"

# Create an Excel workbook and add a worksheet
workbook = xlsxwriter.Workbook(xlsx_file)
worksheet = workbook.add_worksheet()

# Read the CSV file and write it to the Excel worksheet
with open(csv_file, "r") as f:
    reader = csv.reader(f)
    for r, row in enumerate(reader):
        for c, col in enumerate(row):
            worksheet.write(r, c, col)

# Close the Excel workbook
workbook.close()

# Set the input and output for the Excel to Table tool
in_table = xlsx_file
out_table = r"C:\output\table.dbf"

# Run the Excel to Table tool
arcpy.ExcelToTable_conversion(in_table, out_table)
