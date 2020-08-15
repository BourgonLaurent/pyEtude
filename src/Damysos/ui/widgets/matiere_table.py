## matiere_table_widget.py - damysos.ui.widgets
# Label that prevents using dangerous and breaking characters
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

# External packages
from typing import cast, List
from PySide2.QtCore import QRect, SignalInstance
from PySide2.QtGui import Qt
from PySide2.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView,
    QAbstractScrollArea,
)


class MatiereTable(QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent=parent)

        self.verticalLayout = QVBoxLayout(self)

        self.tableWidget = MatiereTableWidget(parent=self)
        self.verticalLayout.addWidget(self.tableWidget)

        self.control = MatiereTableControl(self)
        self.verticalLayout.addLayout(self.control.boxlayout)


class MatiereTableWidget(QTableWidget):
    """QLabel that prevents using dangerous and breaking characters"""

    def __init__(self, parent: QWidget):
        """
        Creates the QLabel and sets its text

        Parameters
        ----------
        parent : QWidget
            Any Widget that will be parent of the QLabel
        """

        super().__init__(parent=parent)  # type: ignore
        # self.setGeometry(0, 0, 641, 191)
        self.setColumnCount(3)
        self.setRowCount(15)

        self.setHeaders()
        self.setConnections()

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.setAutoScroll(False)
        self.setAutoScrollMargin(0)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        self.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.setAlternatingRowColors(True)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.setShowGrid(False)
        self.setWordWrap(False)
        self.setCornerButtonEnabled(True)

    def setHeaders(self):
        self.header_matiere = QTableWidgetItem()
        self.header_matiere.setTextAlignment(cast(int, Qt.AlignCenter))
        self.header_matiere.setText("Matière")
        self.setHorizontalHeaderItem(0, self.header_matiere)

        self.header_nom_court = QTableWidgetItem()
        self.header_nom_court.setTextAlignment(cast(int, Qt.AlignCenter))
        self.header_nom_court.setText("Nom Court")
        self.setHorizontalHeaderItem(1, self.header_nom_court)

        self.header_chemin = QTableWidgetItem()
        self.header_chemin.setTextAlignment(cast(int, Qt.AlignCenter))
        self.header_chemin.setText("Chemin")
        self.setHorizontalHeaderItem(2, self.header_chemin)

        self.horizontalHeader().setDefaultSectionSize(175)
        self.horizontalHeader().setHighlightSections(True)
        self.horizontalHeader().setStretchLastSection(True)

        self.verticalHeader().setVisible(False)

    def add_row(self):
        self.insertRow(self.rowCount())

    def remove_row(self):
        self.removeRow(
            self.currentRow() if self.currentRow() > 0 else self.rowCount() - 1
        )

    def reset_table(self):
        self.clear()
        self.setHeaders()

    def check_if_browsing(self, item: QTableWidgetItem):
        if item.column() == 2:
            item.setFlags(cast(Qt.ItemFlags, Qt.ItemIsEnabled))

            filename: str = QFileDialog.getExistingDirectory()

            if not filename:
                self.item(self.currentRow(), 2).setText("")
                return

            table_item = QTableWidgetItem()
            table_item.setText(filename)

            self.setItem(self.currentRow(), 2, table_item)

    def test(self, hi):
        print(hi)

    def setConnections(self):
        self.itemDoubleClicked.connect(self.check_if_browsing)  # type: ignore
        # self.


class MatiereTableControl(QWidget):
    def __init__(self, parent: MatiereTable) -> None:
        super().__init__(parent=parent)
        self.boxlayout = QHBoxLayout(parent)

        self.plus = QPushButton(text="+", parent=self)
        self.plus.setFixedSize(21, 24)
        self.plus.clicked.connect(parent.tableWidget.add_row)  # type: ignore
        self.boxlayout.addWidget(self.plus)

        self.minus = QPushButton(text="-", parent=self)
        self.minus.setFixedSize(21, 24)
        self.minus.clicked.connect(parent.tableWidget.remove_row)  # type: ignore
        self.boxlayout.addWidget(self.minus)

        self.controlSpacer = QSpacerItem(
            100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum  # type: ignore
        )
        self.boxlayout.addItem(self.controlSpacer)

        self.reset = QPushButton(text="Réinitialiser", parent=self)
        self.reset.setFixedSize(85, 24)
        self.reset.clicked.connect(parent.tableWidget.reset_table) # type: ignore
        self.boxlayout.addWidget(self.reset)
