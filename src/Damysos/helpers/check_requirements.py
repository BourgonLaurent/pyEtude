## check_requirements.py - Damysos.helpers
# Check if everything is installed correctly
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


import sys  # Required to import

try:
    # Standard library
    import os, json, locale, typing

    # External libraries
    import PySide2, docxtpl
except ImportError as e:
    # Affiche le message d'erreur
    print(
        "[!] Impossible de continuer:\n\n"
        + f"\t{repr(e)}"
        + "\n\n"
        + f"[*] Avez-vous installé {e.name}?\n"
        + "C'est un module nécessaire au fonctionnement de Damysos.\n\n"
        + "Essayez la commande suivante:"
        + f"\tpip install --update {e.name}\n\n"
        + "Vous pouvez aussi vous référer au README.md de la page GitHub."
    )
    # Quitte le programme en indiquant l'erreur
    sys.exit(e)
