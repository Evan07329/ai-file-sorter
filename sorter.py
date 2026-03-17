import os
import shutil


folder_to_sort = input("Please enter the path of the folder you want to sort: ").strip(" '\"")


extensions_map = {
    ".jpg": "Images",
    ".png": "Images",
    ".txt": "Documents",
    ".pdf": "Documents",
    ".mp4": "Videos",
    ".zip": "Archives"
}

all_files = os.listdir(folder_to_sort)
print("Starting Version 2.0 sorting process...")

for file in all_files:
    
    if file.startswith('.') or os.path.isdir(f"{folder_to_sort}/{file}"):
        continue
    
    file_name, file_extension = os.path.splitext(file)
    
    
    file_extension = file_extension.lower()

   
    if file_extension in extensions_map:
       
        folder_name = extensions_map[file_extension]
        
        destination_folder = f"{folder_to_sort}/{folder_name}"
        os.makedirs(destination_folder, exist_ok=True)
        
       
        current_location = f"{folder_to_sort}/{file}"
        print(f" --> Moving {file} to {folder_name} folder")
        shutil.move(current_location, destination_folder)
    else:
        
        print(f" [!] Skipping {file} - unknown extension.")

print("Version 2.0 Sorting complete!")
