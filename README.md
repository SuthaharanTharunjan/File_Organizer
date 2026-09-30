# 📂 File Organizer

![File Organizer Img](<images/1.png>)

**Instantly declutter your messy directories.** 
File Organizer is a lightweight, robust Python utility that automatically sorts files in any directory into neatly categorized subfolders based on their file extensions.

---

## ✨ Features

- **🚀 Blazing Fast:** Sorts thousands of files in seconds.
- **🛡️ Extremely Safe:** 
  - Prevents accidental self-modification (the script won't move itself).
  - Never overwrites existing files (skips duplicates automatically).
- **👻 Smart Filtering:** Ignores hidden system files (like `.DS_Store` or `.git`) to keep your OS happy.
- **🎨 Visual Feedback:** Real-time, color-coded console output lets you know exactly what's happening.
- **🖱️ Drag-and-Drop Friendly:** Automatically cleans up hidden quotes and tildes (`~`) if you drag a folder directly into your terminal.
- **📦 Zero Dependencies:** Uses only built-in Python libraries (`pathlib`, `shutil`). No `pip install` required!

---

## 🛠️ How It Works

When you run the script, it scans the target folder and checks the extension of every file. It compares these extensions against a massive internal dictionary of **20+ categories**. 

If a match is found, the script creates a designated folder (e.g., `Images`, `Documents & Text`) and safely moves the file there. If a file type is unknown, it is safely left exactly where it is.

### 🟢 Real-time Status Indicators
While sorting, the script prints colored dots to show progress:
* <span style="color:green">**Green Dot (`.`)**</span>: File successfully categorized and moved.
* <span style="color:red">**Red Dot (`.`)**</span>: File skipped (a file with the same name already exists in the target folder).
* **Gray/White Dot (`.`)**: File untouched (extension unmatched).

---

## 🚀 Getting Started

### Prerequisites
All you need is **Python 3.6** or higher installed on your system.

### Usage
1. Download or clone `main.py` to your computer.
2. Open your terminal or command prompt.
3. Run the script:
   ```bash
   python main.py
   ```
   *(Note: Use `python3 main.py` on macOS/Linux if required).*
4. When prompted, enter the path to the messy folder you want to organize. *(Pro tip: You can just drag and drop the folder from your file manager directly into the terminal!)*
5. Type `yes` or `y` to confirm.
6. Watch the magic happen! 🪄

---

## 🗂️ Supported Categories

The script currently recognizes and sorts hundreds of file extensions into the following folders:

| Category | Common Extensions Included |
| :--- | :--- |
| 📄 **Documents & Text** | `.pdf`, `.docx`, `.txt`, `.md`, `.rtf` |
| 🖼️ **Images** | `.jpg`, `.png`, `.svg`, `.gif`, `.heic` |
| 🎵 **Audio** | `.mp3`, `.wav`, `.flac`, `.m4a` |
| 🎥 **Video** | `.mp4`, `.mkv`, `.mov`, `.avi` |
| 📊 **Tabular & Structured Data** | `.csv`, `.json`, `.xml`, `.yaml` |
| 📈 **Spreadsheets** | `.xlsx`, `.ods`, `.numbers` |
| 🗜️ **Archives & Compressed** | `.zip`, `.tar.gz`, `.rar`, `.7z` |
| 💻 **Code & Scripts** | `.py`, `.js`, `.html`, `.cpp`, `.sh` |
| ⚙️ **Executables & Binaries** | `.exe`, `.app`, `.apk`, `.deb` |
| 🧱 **3D Models & CAD** | `.stl`, `.obj`, `.blend`, `.step` |
| 🖥️ **Presentations** | `.pptx`, `.key`, `.odp` |
| 🔤 **Fonts** | `.ttf`, `.otf`, `.woff` |
| 💿 **Disk Images** | `.iso`, `.dmg`, `.vmdk` |
| 📚 **eBooks** | `.epub`, `.mobi`, `.azw3` |
| 🗄️ **Databases & Backups** | `.db`, `.sqlite`, `.bak` |
| 📋 **Logs & Configs** | `.log`, `.ini`, `.env`, `.conf` |
| 🎨 **Vector & Design Assets** | `.psd`, `.ai`, `.fig`, `.sketch` |
| 🔐 **Certificates & Keys** | `.crt`, `.pem`, `.pfx` |
| 🔗 **Shortcuts** | `.lnk`, `.url`, `.desktop` |
| 🧲 **Torrents** | `.torrent`, `.magnet` |

---

## ⚙️ Customization

Want to add a new file type or create a custom folder? It's incredibly easy! 
Open `main.py` in any text editor and locate the extension lists at the top of the file. 

To add a new category, simply create a new tuple and add it to the `CATEGORY_MAP`:

```python
# 1. Create your custom list
MY_CUSTOM_FILES = (".myext", ".custom")

# 2. Add it to the map at the bottom of the lists
CATEGORY_MAP = {
    # ... existing categories ...
    "My Custom Folder": MY_CUSTOM_FILES,
}
```

---

## 📝 License
This project is open-source and free to use, modify, and distribute. Happy organizing! 🎉