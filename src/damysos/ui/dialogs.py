## dialogs.py - damysos.ui
# Different kind of dialogs
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

# Default packages
from typing import cast
import os, sys

# External packages
from PySide2.QtCore import QDate, QFile, Qt, Signal, SignalInstance, Slot
from PySide2.QtGui import QColor, QTextCharFormat
from PySide2.QtWidgets import (
    QFileDialog,
    QMessageBox,
    QWidget,
    QDialog,
    QCalendarWidget,
)


class UpdateMessageBox(QMessageBox):
    def __init__(self, parent: QWidget, online_version: str) -> None:
        super().__init__(parent=parent)

        self.setIcon(QMessageBox.Icon.Warning)
        self.setWindowTitle(f"Damysos - v{__version__} - Nouvelle version")

        self.setText(f"Une version plus récente de Damysos a été trouvée.")
        self.setInformativeText(
            f"<p>Version actuelle: v{__version__}<br>Version la plus récente: {online_version}</p>"
            + "<br><br>"
            + f"<a href='https://github.com/{GITHUB_REPO}/releases'>Téléchargez-la sur GitHub</a>"
        )


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

        self.calendar = CalendarDialog.CustomCalendar(parent=self)
        self.calendar.clicked.connect(self.QDateToString)

    @Slot(QDate)  # type: ignore
    def QDateToString(self, qdate: QDate):
        """
        Converts the date selected to a string in MMdd

        Parameters
        ----------
        qdate : QDate
            Date that will be transformed
        """
        self.date = qdate.toString("MMdd", self.calendar.calendar())
        self.done(0)

    class CustomCalendar(QCalendarWidget):
        """Modified QCalendarWidget"""

        clicked: SignalInstance

        def __init__(self, parent: QDialog) -> None:
            """
            Initialize the modified calendar

            Parameters
            ----------
            parent : QDialog
                QDialog that will be attached to the calendar
            """
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


class DocumentCreatedMessageBox(QMessageBox):
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
    openFile: () -> ()
        Open the file set, according to the current OS
    """

    def __init__(self, filepath: str, window: QWidget) -> None:
        super().__init__(window)

        self.filepath = filepath

        self.setIcon(QMessageBox.Icon.Information)
        self.setWindowTitle(f"Damysos - {__version__} - Document généré")

        self.setText(f"Le document a été créé:\n{filepath}\n\nVoulez-vous l'ouvrir?")

        self.buttonAccept = self.addButton(
            "Ouvrir le fichier", QMessageBox.ButtonRole.AcceptRole
        )

        self.buttonReject = self.addButton("Non", QMessageBox.ButtonRole.RejectRole)

    def exec_(self):
        """Show the alert"""
        if not super().exec_():  # if exited with Success (0)
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

    class DocumentExistsMessageBox(QMessageBox):
        """
        Custom QMesageBox asking if user wants to overwrite contents of the file

        Attributes
        ----------
        buttonAccept : QPushButton (role: QMessageBox.ButtonRole.AcceptRole)
            Button accepting the overwrite

        buttonReject : QPushButton (role: QMessageBox.ButtonRole.RejectRole)
            Button refusing the overwrite
        """

        def __init__(self, parent: QWidget, file_destroyed: str) -> None:
            super().__init__(parent=parent)

            self.setIcon(QMessageBox.Icon.Information)
            self.setWindowTitle(f"Damysos - {__version__} - Fichier Existant Trouvé")
            self.setText(
                "Damysos a trouvé un fichier ayant le même nom.\n"
                + "Souhaitez-vous écraser le fichier actuel?\n\n"
                + "*ATTENTION CETTE ACTION EST IRRÉVERSIBLE*\n\n"
                + f"Fichier qui sera écrasé: {file_destroyed}"
            )

            self.buttonAccept = self.addButton("Oui", QMessageBox.ButtonRole.AcceptRole)
            self.buttonReject = self.addButton("Non", QMessageBox.ButtonRole.RejectRole)


class AutomaticNumberMessageBox(QMessageBox):
    """
    Custom QMesageBox asking if user wants to overwrite contents of the file

    Attributes
    ----------
    buttonAccept : QPushButton (role: QMessageBox.ButtonRole.AcceptRole)
        Button accepting the overwrite

    buttonReject : QPushButton (role: QMessageBox.ButtonRole.RejectRole)
        Button refusing the overwrite
    """

    def __init__(self, parent: QWidget, new_file: str) -> None:
        super().__init__(parent=parent)

        self.setIcon(QMessageBox.Icon.Information)
        self.setWindowTitle(f"Damysos - {__version__} - Numérotation Automatique")

        self.setText(
            "Damysos a trouvé des documents existants pour cette matière.\n"
            + "Souhaitez-vous poursuivre la numérotation trouvée?\n\n"
            + f"\tNouveau fichier: {new_file}.docx"
        )

        self.buttonAccept = self.addButton("Oui", QMessageBox.ButtonRole.AcceptRole)
        self.buttonReject = self.addButton("Non", QMessageBox.ButtonRole.RejectRole)


class WordSaveFileDialog(QFileDialog):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)

        self.setFileMode(QFileDialog.FileMode.AnyFile)
        self.setNameFilter("Microsoft Word (*.docx)")
        self.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
