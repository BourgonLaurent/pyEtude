## app.py - damysos
# Main Application of damysos
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
from .ui.window import DamysosMainWindow

# Default packages
from typing import cast

# Externals packages
from PySide2.QtCore import QFile, QIODevice, QTextStream
from PySide2.QtWidgets import QApplication


class DamysosApp(QApplication):
    def __init__(self) -> None:
        super().__init__([])
        # Set the global theme
        self.setStyle("Fusion")

        # Load the stylesheet inside resources
        _stylesheet = QFile(self)
        _stylesheet.setFileName(":/styles/designer_styles.qss")
        _stylesheet.open(cast(QIODevice.OpenMode, QIODevice.OpenModeFlag.ReadOnly))
        self.setStyleSheet(QTextStream(_stylesheet).readAll())
        _stylesheet.close()

        # Create the mainwindow
        self.window = DamysosMainWindow()

    def exec_(self) -> int:
        self.window.show()
        return super().exec_()
