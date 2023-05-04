import os
import shutil
import zipfile

source_folder = r'C:\Users\shawn\DataScienceMaster\Code\SLB\As_Built'
target_folder = r'C:\Users\shawn\DataScienceMaster\Code\SLB\As_Built_Extracted'

if not os.path.exists(target_folder):
    os.makedirs(target_folder)f

for root, dirs, files in os.walk(source_folder):
    for file in files:
        # extract any zip files
        if file.endswith('.zip'):
            file_path = os.path.join(root, file)
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                # create the same folder structure in the target folder
                zip_ref.extractall(os.path.join(target_folder, os.path.relpath(root, source_folder)))
        else:
            # copy all other files to target folder with the same folder structure
            src_path = os.path.join(root, file)
            dst_path = os.path.join(target_folder, os.path.relpath(root, source_folder), file)
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            shutil.copy2(src_path, dst_path)
