## __main__.py - damysos
# Launch Damysos (`python3 -m damysos`)
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

from . import __version__, GITHUB_REPO

try:
    ## Imports
    # Project packages
    from .app import DamysosApp

    # Default packages
    import os

    # Move to `Damysos` folder, where the config is
    os.chdir(os.path.dirname(os.path.dirname(__file__)))

    if __name__ == "__main__":
        DamysosApp().exec()

except ImportError as import_error:
    # Show error message
    print(
        "[!] ERREUR: Impossible de continuer:\n\n"
        + f"\tMessage: {repr(import_error)}\n\n"
        + f"\tAvez-vous installé {import_error.name}?\n"
        + f"\tC'est un module nécessaire au fonctionnement de {__package__}.\n\n"
        + "\t[*] Essayez la commande suivante:\n"
        + f"\t\tpython -m pip install --update {import_error.name}\n\n"
        + "\tPour plus d'aide référez-vous au README.md sur GitHub:\n"
        + f"\t\thttps://github.com/{GITHUB_REPO}\n"
    )

    # Re-throw error
    raise import_error
