from cx_Freeze import setup, Executable
import sys
from pathlib import Path

# Đường dẫn settings.json
settings_file = "settings.json"
include_files = [settings_file] if Path(settings_file).exists() else []

# Nếu là GUI, dùng base="Win32GUI"
base = None
if sys.platform.startswith("win"):
    base = "Win32GUI"

executables = [Executable("tenfile.py", base=base)]

setup(
    name="ShopeeAutoPick",
    version="1.0",
    description="Tool tự động chọn ảnh Shopee",
    options={
        "build_exe": {
            "packages": [
                "os", "sys", "time", "glob", "subprocess", "threading", "queue",
                "json", "random", "pathlib", "tkinter", "PIL", "cv2",
                "numpy", "pandas", "openpyxl", "ultralytics", "tensorflow",
                "nsfw_detector"
            ],
            "include_files": include_files,
            "excludes": ["test", "unittest", "email", "html", "http", "xmlrpc"],
        }
    },
    executables=executables
)
