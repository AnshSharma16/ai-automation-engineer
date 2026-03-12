import os

folder_path = "sample_files"

files = os.listdir(folder_path)

for i, file in enumerate(files):

    old_path = os.path.join(folder_path, file)

    extension = file.split(".")[-1]

    new_name = f"file_{i+1}.{extension}"

    new_path = os.path.join(folder_path, new_name)

    os.rename(old_path, new_path)

print("Files renamed successfully!")