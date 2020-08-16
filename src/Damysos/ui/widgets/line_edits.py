## line_edit.py - damysos.ui.widgets
# Various modified Line Edits
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
from damysos.helpers.utilities import SAFE_CHARACTERS_QREGEXP

# External packages
from PySide2.QtGui import QRegExpValidator
from PySide2.QtWidgets import QWidget, QLineEdit


class AdvancedLineEdit(QLineEdit):
    def __init__(self, parent: QWidget) -> None:
        """
        Creates the QLineEdit and sets its text

        Parameters
        ----------
        parent : QWidget
            Any Widget that will be parent of the QLineEdit
        """

        super().__init__(parent=parent)

    def getText(self) -> str:
        return self.text() or self.placeholderText()


class SafeAdvancedLineEdit(AdvancedLineEdit):
    """AdvancedLineEdit that prevents using dangerous and breaking characters"""

    def __init__(self, parent: QWidget):
        """
        Creates the QLineEdit and sets its text

        Parameters
        ----------
        parent : QWidget
            Any Widget that will be parent of the QLineEdit
        """

        super().__init__(parent=parent)

        self.setValidator(QRegExpValidator(SAFE_CHARACTERS_QREGEXP, self))
