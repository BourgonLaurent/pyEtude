## labels.py - damysos.ui.widgets
# Various modified Labels
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
from damysos.helpers.utilities import execute_file

# Default packages
import os
from typing import cast

# External packages
from PySide2.QtCore import QPoint, Signal, SignalInstance, Slot
from PySide2.QtGui import QMouseEvent
from PySide2.QtWidgets import QAction, QActionGroup, QFileDialog, QLabel, QMenu, QWidget


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


class ClickableLabel(QLabel):
    clicked = cast(SignalInstance, Signal())

    def __init__(self, parent: QWidget) -> None:
        super().__init__(text="", parent=parent)

    def mousePressEvent(self, event: QMouseEvent):
        self.clicked.emit()


class PathMenuLabel(ClickableLabel):
    directory: str = ""
    filepath: str = ""

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)

        self.menu = QMenu("pathMenu", parent)
        self.action_group = QActionGroup(self.menu)

        self.action_open_folder = self.add_action("Ouvrir le dossier sélectionné")
        self.menu.addSeparator()
        self.action_choose_folder = self.add_action("Choisir le dossier de sortie")
        self.action_choose_file = self.add_action("Enregister sous...")
        self.menu.addSeparator()
        self.action_restore_default = self.add_action("Restaurer la valeur par défaut")

        self.clicked.connect(
            lambda: self.menu.exec_(
                self.mapToGlobal(QPoint(0, self.geometry().height()))
            )
        )

    def add_action(self, text: str) -> QAction:
        action = QAction(text)
        self.menu.addAction(self.action_group.addAction(action))  # type: ignore
        return action

    def set_filepath(self, file_name: str):
        self.filepath = os.path.join(self.directory, file_name)
        _filepath_formatted = self.filepath
        if _filepath_formatted.startswith(os.sep):
            _filepath_formatted = _filepath_formatted.replace(os.sep, "", 1)

        self.setText(_filepath_formatted.replace(os.sep, " > "))
