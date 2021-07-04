## __init__.py - damysos
# Set global variables and make global checks
# Ensures that everything will work correctly after
# Run this file as "__main__" to launch Damysos
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

## Imports
# Required to import separately
import sys

# Check if everything is installed correctly
# Shows an error to the user if not
try:
    # Standard library to check
    import os, importlib, json, locale, typing

    # Used in __init__
    from typing import Dict
    from importlib.metadata import metadata

    # External libraries
    import PySide2, docxtpl

except ImportError as e:
    # Show error message
    print(
        f"damysos\n\n"
        + "[!] Impossible de continuer:\n\n"
        + f"\t{repr(e)}"
        + "\n\n"
        + f"[*] Avez-vous installé {e.name}?\n"
        + "C'est un module nécessaire au fonctionnement de Damysos.\n\n"
        + "Essayez la commande suivante:"
        + f"\tpip install --update {e.name}\n\n"
        + "Pour plus d'aide référez-vous au README.md sur GitHub:\n"
    )
    # Exit and tell error
    sys.exit(e)

## Locale
# Try to get into an UTF-8 locale
# if it isn't currently
try:
    if not locale.getlocale()[1].lower() == "utf-8":
        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
except:
    assert EnvironmentError

## Get Project Variables
_metadata = metadata(__package__)

__version__: str = _metadata.get("Version", failobj="0.0.0")

GITHUB_REPO: str = _metadata.get("Project-URL", failobj="").replace(
    "Repository, https://github.com/", ""
)

CONFIG_FILE: str = "damysos.config"  # (format: JSON) généré avec le configurateur
