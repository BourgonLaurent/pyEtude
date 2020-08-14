# create_dependencies.py: Compile the UI files
#
# MIT (c) 2020 Laurent Bourgon
#    Permission is hereby granted, free of charge, to any person obtaining a copy
#    of this software and associated documentation files (the "Software"), to deal
#    in the Software without restriction, including without limitation the rights
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#    copies of the Software, and to permit persons to whom the Software is
#    furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be included in all
#    copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#    SOFTWARE.


## Librairies
# Default packages
from os import chdir, path
from subprocess import CompletedProcess, run
from typing import Dict, List, Text

# Access files through the root of this file, not the root of the shell
chdir(path.realpath(__file__).replace(path.basename(__file__), ""))

# MODIFY THIS TO CHANGE COMPILING
BASE_FOLDER: Text = path.join("./", "src", "damysos", "ui")
FILES: List[str] = ["main"]

# Create an empty Dict that will hold the success codes
SUCCESS: Dict[str, Dict[str, CompletedProcess]] = {"qrc": {}, "ui": {}}

# Loop through the files to compile
for f in FILES:
    # Resources files
    qrc: Text = path.join(
        BASE_FOLDER, f"damysos_{f}_resources.qrc"
    )  # Get the .qrc file
    qrc_py: Text = path.join(
        BASE_FOLDER, f"damysos_{f}_resources_rc.py"
    )  # File to create
    if path.exists(qrc):  # Check if a .qrc file needs to be compiled
        SUCCESS["qrc"][f] = run(
            ["pyside2-rcc", qrc, "-o", qrc_py,]
        )  # Run the compile command

    # UI files
    ui: Text = path.join(BASE_FOLDER, f"damysos_{f}_ui.ui")  # Get the .ui file
    ui_py: Text = path.join(BASE_FOLDER, f"damysos_{f}_ui.py")  # File to create
    if path.exists(ui):  # Check if a .ui file needs to be compiled
        SUCCESS["ui"][f] = run(
            ["pyside2-uic", ui, "--from-imports", "-o", ui_py,]
        )  # Run the compile command

# Print success
for tool, success_dict in SUCCESS.items():
    print(f"[+] {tool}:")  # Print the file type
    for f, cmd in success_dict.items():  # Loop throught the files compiled
        if not cmd.returncode:  # Only if there's no error code
            print(f"\t[+] {cmd.args[-1]}")  # Print the file created
