"""
📄 Project 1: File Automation Tool
👨‍💻 Created by: Hashir Adnan
🌐 Website: www.techthf.xyz
🗓️ Date: [Insert today's date]

🧠 Description:
This Python script automates the organization of files within a folder by sorting them based on their file type (e.g., moving .txt files to a dedicated folder).
It's a practical tool for anyone who wants to streamline their file management.

📦 Features:
- Scans a folder for files
- Automatically moves files to corresponding subfolders based on their extensions
- Creates destination folders if they don't exist
- Supports customization for different file extensions

🧰 Tools & Modules Used:
- os: for interacting with the operating system (e.g., listing files, creating directories)
- shutil: for moving files between directories

💡 How to Use:
1. Place your files in the target folder.
2. Set the `source_dir` and `dest_dir` variables in the script to your source and destination folders.
3. Run the script.
4. The script will organize the files by moving them to corresponding subfolders.

✅ Example:
Input Files: file1.txt, file2.txt  
Output Folders: .txt files moved to "OrganizedFiles"
"""

import os
import shutil

def organize_files():
    source_dir = r'C:\Users\ads\Desktop\py\proj 6\MyFiles'
  # Replace with your actual path
    dest_dir = r'C:\Users\ads\Documents\OrganizedFiles'  # Destination folder
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    if not os.path.exists(source_dir):
        print(f"Source directory not found: {source_dir}")
        return

    for filename in os.listdir(source_dir):
        if filename.endswith('.png'):  # Example: moving .txt files
            shutil.move(os.path.join(source_dir, filename), os.path.join(dest_dir, filename))
    print("Files organized!")

organize_files()
