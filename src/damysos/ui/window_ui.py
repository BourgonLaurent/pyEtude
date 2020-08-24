## window_ui.py - damysos.ui
# Modified UI of DamysosMainWindow
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
from damysos.config.settings import Settings
from .designer.designer_ui import Ui_MainWindow

# Default packages
import locale

# External packages
from PySide2.QtCore import Slot, Qt
from PySide2.QtWidgets import QAction, QMainWindow


class DamysosMWUI(Ui_MainWindow):
    def __init__(self, window: QMainWindow):
        super().__init__()
        self.setupUi(window)

        self.settings = Settings.load_config_file(tab_widget=self.tabWidget)
        self.set_settings_values()

        self.matMenuButton.refresh_menu(self)

        self.configSaveButton.ui = self
        self.configSaveButton.config_done.connect(
            lambda: self.tabWidget.setConfigurationMode(in_configuration_mode=False)
        )
        self.configSaveButton.config_done.connect(
            lambda: self.matMenuButton.refresh_menu(self)
        )

        self.matieresConfig.toggled.connect(self.check_matieres_status)  # type: ignore

    def set_settings_values(self):
        self.auteurLineEdit.setText(self.settings.auteur)
        self.niveauLineEdit.setText(self.settings.niveau)

        self.matieresConfig.setChecked(self.settings.custom_matieres)

        self.matiereTable.tableWidget.clear()
        for i, name in enumerate(sorted(self.settings.matieres, key=locale.strxfrm)):
            self.matiereTable.tableWidget.add_row()
            self.matiereTable.tableWidget.setTextAt((i, 0), name)
            self.matiereTable.tableWidget.setTextAt(
                (i, 1), self.settings.matieres[name].alias
            )
            self.matiereTable.tableWidget.setTextAt(
                (i, 2), self.settings.matieres[name].path
            )

    @Slot(bool)  # type: ignore
    def check_matieres_status(self, state: bool):
        self.matiereTable.setEnabled(state)
        self.settings.custom_matieres = state
