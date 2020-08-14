## Document.py - damysos.document
# Document exporter
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
from . import __version__

# Default packages
import os, sys
from typing import Dict

# External packages
from docxtpl import DocxTemplate
from PySide2.QtWidgets import QMessageBox, QWidget


class Document:
    """
    Create a word document with specific values

    Parameters
    ----------
    values : Dict[str, str]
        Dictionnary containing the values to replace {"placeholder": "replaced"}
    
    model : str
        Path to the document model
    
    filepath : str
        Path to the export destination
    
    Methods
    ----------
    packWord : () -> ()
        Export the Word Document
    """

    def __init__(self, values: Dict[str, str], model: str, filepath: str):
        self.values = values
        self.model = model
        self.filepath = filepath

        self.document = DocxTemplate(self.model)

    def packWord(self):
        """Export the Word Document with the values given earlier"""
        self.document.render(self.values)
        self.document.save(self.filepath)


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
        self.setWindowTitle(f"Damysos - {__version__} - Document généré")

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
