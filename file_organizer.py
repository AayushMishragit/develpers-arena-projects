import os
import shutil

print("=====================================================")
print("FILE ORGANIZER TOOL")

def organize_folder(folder_path):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Audio': ['.mp3', '.wav'],
        'Archives': ['.zip', '.rar'],
        'Scripts': ['.py', '.js']
    }

    moved_files = []
    for file_name in os.listdir(folder_path):
        src_path = os.path.join(folder_path, file_name)
        if not os.path.isfile(src_path):
            continue
        _, ext = os.path.splitext(file_name)
        ext = ext.lower()
        for folder, extensions in file_types.items():
            if ext in extensions:
                target_folder = os.path.join(folder_path, folder)
                os.makedirs(target_folder, exist_ok=True)
                dest_path = os.path.join(target_folder, file_name)
                try:
                    shutil.move(src_path, dest_path)
                    moved_files.append(dest_path)
                except Exception as e:
                    print(f"Failed to move {file_name}: {e}")
                break



    return moved_files



files = organize_folder(r" C:\Users\DELL\Documents\developers arena\Productivity suite")
print(files)
