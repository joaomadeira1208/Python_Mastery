from pathlib import Path
from time import ctime
import shutil


path = Path("ecommerce/__init__.py")
# path.exists() # check if file exists
# path.rename("init.txt") # rename file
# path.unlink() # delete file


# print(ctime(path.stat().st_ctime))  # get creation time

# path.read_bytes()  # read file as bytes


# print(path.read_text())  # read file as text
# # Line above is better than line below
# # with open("ecommerce/__init__.py") as file:

# path.write_text("...")  # write text to file
# path.write_bytes(b"...")  # write bytes to file

# COPY FILE

source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"

target.write_text(source.read_text())
# same as
shutil.copy(source, target)
