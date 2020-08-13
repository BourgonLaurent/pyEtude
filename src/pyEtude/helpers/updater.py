## downloader.py - pyEtude.helpers
# Check updates on GitHub
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
# Project packages
from .. import __version__, GITHUB_REPO

# Default packages
from json import loads
from urllib.request import urlopen
from urllib.parse import quote

# External packages
from PySide2.QtWidgets import QMessageBox
from PySide2.QtGui import QIcon


def checkNewVersion():
    """Vérifie si une nouvelle version existe

    Returns:
        {str}: Dernière version stable sur GitHub
    """
    with urlopen(
        quote(
            fr"https://api.github.com/repos/{GITHUB_REPO}/releases/latest",
            safe="/:?=&",
        )
    ) as ur:
        return loads(ur.read().decode("utf-8"))["tag_name"]


def checkUpdates(window):
    """Vérifie les nouvelles versions du logiciel et affiche une boîte de dialogue
    
    Arguments:\n
      * window {PySide2.QtWidgets.QWidget} -- Instance QWidget auquel la boîte de dialogue s'attachera
    """
    current_version = checkNewVersion()

    if current_version > f"v{__version__}":
        alert = QMessageBox(window)
        alert.setIcon(QMessageBox.Warning)  # type: ignore

        alert.setWindowTitle(f"pyÉtude - v{__version__} - Nouvelle version")

        alert.setText(f"Une version plus récente de pyÉtude a été trouvée.")
        alert.setInformativeText(
            f"<p>Version actuelle: v{__version__}<br>Version la plus récente: {current_version}</p>"
            + "<br><br>"
            + f"<a style='color: white;' href='https://github.com/{GITHUB_REPO}/releases'>Téléchargez-la sur GitHub</a>"
        )

        alert.exec_()
