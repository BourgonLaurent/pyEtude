## document_alert.py - pyEtude.document
# Alert dialog to open a document
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
from .. import __version__

# Default packages
import os, sys

# External packages
from PySide2.QtWidgets import QMessageBox, QWidget


class DocumentAlert(QMessageBox):
    """
    Custom QMessageBox to open a file

    Parameters
    ----------
    filepath : str
        Path to file to open
    
    window : QWidget
        Widget that will have the QMessageBox
    
    Methods
    ----------
    exec_ : () -> ()
        Show the alert
    
    openFile: () -> ()
        Open the file set, according to the current OS
    """

    def __init__(self, filepath: str, window: QWidget) -> None:
        super().__init__(window)

        self.filepath = filepath

        self.setIcon(QMessageBox.Information)  # type: ignore
        self.setWindowTitle(f"pyÉtude - {__version__} - Document généré")

        self.setText(f"Le document a été créé:\n{filepath}\n\nVoulez-vous l'ouvrir?")

        self.buttonOpen = self.addButton(QMessageBox.Open)  # type: ignore
        self.buttonOpen.setText("Ouvrir le fichier")

        self.buttonIgnore = self.addButton(QMessageBox.No)  # type: ignore
        self.buttonIgnore.setText("Non")

    def exec_(self):
        """Show the alert"""
        super().exec_()

        if self.clickedButton() == self.buttonOpen:
            self.openFile()
        else:
            assert ConnectionRefusedError

    def openFile(self):
        """Open the file set depending on the OS"""
        if sys.platform.startswith("win"):
            try:
                os.startfile(self.filepath)  # type: ignore
            except:
                pass
        else:
            os.system(f'open "{self.filepath}"')
