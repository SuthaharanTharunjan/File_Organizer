from pathlib import Path
import shutil

from pathlib import Path

# Documents & Text
DOCUMENTS = (".pdf", ".docx", ".doc", ".txt", ".rtf", ".odt", ".md", ".tex")

# Images
IMAGES = (
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    ".bmp",
    ".tiff",
    ".tif",
    ".svg",
    ".ico",
    ".heic",
)

# Audio
AUDIO = (".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma", ".alac")

# Video
VIDEO = (".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv", ".webm", ".m4v")

# Tabular & Structured Data
DATA = (".csv", ".tsv", ".json", ".xml", ".yaml", ".yml", ".parquet")

# Spreadsheets (No .csv to avoid overlap with DATA)
SPREADSHEETS = (".xlsx", ".xls", ".xlsm", ".ods", ".numbers")

# Archives & Compressed Files
ARCHIVES = (".zip", ".tar.gz", ".tgz", ".tar", ".gz", ".rar", ".7z", ".bz2", ".xz")

# Code & Scripts (Contains .sql)
CODE = (
    ".py",
    ".js",
    ".ts",
    ".html",
    ".css",
    ".java",
    ".c",
    ".cpp",
    ".rs",
    ".go",
    ".sh",
    ".sql",
    ".php",
    ".rb",
    ".swift",
    ".kt",
)

# Executables & Binaries
EXECUTABLES = (
    ".exe",
    ".msi",
    ".bin",
    ".app",
    ".bat",
    ".cmd",
    ".apk",
    ".deb",
    ".rpm",
    ".jar",
    ".appimage",
)

# System Files & Libraries (NEW)
SYSTEM_FILES = (".sys", ".dll", ".so", ".drv", ".efi", ".kext")

# 3D Models & CAD / 3D Printing
MODELS_3D = (
    ".stl",
    ".obj",
    ".fbx",
    ".step",
    ".stp",
    ".iges",
    ".igs",
    ".blend",
    ".dae",
    ".3ds",
    ".gltf",
    ".glb",
)

# Presentations / Slides (Contains .key)
PRESENTATIONS = (".pptx", ".ppt", ".key", ".odp", ".ppsx")

# Fonts
FONTS = (".ttf", ".otf", ".woff", ".woff2", ".eot")

# Disk Images & Virtual Machines
DISK_IMAGES = (".iso", ".dmg", ".img", ".vmdk", ".vdi", ".qcow2", ".vhd")

# eBooks
EBOOKS = (".epub", ".mobi", ".azw", ".azw3", ".cbz", ".cbr")

# Databases & Backups (Removed .sql to prevent Code overlap)
DATABASES = (".db", ".sqlite", ".sqlite3", ".mdb", ".accdb", ".bak", ".dump")

# Logs & System Configs
LOGS_AND_CONFIGS = (".log", ".cfg", ".ini", ".conf", ".env", ".properties", ".toml")

# Vector & Design Assets
DESIGN = (".psd", ".ai", ".xd", ".fig", ".sketch", ".eps", ".cdr")

# Certificates & Keys (NEW - Note: .key is kept in Presentations to avoid overlap)
CERTIFICATES = (".crt", ".pem", ".cer", ".pfx", ".p12", ".pub")

# Shortcuts & Links (NEW)
SHORTCUTS = (".lnk", ".url", ".desktop", ".webloc")


# Torrents & Metadata
TORRENTS = (".torrent", ".magnet")

CATEGORY_MAP = {
    "Documents & Text": DOCUMENTS,
    "Images": IMAGES,
    "Audio": AUDIO,
    "Video": VIDEO,
    "Tabular & Structured Data": DATA,
    "Spreadsheets": SPREADSHEETS,
    "Archives & Compressed Files": ARCHIVES,
    "Code & Scripts": CODE,
    "Executables & Binaries": EXECUTABLES,
    "System Files & Libraries": SYSTEM_FILES,
    "3D Models & CAD": MODELS_3D,
    "Presentations": PRESENTATIONS,
    "Fonts": FONTS,
    "Disk Images": DISK_IMAGES,
    "eBooks": EBOOKS,
    "Databases": DATABASES,
    "Logs & Configs": LOGS_AND_CONFIGS,
    "Vector & Design Assets": DESIGN,
    "Certificates & Keys": CERTIFICATES,
    "Shortcuts": SHORTCUTS,
    "Torrents": TORRENTS,
}

GREEN = "\033[92m"
RESET = "\033[0m"


def source_location_getter():
    while True:
        source_location = Path(input("Enter the destination folder : ").strip())
        if source_location.exists() and source_location.is_dir():
            return source_location
        else:
            print("FOLDER doesn't exists...")


def main():
    source_location = source_location_getter()

    for file in source_location.iterdir():
        if not file.is_file():
            continue

        file_ext = file.suffix.lower()

        for folder_name, extensions in CATEGORY_MAP.items():

            if file_ext in extensions:
                target_folder = source_location / folder_name
                target_folder.mkdir(exist_ok=True)
                shutil.move(file, target_folder)
                break

    print(f"{GREEN}Finished{RESET}")


if __name__ == "__main__":
    main()
