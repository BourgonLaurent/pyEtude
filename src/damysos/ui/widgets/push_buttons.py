## push_buttons.py - damysos.ui.widgets
# Various modified Push Buttons
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
import damysos.ui.designer.designer_ui
from damysos.ui.dialogs import CalendarDialog
from damysos.ui.widgets.line_edits import SafeAdvancedLineEdit
from damysos.config.settings import Settings
from damysos.config.matieres import Matiere

# Default packages
import locale
from typing import cast, overload

# External packages
from PySide2.QtCore import Qt, Signal, SignalInstance, Slot
from PySide2.QtWidgets import (
    QAction,
    QActionGroup,
    QMenu,
    QWidget,
    QPushButton,
)


class SignalizedPushButton(QPushButton):
    pressed: SignalInstance

    @overload
    def __init__(self, parent: QWidget) -> None:
        ...

    @overload
    def __init__(self, text: str, parent: QWidget) -> None:
        super().__init__(text=text or "", parent=parent)


class ConfigPushButton(SignalizedPushButton):
    ui: "damysos.ui.designer.designer_ui.Ui_MainWindow"

    config_done = cast(SignalInstance, Signal())

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent=parent)

        self.pressed.connect(self.save_config)

    def save_config(self):
        settings: Settings = self.ui.settings  # type: ignore

        settings.auteur = self.ui.auteurLineEdit.getText()
        settings.niveau = self.ui.niveauLineEdit.getText()

        settings.matieres.clear()

        for row in range(self.ui.matiereTable.tableWidget.rowCount()):
            name = self.ui.matiereTable.tableWidget.item(row, 0)
            alias = self.ui.matiereTable.tableWidget.item(row, 1)
            path = self.ui.matiereTable.tableWidget.item(row, 2)

            if name and alias:
                settings.matieres[name.text()] = Matiere(
                    alias.text(), path.text() if path else ""
                )

        settings.dump_config_file()

        self.config_done.emit()


class MatiereMenuPushButton(SignalizedPushButton):
    settings: Settings
    requestAutomaticCheck = cast(SignalInstance, Signal(str))

    def __init__(self, parent: QWidget) -> None:
        super().__init__(text="", parent=parent)
        self.line_edit = cast(
            SafeAdvancedLineEdit, parent.findChild(SafeAdvancedLineEdit)
        )

        self.setMenu(QMenu("matMenu", self))

        self.action_group = QActionGroup(self.menu())
        self.action_group.setExclusive(True)

        self.menu().triggered.connect(self.action_changed)  # type: ignore

    def refresh_menu(self, settings: Settings):
        self.settings = settings

        for _action in self.menu().actions():
            self.menu().removeAction(_action)

        for matiere in sorted(self.settings.matieres.keys(), key=locale.strxfrm):
            self.add_action(matiere)

        self.menu().addSeparator()
        self.action_personalize = self.add_action("Personnaliser")

    def add_action(self, text: str) -> QAction:
        action = QAction(text)
        action.setCheckable(True)
        self.menu().addAction(self.action_group.addAction(action))  # type: ignore
        return action

    @Slot(QAction)  # type: ignore
    def action_changed(self, selection: QAction):
        if selection == self.action_personalize:
            self.line_edit.setEnabled(True)
            self.line_edit.clear()
            self.line_edit.setFocus(Qt.FocusReason.MenuBarFocusReason)
        else:
            self.line_edit.setEnabled(False)
            _alias = self.settings.matieres[selection.text()].alias
            self.line_edit.setText(_alias)
            self.requestAutomaticCheck.emit(None)


class NumeroMenuPushButton(SignalizedPushButton):
    requestAutomaticCheck = cast(SignalInstance, Signal(str))

    def __init__(self, parent: QWidget) -> None:
        super().__init__(text="", parent=parent)
        self.line_edit = cast(
            SafeAdvancedLineEdit, parent.findChild(SafeAdvancedLineEdit)
        )

        self.setMenu(QMenu("numMenu", self))

        self.action_group = QActionGroup(self.menu())
        self.action_group.setExclusive(True)

        # Content prefix
        self.action_chapter = self.menu().addMenu("Chapitre")
        self.action_module = self.menu().addMenu("Module")

        for alias, action_menu in {
            "CHP": self.action_chapter,
            "MOD": self.action_module,
        }.items():
            for i in range(20):
                _action = QAction(f"{alias}{i}")
                _action.setCheckable(True)
                action_menu.addAction(self.action_group.addAction(_action))  # type: ignore

        # Date prefix
        self.action_calendar = self.add_action("Choisir une date")
        self.menu().addSeparator()
        # Automatic
        self.action_automatic = self.add_action("Automatique")
        # Custom
        self.action_personalize = self.add_action("Personnaliser")

        self.menu().triggered.connect(self.action_changed)  # type: ignore

    def add_action(self, text: str) -> QAction:
        action = QAction(text)
        action.setCheckable(True)
        self.menu().addAction(self.action_group.addAction(action))  # type: ignore
        return action

    @Slot(str)  # type: ignore
    def action_changed(self, selection: QAction):
        if selection == self.action_calendar:
            calendar_dialog = CalendarDialog(self)
            calendar_dialog.exec_()
            try:
                self.line_edit.setText(calendar_dialog.date)
            except AttributeError:
                return

        elif selection == self.action_automatic:
            self.requestAutomaticCheck.emit(None)

        elif selection == self.action_personalize:
            self.line_edit.setEnabled(True)
            self.line_edit.clear()
            self.line_edit.setFocus(Qt.FocusReason.MenuBarFocusReason)

        else:
            self.line_edit.setEnabled(False)
            self.line_edit.setText(selection.text())
            self.requestAutomaticCheck.emit(selection.text()[:3])
