# Node Cleanup Automation

A Python script to **automate the cleanup of `node_modules` folders** across multiple projects. It efficiently finds and removes `node_modules` directories, freeing up disk space and making your system cleaner.

## 🚀 Features
- Recursively scans for `node_modules` in all subdirectories
- **Deletes only the top-level** `node_modules` to avoid redundant errors
- **User confirmation** before deletion
- Handles permission errors gracefully
- Cross-platform support (Windows, macOS, Linux)

## 🛠️ Installation
Ensure you have **Python 3.x** installed. Clone this repository and navigate to the project folder:
```sh
git clone https://github.com/krutarthpatel28/node-cleanup-automation.git
cd node-cleanup-automation
```

## ▶️ Usage
Run the script from the terminal:
```sh
python automation.py
```
Enter the absolute path of the folder containing your projects. The script will scan and list `node_modules` folders for deletion.

## 🔥 Example
```sh
Enter the absolute folder path: /Users/yourname/projects
Found 5 'node_modules' folders.
Do you want to remove this directory? Are you sure?
/Users/yourname/projects/app1/node_modules (yes/no): yes
Deleting /Users/yourname/projects/app1/node_modules...
Deletion completed.
```

## 📝 To-Do
- Add a **dry-run mode** to preview deletions before execution
- Implement **parallel execution** for faster processing
- Create a GUI version for ease of use


---
Created by [Krutarth Patel](https://github.com/krutarthpatel28) 🚀

Feel free to modify this code to your convenience
