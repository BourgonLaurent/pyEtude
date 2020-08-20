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
from PySide2.QtGui import QCursor
from damysos.config.settings import DEFAULT_MATIERES

# Default packages
import locale

# External packages
from typing import cast, Tuple
from PySide2.QtCore import Signal, SignalInstance, Slot, Qt
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
    """
    Group of modified QTableWidget and QPushButton containing additional logic and buttons
    
    Attributes
    ----------
    verticalLayout: QVBoxLayout
        The main layout of the widget, regroups everything
    
    tableWidget: MatiereTableWidget
        The MatiereTableWidget
    
    control: MatiereTableControl
        The buttons under the MatiereTableWidget
    """

    def __init__(self, parent: QWidget) -> None:
        """
        Initialize the Widget

        Parameters
        ----------
        parent : QWidget
            QWidget that will be attached to this widget
        """
        super().__init__(parent=parent)

        self.verticalLayout = QVBoxLayout(self)

        self.tableWidget = MatiereTableWidget(parent=self)
        self.verticalLayout.addWidget(self.tableWidget)

        self.control = MatiereTableControl(parent=self)
        self.verticalLayout.addLayout(self.control.boxlayout)

        self.control.reset.pressed.connect(lambda: print("hi"))


class MatiereTableWidget(QTableWidget):
    """
    Modified QTableWidget containing additional logic
    
    Attributes
    ----------
    verticalLayout: QVBoxLayout
        The main layout of the widget, regroups everything
    
    tableWidget: MatiereTableWidget
        The MatiereTableWidget
    
    control: MatiereTableControl
        The buttons under the MatiereTableWidget
    """

    itemDoubleClicked: SignalInstance

    def __init__(self, parent: QWidget):
        """
        Initialize the Widget

        Parameters
        ----------
        parent : QWidget
            QWidget that will be attached to this widget
        
        Methods
        ----------
        set_headers: () -> ()
            Configures and loads the widget inside the table
        
        set_connections: () -> ()
            Connects the Signals and Slots of components
        
        add_row: () -> ()
            Add a row to the bottom of the table
        
        remove_row: () -> ()
            Remove the selected row (or the last one if none are selected) in the table
        
        clear: () -> ()
            (Override) Remove everything in the table
        
        setTextAt: (row: int, column: int, text: str) -> ()
            Set the text on a new item
        """

        super().__init__(parent=parent)  # type: ignore
        self.setColumnCount(3)
        self.setRowCount(15)

        self.set_headers()
        self.set_connections()

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

    def set_headers(self):
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

    def set_connections(self):
        """Connects the Signals and Slots of components"""
        self.itemDoubleClicked.connect(self.browse_directory)

    def add_row(self):
        """Add a row to the bottom of the table"""
        self.insertRow(self.rowCount())

    def remove_row(self):
        """Remove the selected row (or the last one if none are selected) in the table"""
        self.removeRow(
            self.currentRow() if self.currentRow() > 0 else self.rowCount() - 1
        )

    def clear(self, set_default=False):
        """(Override) Remove everything in the table"""
        super().clear()

        while self.rowCount() > 0:
            self.remove_row()

        if set_default:
            for i, name in enumerate(sorted(DEFAULT_MATIERES, key=locale.strxfrm)):
                self.add_row()
                self.setTextAt((i, 0), name)
                self.setTextAt((i, 1), DEFAULT_MATIERES[name].alias)
                self.setTextAt((i, 2), DEFAULT_MATIERES[name].path)

        self.set_headers()

    def setTextAt(self, coords: Tuple[int, int], text: str):
        """
        Set the text on a new item

        Parameters
        ----------
        coords : Tuple[int, int]
            x: Horizontal Point
            y: Vertical Point

        text : str
            [description]
        """
        table_item = QTableWidgetItem()
        table_item.setText(text)
        table_item.setToolTip(text)

        self.setItem(coords[0], coords[1], table_item)

    @Slot(QTableWidgetItem)  # type: ignore
    def browse_directory(self, item: QTableWidgetItem):
        """
        Opens a dialog to select a folder

        Parameters
        ----------
        item : QTableWidgetItem
            Item that will have the path of the directory
        """
        if item.column() == 2:
            item.setFlags(cast(Qt.ItemFlags, Qt.ItemIsEnabled))

            filename: str = QFileDialog.getExistingDirectory()

            self.setTextAt((item.row(), item.column()), filename or "")


class MatiereTableControl(QWidget):
    def __init__(self, parent: MatiereTable) -> None:
        """
        Initialize the Widget

        Parameters
        ----------
        parent : QWidget
            QWidget that will be attached to this widget
        """
        super().__init__(parent=parent)

        self.boxlayout = QHBoxLayout()  # type: ignore

        self.plus = QPushButton(text="+", parent=self)
        self.plus.setFixedSize(21, 24)
        # self.plus.pressed.connect(
        #     lambda: print("hi")
        # )  # parent.tableWidget.add_row)  # type: ignore
        self.boxlayout.addWidget(self.plus)

        # self.minus = QPushButton(text="-", parent=self)
        # self.minus.setFixedSize(21, 24)
        # self.minus.clicked.connect(parent.tableWidget.remove_row)  # type: ignore
        # self.boxlayout.addWidget(self.minus)

        # self.spacer = QSpacerItem(
        #     100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        # )
        # self.boxlayout.addItem(self.spacer)

        self.reset = QPushButton(text="Réinitialiser", parent=self)
        self.reset.setFixedSize(85, 24)
        # self.reset.clicked.connect(parent.tableWidget.clear)  # type: ignore
        self.boxlayout.addWidget(self.reset)
