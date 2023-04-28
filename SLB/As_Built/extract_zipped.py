import os
import shutil
import zipfile

source_folder = r'C:\Users\shawn\DataScienceMaster\Code\SLB\As_Built'
target_folder = r'C:\Users\shawn\DataScienceMaster\Code\SLB\As_Built_Extracted'

if not os.path.exists(target_folder):
    os.makedirs(target_folder)

for root, dirs, files in os.walk(source_folder):
    for file in files:
        # extract any zip files
        if file.endswith('.zip'):
            file_path = os.path.join(root, file)
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(target_folder)
        else:
            # copy all other files to target folder
            src_path = os.path.join(root, file)
            dst_path = os.path.join(target_folder, file)
            shutil.copy2(src_path, dst_path)
