from pathlib import Path
import shutil

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
RED = "\033[91m"

NAME = r"""
  ___ _ _          ___                     _            
 | __(_) |___ ___ / _ \ _ _ __ _ __ _ _ _ (_)______ _ _ 
 | _|| | / -_)___| (_) | '_/ _` / _` | ' \| |_ / -_) '_|
 |_| |_|_\___|    \___/|_| \__, \__,_|_||_|_/__\___|_|  
                           |___/                        
"""


def source_location_getter():
    while True:
        source_location = (
            Path(input("Enter source folder : ").strip().strip("'\""))
            .expanduser()
            .resolve()
        )
        if source_location.exists() and source_location.is_dir():
            return source_location
        else:
            print(f"{RED}FOLDER doesn't exist...{RESET}")


def main():
    print(NAME)
    source_location = source_location_getter()
    print(
        f"{RED}Warning : Files will be moved to categorized folders permanently{RESET}"
    )

    confirmation = input("Do you really want to continue (yes/no) : ").strip().lower()

    if confirmation in ["y", "yes"]:
        count = 0
        skipped = 0
        unmatched = 0

        current_script = Path(__file__).resolve()

        files = [
            f
            for f in source_location.iterdir()
            if f.is_file() and not f.name.startswith(".")
        ]
        for file in files:
            if file.resolve() == current_script:
                continue

            filename = file.name
            filename_m = filename.lower()
            matched = False

            for folder_name, extensions in CATEGORY_MAP.items():
                if filename_m.endswith(extensions):
                    target_folder = source_location / folder_name
                    target_file = target_folder / filename
                    matched = True

                    try:
                        target_folder.mkdir(exist_ok=True)
                        if not target_file.exists():
                            shutil.move(file, target_folder)
                            count += 1
                            print(f"{GREEN}.{RESET}", end="", flush=True)
                        else:
                            skipped += 1
                            print(f"{RED}.{RESET}", end="", flush=True)
                    except (PermissionError, OSError) as e:
                        print(f"\n{RED}Error moving '{filename}': {e}{RESET}")
                        skipped += 1
                    break

            if not matched:
                unmatched += 1
                print(".", end="", flush=True)

        print()
        print(f"✨ Files moved : {count}")
        if skipped > 0:
            print(f"⚠️ Files skipped : {skipped}")
        if unmatched > 0:
            print(f"ℹ️ Unmatched files: {unmatched} (left in place)")
        print(f"{GREEN}Finished Successfully.{RESET}")
    else:
        print(f"{RED}Cancelling and exiting the programme...{RESET}")


if __name__ == "__main__":
    main()
