## version_label.py - damysos.ui.widgets
# Label that shows the current version (damysos.__version__)
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
from damysos import __version__, GITHUB_REPO
from damysos.helpers.updater import check_new_version

# External packages
from PySide2.QtWidgets import QWidget, QLabel


class VersionLabel(QLabel):
    """QLabel saying the latest version available on damysos.GITHUB_REPO"""

    def __init__(self, parent: QWidget):
        """
        Creates the QLabel and sets its text

        Parameters
        ----------
        parent : QWidget
            Any Widget that will be parent of the QLabel
        """
        new_version = check_new_version()

        super().__init__(
            text="<html><head/><body>"
            + '<p><span style="font-size:12pt;">'
            + (
                f'<a href="https://github.com/{GITHUB_REPO}/releases">'
                + f"Une nouvelle version de Damysos ({new_version}) est disponible sur GitHub."
                + "</a>"
                if new_version > f"v{__version__}"
                else "Vous avez la version la plus récente de Damysos."
            )
            + "</span></p>"
            + "</body></html>",
            parent=parent,
        )
