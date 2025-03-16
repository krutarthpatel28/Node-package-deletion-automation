import os
import shutil

def check_folder_exists(path):
    return os.path.exists(path)

def find_top_level_node_modules(root_folder):
    """Finds only the top-level 'node_modules' folders, avoiding redundant deletions."""
    node_modules_paths = []

    for dirpath, dirnames, _ in os.walk(root_folder):
        if "node_modules" in dirnames:
            node_modules_path = os.path.join(dirpath, "node_modules")
            node_modules_paths.append(node_modules_path)
            dirnames.remove("node_modules")  # Prevents os.walk from going deeper into node_modules

    return node_modules_paths

def delete_node_modules(folder_path):
    """Deletes a given 'node_modules' folder with user confirmation."""
    user_input = input(f"Do you want to remove this directory? Are you sure?\n{folder_path} (yes/no): ").strip().lower()
    if user_input == "yes":
        try:
            print(f"Deleting {folder_path}...")
            shutil.rmtree(folder_path)
            print("Deletion completed.")
        except Exception as e:
            print(f"Error deleting {folder_path}: {e}")
    else:
        print("Deletion canceled.")

# Get user input for the root folder
user_folder_path = input("Enter the absolute folder path: ").strip()

if not check_folder_exists(user_folder_path):
    print("Folder not found. Type 'help' for assistance.")
    exit()

# Find only top-level node_modules folders
node_modules_folders = find_top_level_node_modules(user_folder_path)

if not node_modules_folders:
    print("No 'node_modules' folders found.")
else:
    print(f"Found {len(node_modules_folders)} 'node_modules' folders.")
    for folder in node_modules_folders:
        delete_node_modules(folder)
