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

## IMPORTS
from importlib.metadata import metadata, PackageNotFoundError
import locale

## VARIABLES
# Get Project Variables

try:
    _metadata = metadata(__package__)

    __version__: str = _metadata.get("Version", failobj="0.0.0")

    GITHUB_REPO: str = _metadata.get("Project-URL", failobj="").replace(
        "Repository, https://github.com/", ""
    )
except PackageNotFoundError as package_error:
    print(
        "\n[?] Impossible d'accéder aux métadonnées\n\n"
        + f"\t{package_error.msg} doit être installé pour l'utilisation des métadonnées\n\n"
        + "\t[*] Essayez la commande suivante: poetry install\n"
    )
    __version__ = "0.0.0"
    GITHUB_REPO = ""

# Set Project Variables
CONFIG_FILE: str = (
    f"{__package__}.config"  # (format: JSON) généré avec le configurateur
)


## Locale
# Try to get into an UTF-8 locale
# if it isn't currently
try:
    # Get the locale of the system
    default_locale = locale.getdefaultlocale()[1]

    if default_locale and default_locale.lower() == "utf-8":
        # Bug fix: some versions of python (like on macOS)
        #   don't apply UTF-8 sorting
        #   even if the current locale is UTF-8,
        #   it needs to be set or reset manually
        locale.resetlocale(locale.LC_ALL)
    else:
        # en_US.UTF-8 is a common locale
        # that should be installed on all devices
        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
except locale.Error as locale_error:
    print(
        "\n[?] Impossible d'utiliser une langue UTF-8\n\n"
        + f"\tMessage: {locale_error}\n"
        + f"\t{__package__} a besoin d'une langue UTF-8 disponible pour que les tris fonctionnent correctement\n\n"
    )
