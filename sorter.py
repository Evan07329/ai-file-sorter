import os
import shutil

# Your test folder path
folder_to_sort = "/Users/eti/Desktop/Test_Downloads" 

# 1. THE UPGRADE: A Dictionary mapping extensions to their folder names
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
    # Ignore hidden Mac files (like .DS_Store) and folders
    if file.startswith('.') or os.path.isdir(f"{folder_to_sort}/{file}"):
        continue
        
    # 2. THE TRICK: This splits "document.pdf" into "document" and ".pdf"
    file_name, file_extension = os.path.splitext(file)
    
    # Make the extension lowercase just in case (e.g., .JPG becomes .jpg)
    file_extension = file_extension.lower()

    # 3. THE LOGIC: Check if the extension is in our dictionary map
    if file_extension in extensions_map:
        # Get the correct folder name from the map
        folder_name = extensions_map[file_extension]
        
        # Build the path and create the folder if it doesn't exist
        destination_folder = f"{folder_to_sort}/{folder_name}"
        os.makedirs(destination_folder, exist_ok=True)
        
        # Move the file
        current_location = f"{folder_to_sort}/{file}"
        print(f" --> Moving {file} to {folder_name} folder")
        shutil.move(current_location, destination_folder)
    else:
        # What happens if we don't know the file type?
        print(f" [!] Skipping {file} - unknown extension.")

print("Version 2.0 Sorting complete!")