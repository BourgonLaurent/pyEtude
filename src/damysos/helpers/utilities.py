## utilities.py - damysos.helpers
# Useful Components
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

## Imports
# Default packages
import os
import sys

# External packages
from PySide2.QtCore import QRegExp

# Allow only safe, path-friendly characters
SAFE_CHARACTERS = r"[^#%&{}j\\<>*?/$!'\":@+`|=]+"
SAFE_CHARACTERS_QREGEXP = QRegExp(SAFE_CHARACTERS)


def execute_file(file_to_open: str):
    if sys.platform.startswith("win"):
        try:
            os.startfile(file_to_open)  # type: ignore
        except:
            pass
    else:
        os.system(f'open "{file_to_open}"')
