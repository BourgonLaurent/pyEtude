## __init__.py - Damysos
# Placeholder so that Python see this directory as a module
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
import locale

## Paramètres généraux
# Information de la version actuelle
__version__ = r"4.0.0b5"
# Nom de fichiers importants
CONFIG_FILE = "Damysos.config"  # (format: JSON) généré avec le configurateur
# Assets
GITHUB_REPO = r"BourgonLaurent/Damysos"

# Essaie d'aller dans une langue UTF-8
# si elle ne l'est pas
try:
    if not locale.getlocale()[1].lower() == "utf-8":
        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
except:
    assert EnvironmentError

# Check if everything is installed correctly
# Shows an error to the user if not
from .helpers import check_requirements
