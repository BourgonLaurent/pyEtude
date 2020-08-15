## calendar_dialog.py - damysos.ui.dialogs
# Dialog showing a calendar
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
from PySide2.QtGui import QBrush, QTextCharFormat
from damysos.helpers.utilities import SAFE_CHARACTERS_QREGEXP

# Default packages
from typing import cast

# External packages
from PySide2.QtCore import QDate, Qt, QRect, Slot
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QWidget, QDialog, QCalendarWidget


class CalendarDialog(QDialog):
    """
    QDialog that presents a calendar

    Attributes
    ----------
    date : str
        Date selected, formatted in MMdd 
    """

    date: str

    def __init__(self, parent: QWidget):
        """
        Creates the Dialog and its widgets

        Parameters
        ----------
        parent : QWidget
            QWidget that will be attached to this dialog
        """

        super().__init__(parent=parent)

        self.setWindowTitle("Veuillez choisir une date")
        self.setWindowFlags(
            cast(
                Qt.WindowFlags,
                cast(int, Qt.Dialog)
                | cast(int, Qt.MSWindowsFixedSizeDialogHint)
                | cast(int, Qt.WindowMinimizeButtonHint),
            )
        )

        self.calendar = CustomCalendar(self)
        self.calendar.clicked.connect(self.QDateToString)  # type: ignore

    @Slot(QDate)  # type: ignore
    def QDateToString(self, qdate: QDate):
        self.date = qdate.toString("MMdd", self.calendar.calendar())
        self.done(0)


class CustomCalendar(QCalendarWidget):
    def __init__(self, parent: QDialog) -> None:
        super().__init__(parent=parent)

        self.setGeometry(0, 0, 312, 183)
        self.setGridVisible(True)

        self.setFirstDayOfWeek(Qt.DayOfWeek.Monday)
        self.setVerticalHeaderFormat(
            QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader
        )

        self.week_end_text_format = QTextCharFormat()  # type: ignore
        self.week_end_text_format.setForeground(QColor("#148CD2"))  # type: ignore

        self.setWeekdayTextFormat(Qt.DayOfWeek.Saturday, self.week_end_text_format)
        self.setWeekdayTextFormat(Qt.DayOfWeek.Sunday, self.week_end_text_format)
