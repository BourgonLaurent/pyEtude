# create_dependencies.py: Compile the UI files
#
# GPLv3 (c) 2020 Laurent Bourgon
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.


# Librairies
from os import chdir, path
from subprocess import CompletedProcess, run
from typing import Dict, List, Text

# Access files through the root of this file, not the root of the shell
chdir(path.realpath(__file__).replace(path.basename(__file__), ""))

# MODIFY THIS TO CHANGE COMPILING
BASE_FOLDER: Text = path.join("./", "src", "pyEtude", "ui")
FILES: List[str] = ["main"]

# Create an empty Dict that will hold the success codes
SUCCESS: Dict[str, Dict[str, CompletedProcess]] = {"qrc": {}, "ui": {}}

# Loop through the files to compile
for f in FILES:
    # Resources files
    qrc: Text = path.join(BASE_FOLDER, f"pyEt_{f}_resources.qrc")  # Get the .qrc file
    qrc_py: Text = path.join(BASE_FOLDER, f"pyEt_{f}_resources_rc.py")  # File to create
    if path.exists(qrc):  # Check if a .qrc file needs to be compiled
        SUCCESS["qrc"][f] = run(
            ["pyside2-rcc", qrc, "-o", qrc_py,]
        )  # Run the compile command

    # UI files
    ui: Text = path.join(BASE_FOLDER, f"pyEt_{f}_ui.ui")  # Get the .ui file
    ui_py: Text = path.join(BASE_FOLDER, f"pyEt_{f}_ui.py")  # File to create
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
