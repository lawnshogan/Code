from zipfile import ZipFile

with ZipFile('name.zip', 'r') as zip_object:
    zip_object.extractall()
# List all files that are archived in the zip
print(zip_object.namelist())