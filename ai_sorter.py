import os
import shutil
import time 
from google import genai

API_KEY = "YOUR_API_KEY_HERE"

client = genai.Client(api_key=API_KEY)


print("\n--- Welcome to the AI File Sorter ---")
folder_to_sort = input("Please enter the path of the folder you want to sort: ").strip(" '\"")

all_files = os.listdir(folder_to_sort)
print("Waking up the AI Sorter...")

for file in all_files:
    if file.startswith('.') or os.path.isdir(f"{folder_to_sort}/{file}"):
        continue
        
    print(f"\nAsking AI about: {file}...")
    
    prompt = f"I have a file named '{file}'. Based on its name and extension, should it go in 'Images', 'Documents', 'Videos', 'Archives', 'Code', or 'Other'? Reply with ONLY the exact folder name, nothing else."
    
    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash', 
            contents=prompt
        )
        folder_name = response.text.strip() 
        
        print(f" --> AI decided: {folder_name}")
        
        destination_folder = f"{folder_to_sort}/{folder_name}"
        os.makedirs(destination_folder, exist_ok=True)
        
        current_location = f"{folder_to_sort}/{file}"
        shutil.move(current_location, destination_folder)
        
    except Exception as e:
        print(f" --> Oops, hit a snag with {file}. Error: {e}")
        
    time.sleep(4)

print("\nAI Sorting complete! Check your folder.")
