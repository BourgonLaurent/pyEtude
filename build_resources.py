# create_dependencies.py: Compile the UI files
#
# MIT (c) 2021 Laurent Bourgon
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
import sys
import os
from subprocess import CompletedProcess, run
from typing import Dict, List

# Access files through the root of this file, not the root of the shell
os.chdir(os.path.dirname(__file__))

# Get python environment executable
# PYTHON_PATH = sys.argv[-1].replace("/python", "", 1)
# print(environ)

if len(sys.argv) > 1:
    PYTHON_PATH = sys.argv[-1].replace("/python", "", 1)
else:
    PYTHON_PATH = os.path.join(os.environ.get("VIRTUAL_ENV", ""), "bin")

# MODIFY THIS TO CHANGE COMPILING
BASE_FOLDER: str = os.path.join("./", "damysos", "ui", "designer")
FILES: List[str] = ["designer"]

# Create an empty Dict that will hold the success codes
SUCCESS: Dict[str, Dict[str, CompletedProcess]] = {"qrc": {}, "ui": {}}


def main():
    # Loop through the files to compile
    for f in FILES:
        # Resources files
        qrc = os.path.join(BASE_FOLDER, f"{f}_resources.qrc")  # Get the .qrc file
        qrc_py = os.path.join(BASE_FOLDER, f"{f}_resources_rc.py")  # File to create
        if os.path.exists(qrc):  # Check if a .qrc file needs to be compiled
            SUCCESS["qrc"][f] = run(
                [
                    f"{PYTHON_PATH}/PySide6-rcc",
                    qrc,
                    "-o",
                    qrc_py,
                ]
            )  # Run the compile command

        # UI files
        ui = os.path.join(BASE_FOLDER, f"{f}_ui.ui")  # Get the .ui file
        ui_py = os.path.join(BASE_FOLDER, f"{f}_ui.py")  # File to create
        if os.path.exists(ui):  # Check if a .ui file needs to be compiled
            SUCCESS["ui"][f] = run(
                [
                    f"{PYTHON_PATH}/PySide6-uic",
                    ui,
                    "--from-imports",
                    "-o",
                    ui_py,
                ],
            )  # Run the compile command

    # Print success
    for tool, success_dict in SUCCESS.items():
        print(f"[+] {tool}:")  # Print the file type
        for f, cmd in success_dict.items():  # Loop throught the files compiled
            if not cmd.returncode:  # Only if there's no error code
                print(f"\t[+] {cmd.args[-1]}")  # Print the file created


if __name__ == "__main__":
    main()