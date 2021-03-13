## downloader.py - damysos.helpers
# Check updates on GitHub
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
# Project packages
from damysos import __version__, GITHUB_REPO
from damysos.ui.dialogs import UpdateMessageBox

# Default packages
from json import loads
from urllib.request import urlopen
from urllib.parse import quote
from urllib.error import HTTPError, URLError


def check_new_version():
    """Vérifie si une nouvelle version existe

    Returns:
        {str}: Dernière version stable sur GitHub
    """
    try:
        with urlopen(
            quote(
                fr"https://api.github.com/repos/{GITHUB_REPO}/releases/latest",
                safe="/:?=&",
            )
        ) as ur:
            return loads(ur.read().decode("utf-8"))["tag_name"]
    except (HTTPError, URLError):
        return __version__


def check_updates(window):
    """Vérifie les nouvelles versions du logiciel et affiche une boîte de dialogue

    Arguments:\n
      * window {PySide2.QtWidgets.QWidget} -- Instance QWidget auquel la boîte de dialogue s'attachera
    """
    version = check_new_version()

    if version > f"v{__version__}":
        update_msgbox = UpdateMessageBox(parent=window, online_version=version)
        update_msgbox.exec_()
