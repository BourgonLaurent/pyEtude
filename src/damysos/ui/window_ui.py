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
from damysos.document import Document
from damysos.helpers.utilities import execute_file
from damysos.ui.dialogs import AutomaticNumberMessageBox, WordSaveFileDialog
from .designer.designer_ui import Ui_MainWindow

# Default packages
import locale
import os
from typing import Union
from typing import List

# External packages
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QAction, QFileDialog, QMainWindow


class DamysosMWUI(Ui_MainWindow):
    def __init__(self, window: QMainWindow):
        super().__init__()
        self.setupUi(window)
        self.window = window

        self.settings = Settings.load_config_file(tab_widget=self.tabWidget)
        self.set_settings_values()

        self.matMenuButton.refresh_menu(self.settings)
        self.matMenuButton.requestAutomaticCheck.connect(self.check_automatic_file)
        self.numMenuButton.requestAutomaticCheck.connect(self.check_automatic_file)

        self.matLineEdit.textChanged.connect(self.update_path_label)
        self.numLineEdit.textChanged.connect(self.update_path_label)

        self.pathPathLabel.menu.triggered.connect(self.path_menu_response)  # type: ignore

        self.genPushButton.clicked.connect(self.generateDocument)  # type: ignore

        self.configSaveButton.ui = self  # type: ignore
        self.configSaveButton.config_done.connect(self.refresh_configuration)

        self.matieresConfig.toggled.connect(self.check_matieres_status)  # type: ignore

        self.update_path_label()

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

        if not self.settings.modeles.default or not self.settings.modeles.get_model(
            self.settings.modeles.default
        ):
            self.settings.modeles.default = self.settings.modeles.models[0].name

        self.modelLineEdit.setText(self.settings.modeles.default)

    def get_matiere_path(self) -> str:
        if not self.matMenuButton.action_personalize.isChecked():
            for matiere in self.settings.matieres.values():
                if matiere.alias == self.matLineEdit.getText() and matiere.path:
                    return matiere.path

        return os.getcwd()

    def update_path_label(self, set_directory=True):
        if set_directory:
            self.pathPathLabel.directory = self.get_matiere_path()

        self.pathPathLabel.set_filepath(
            os.path.join(
                self.settings.modeles.get_model(
                    self.settings.modeles.default
                ).export_name,
                f"{self.matLineEdit.getText()}-{self.numLineEdit.getText()}.docx",
            )
        )

    @Slot(QAction)  # type: ignore
    def path_menu_response(self, selection: QAction):
        if selection == self.pathPathLabel.action_open_folder:
            execute_file(self.pathPathLabel.directory)

        elif selection == self.pathPathLabel.action_choose_folder:
            self.pathPathLabel.directory = QFileDialog.getExistingDirectory()
            if self.pathPathLabel.directory:  # Only if clicks on 'Open'
                self.update_path_label(set_directory=False)

        elif selection == self.pathPathLabel.action_choose_file:
            getSaveFilePath = WordSaveFileDialog(parent=self.window)
            if getSaveFilePath.exec_():  # Only if clicks on 'Open'
                if getSaveFilePath.selectedFiles():
                    self.pathPathLabel.directory = getSaveFilePath.directory().path()
                    self.pathPathLabel.set_filepath(
                        os.path.basename(getSaveFilePath.selectedFiles()[0])
                    )

        elif selection == self.pathPathLabel.action_restore_default:
            self.update_path_label()

    @Slot()  # type: ignore
    def refresh_configuration(self):
        self.tabWidget.setConfigurationMode(in_configuration_mode=False)
        self.matMenuButton.refresh_menu(self.settings)

    @Slot(str)  # type: ignore
    def check_automatic_file(self, prefix: Union[str, None]):
        def findFiles(prefix) -> List[str]:
            matpath = os.path.join(
                self.get_matiere_path(),
                self.settings.modeles.get_model(
                    self.settings.modeles.default
                ).export_name,
            )
            try:
                return [
                    f
                    for f in os.listdir(matpath)
                    if os.path.isfile(os.path.join(matpath, f))
                    and f.startswith(f"{matiere}-{prefix}")
                    and f.endswith(".docx")
                ]

            except FileNotFoundError:
                return []

        matiere = self.matLineEdit.getText()
        if not prefix:
            prefix = "CHP"

        matched_files = findFiles(prefix)
        if not matched_files:
            matched_files = findFiles("MOD")

            if matched_files:
                prefix = "MOD"

        new_name = str()

        if matched_files:
            new_name = prefix + (
                str(
                    int(
                        max(matched_files)
                        .replace(f"{matiere}-{prefix}", "")
                        .replace(".docx", "")
                    )
                    + 1
                )
            )

            if not self.numMenuButton.action_automatic.isChecked():
                auto_num = AutomaticNumberMessageBox(
                    self.window, f"{matiere}-{new_name}"
                )

                if auto_num.exec_():
                    self.numMenuButton.action_automatic.setChecked(False)
                    return
                else:
                    self.numMenuButton.action_automatic.setChecked(True)

        elif self.numMenuButton.action_automatic.isChecked():
            new_name = f"{prefix}1"

        if new_name:
            self.numLineEdit.setEnabled(False)
            self.numLineEdit.setText(new_name)

    @Slot(bool)  # type: ignore
    def check_matieres_status(self, state: bool):
        self.matiereTable.setEnabled(state)
        self.settings.custom_matieres = state

    @Slot()  # type: ignore
    def generateDocument(self):
        # Get model name
        model = self.settings.modeles.get_model(self.settings.modeles.default)

        # Get all the values
        access_values = {
            "auteur": self.settings.auteur,
            "niveau": self.settings.niveau,
            "titre": self.titreLineEdit.getText(),
            "soustitre": self.soustitreLineEdit.getText(),
            "matiere": self.matLineEdit.getText(),
            "numero": self.numLineEdit.getText(),
            "section": self.sectionLineEdit.getText(),
        }

        # Only use the values needed
        values = {
            tag: access_values.get(tag, "")
            for tag, name in model.values.__dict__.items()
            if name
        }

        # Create document and export it
        document = Document(model.filepath, values, self.pathPathLabel.filepath)
        document.packWord()

