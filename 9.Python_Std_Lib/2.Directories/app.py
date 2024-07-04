# Run this code from the Directories folder

from pathlib import Path

path = Path("ecommerce")

# path.exists() -> Method to check if the directory exists
# path.mkdir() -> Method to create a directory
# path.rmdir() -> Method to remove a directory
# path.rename("ecommerce2") -> Method to rename a directory

paths = [p for p in path.iterdir() if p.is_dir()]

py_files_in_current_directory = [
    p for p in path.glob("*.py")]  # Non-recursive glob
py_files = [p for p in path.rglob("*.py")]  # Recursive glob
print(paths)

print("--------------------")

print(py_files)

print("--------------------")

print(py_files_in_current_directory)
# PoxisPath is a subclass of Path (Linux, Mac)
# WindowsPath is a subclass of Path (Windows only)
