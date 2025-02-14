import os
import shutil

# Function to organize files based on their extensions
def organize_files(source_folder):
    # Define file extensions and corresponding folder names
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".pptx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Audio": [".mp3", ".wav", ".flac"],
        "Archives": [".zip", ".tar", ".rar"],
        "Other": []  # Any file type that doesn't match the above categories
    }

    # Check if the source folder exists
    if not os.path.exists(source_folder):
        print(f"Error: The folder '{source_folder}' does not exist.")
        return
    
    # Loop through each file in the source folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Identify the file extension
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False
        
        # Check file types and move files accordingly
        for folder_name, extensions in file_types.items():
            if file_extension in extensions:
                # Create the subfolder if it doesn't exist
                folder_path = os.path.join(source_folder, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                
                # Move the file to the appropriate subfolder
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved: {filename} -> {folder_name}")
                moved = True
                break
        
        # If no matching folder, move it to 'Other'
        if not moved:
            folder_path = new_func(source_folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            shutil.move(file_path, os.path.join(folder_path, filename))
            print(f"Moved: {filename} -> Other")
    
    print("File organization completed!")

def new_func(source_folder):
    return os.path.join(source_folder, "Other")

# Example usage: Organize files in a given folder
source_folder = input("Enter the path of the folder to organize: ")
organize_files(source_folder)