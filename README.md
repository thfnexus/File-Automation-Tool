# 📄 File Automation Tool

**Created by:** Hashir Adnan  
🌐 [www.techthf.xyz](https://www.techthf.xyz)  
🗓️ May 14, 2025

---

## 🧠 Description

A simple yet powerful Python script that automates file organization by sorting files based on their extensions.  
Perfect for users who want to keep their folders clean and structured automatically.

---

## 📦 Features

- 🔍 Scans a folder for files  
- 📁 Automatically moves files to subfolders based on file extensions  
- 🛠️ Creates destination folders if they don’t exist  
- 🧩 Supports customization for different file types

---

## 🧰 Tools & Modules Used

- `os` — Interact with the file system (e.g., check paths, list files)  
- `shutil` — Move files between directories

---

## 💡 How to Use

1. Place all your unorganized files in a folder.
2. Set the `source_dir` and `dest_dir` variables in the script:
   ```python
   source_dir = r'path\to\your\source\folder'
   dest_dir = r'path\to\your\destination\folder'
