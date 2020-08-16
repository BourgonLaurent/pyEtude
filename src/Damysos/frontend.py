# -*- coding: utf-8 -*-
"""
                 ███████╗████████╗██╗   ██╗██████╗ ███████╗
                 ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝
██████╗ ██╗   ██╗█████╗     ██║   ██║   ██║██║  ██║█████╗  
██╔══██╗╚██╗ ██╔╝██╔══╝     ██║   ██║   ██║██║  ██║██╔══╝  
██████╔╝ ╚████╔╝ ███████╗   ██║   ╚██████╔╝██████╔╝███████╗
██╔═══╝   ╚██╔╝  ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
██║        ██║   MIT © Laurent Bourgon 2020
╚═╝        ╚═╝   
"""
## Imports
# Project packages
from damysos import __version__, CONFIG_FILE
from .document import Document
from .helpers.downloader import FileDownloader
from .helpers.updater import check_updates
from .ui.main_ui import Ui_MainWindow
from .ui.styles_ui import CustomStyles
from .ui.dialogs import (
    AutomaticNumberMessageBox,
    CalendarDialog,
    DocumentCreatedMessageBox,
    WordSaveFileDialog,
)

# Default packages
import json, locale, os, sys

# External packages
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import *

## CONFIGURATIONS
MODEL_DEFAULT_CONFIG = {
    "default": None,
    "models": {},
    "default_models": {
        "Documents de Révision": {
            "filepath": os.path.join(os.getcwd(), "Documents de Révision.docx"),
            "folderpath": "Documents de Révision",
            "values": {
                "auteur": "Auteur",
                "matiere": "Matière",
                "niveau": "Niveau",
                "numero": "Numéro",
                "section": "Section",
                "soustitre": "Sous-Titre",
                "titre": "Titre",
            },
        }
    },
}


class frontEnd:
    """## GUI de l'application, s'occupe de montrer à l'utilisateur les options possibles

    ### Méthodes:\n
        \t__init__ -- Prépare l'environnement de travail
        \texecuteGUI -- Génère et lance le GUI
    """

    def __init__(self):
        """## Prépare l'environnement de travail"""
        # Crée une application vide
        self.app = QApplication([])

        # Crée des instances de la fenêtre générée avec le fichier UI
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()

        # Associe le design à l'interface graphique
        self.ui.setupUi(self.window)

        # Spécifie l'apparence générale universelle de l'interface
        self.app.setStyle("Fusion")

        # Vérifie si une version plus récente existe
        check_updates(window=self.window)

    def executeGUI(self):
        """## Génère et lance le GUI"""
        # Vérifie si c'est la première fois que le programme est exécuté
        self.firstLaunch()

        # Mise en place de l'onglet de configuration
        self.configTab()

        # Assigne le nom de la fenêtre
        self.window.setWindowTitle("Damysos - v" + __version__)
        # Affiche la fenêtre
        self.window.show()
        # Lance le fonctionnement en arrière-plan de l'application
        self.app.exec_()

    def firstLaunch(self):
        # Crée les matières par défaut
        self.matieresDefault = {
            "Anglais": ["ANG", ""],
            "Arts": ["ART", ""],
            "Chimie": ["CHM", ""],
            "Éducation Financière": ["EFI", ""],
            "Éducation Physique": ["EDP", ""],
            "Éthique et Culture Religieuse": ["ECR", ""],
            "Français": ["FRA", ""],
            "Mathématiques": ["MAT", ""],
            "Monde Contemporain": ["MDC", ""],
            "Physique": ["PHY", ""],
        }
        # Vérifie si la configuration a déjà été faite
        if os.path.isfile(os.path.join("./", CONFIG_FILE)):
            # Change le mode
            self.ui.tabWidget.setConfigurationMode(in_configuration_mode=False)

            # Lit le document de configuration et assigne:
            # self.auteur, self.niveau, self.matieres
            self.readJSON()
            # Asssigne les matières selon le fichier de configuration dans le tableau
            self.setMatieres(self.matieres)

            # Met le nom de l'auteur et du niveau selon le fichier de configuration
            self.ui.auteurLineEdit.setText(self.auteur)
            self.ui.niveauLineEdit.setText(self.niveau)

            self.genGroupBox = {
                "titre": self.ui.titreGroupBox,
                "soustitre": self.ui.soustitreGroupBox,
                "matiere": self.ui.matGroupBox,
                "numero": self.ui.numGroupBox,
                "section": self.ui.sectionGroupBox,
                "auteur": self.ui.auteurPersoGroupBox,
                "niveau": self.ui.niveauPersoGroupBox,
            }

            # Configuration terminée, met en place l'onglet de modèles
            self.modelTab()

            # Configuration terminée, met en place l'onglet de génération
            self.genTab()

        else:
            assert FileNotFoundError
            # Change le mode
            self.ui.tabWidget.setConfigurationMode(in_configuration_mode=True)

            # Assigne les matières par défaut dans le tableau
            self.setMatieres(self.matieresDefault)

    def setMatieres(self, datadict: dict):
        """## Insère le dictionnaire donné dans le tableau self.ui.matiereTable.tableWidget
        
        ### Arguments:\n
            \tdatadict {dict} -- Dictionnaire des matières
        """
        # Supprime toutes les anciennes rangées
        self.ui.matiereTable.tableWidget.clear()
        # Insère les données du dictionnaire dans le tableau
        for i, key in enumerate(sorted(datadict, key=locale.strxfrm)):
            self.ui.matiereTable.tableWidget.insertRow(
                self.ui.matiereTable.tableWidget.rowCount()
            )
            self.ui.matiereTable.tableWidget.setTextAt((i, 0), key)
            self.ui.matiereTable.tableWidget.setTextAt((i, 1), datadict[key][0])
            self.ui.matiereTable.tableWidget.setTextAt((i, 2), datadict[key][1])

    def readJSON(self):
        """## Lit le fichier de configuration .json et lui attribue les informations contenues"""
        # Prends le dictionnaire du fichier de configuration
        with open(CONFIG_FILE, encoding="utf-8") as json_f:
            jsonData = json.load(json_f)
        # Attribue l'auteur et le niveau
        self.auteur = jsonData["auteur"]
        self.niveau = jsonData["niveau"]

        # Vérifie si des matières personnalisées exsitent
        self.matieres = jsonData.get("matieres", self.matieresDefault)

        # Vérifie si les modèles existent
        self.modelConfig = jsonData.get("modeles", MODEL_DEFAULT_CONFIG)

    def writeJSON(self):
        json_data = dict()
        json_data["auteur"] = self.auteur
        json_data["niveau"] = self.niveau
        json_data["matieres"] = dict()
        # Vérifie s'il y a des matières personnalisées
        if self.ui.matieresConfig.isChecked() == True:
            for key, value in self.matieres.items():
                json_data["matieres"][key] = value

        if hasattr(self, "modelConfig"):
            json_data["modeles"] = self.modelConfig

        # Crée le fichier de configuration
        with open(CONFIG_FILE, "w", encoding="utf-8") as json_f:
            # Formatte le fichier JSON
            json.dump(json_data, json_f, sort_keys=True, indent=4)

        QMessageBox.information(
            self.window,
            "Configuration sauvegardée",
            "Vos paramètres ont été exportés avec succès",
        )

    def genTab(self):
        # Gestion des modèles
        self.modelGenTab()

        # Mise en place du menu pour les matières et le numéro
        self.matGenTab()
        self.numGenTab()

        # Met le nom de l'auteur et du niveau selon le fichier de configuration
        self.ui.auteurPersoLabel.setText(self.auteur)
        self.ui.niveauPersoLabel.setText(self.niveau)
        # Applique le style à l'entrée de texte
        # for le in (self.ui.matLineEdit, self.ui.numLineEdit):
        #     le.setStyleSheet(CustomStyles.LINE_EDIT)

        # Mise en place de l'emplacement de sauvegarde
        self.pathGenTab()

        # Connection du bouton 'Générer' à sa fonction
        self.ui.genPushButton.pressed.connect(self.createDocument)  # type: ignore

    def createDocument(self):
        self.model = self.ui.modelLineEdit.getText()
        model_config = self.modelConfig["models"][self.model]

        if not self.model:
            QMessageBox.critical(
                self.window,
                f"Damysos - {__version__} - Générateur",
                "Aucun modèle n'est sélectionné",
            )
            return FileNotFoundError

        if not os.path.isfile(model_config["filepath"]):
            QMessageBox.critical(
                self.window,
                f"Damysos - {__version__} - Modèle",
                f"Le modèle: {self.model} n'a pas été trouvé.\n\n"
                + "Veuillez vous assurez qu'il est bien dans l'emplacement sélectionné",
            )
            return FileNotFoundError

        if os.path.isfile(self.filepaths[2]):
            msg = DocumentCreatedMessageBox.DocumentExistsMessageBox(
                self.window, self.filepaths[2]
            )

            if msg.exec_():  # If user rejects
                return FileExistsError

        if not os.path.isdir(self.filepaths[0]) and not os.path.exists(
            self.filepaths[0]
        ):
            os.mkdir(self.filepaths[0])

        values = {
            "titre": self.ui.titreLineEdit.getText(),
            "soustitre": self.ui.soustitreLineEdit.getText(),
            "matiere": self.matiere,
            "numero": self.numero,
            "section": self.ui.sectionLineEdit.getText(),
            "auteur": self.auteur,
            "niveau": self.niveau,
        }

        values = {i: values[i] for i in values if model_config["values"][i]}

        document = Document(values, model_config["filepath"], self.filepaths[2])

        document.packWord()

        DocumentCreatedMessageBox(document.filepath, self.window).exec_()

    def matGenTab(self):
        def isChecked(selection):
            if selection.text() == "Personnaliser":
                self.ui.matLineEdit.setEnabled(True)
                self.ui.matLineEdit.clear()
                self.ui.matLineEdit.setFocus(QtCore.Qt.FocusReason.MenuBarFocusReason)
                self.customMatName = True
            else:
                self.customMatName = False
                self.ui.matLineEdit.setEnabled(False)
                self.ui.matLineEdit.setText(self.matieres[selection.text()][0])

                if selection.text() == "Automatique":
                    self.checkNumMat()

        self.matiere = "PHY"

        matMenu = QMenu("matMenu", self.window)
        matMenu.triggered.connect(isChecked)
        self.ui.matToolButton.setMenu(matMenu)
        matActionGroup = QActionGroup(matMenu)
        matActionGroup.setExclusive(True)

        for mat in sorted(self.matieres, key=locale.strxfrm):
            matMenu.addAction(
                matActionGroup.addAction(QAction(f"{mat}", checkable=True))
            )

        matMenu.addSeparator()
        personalizeMatAction = matActionGroup.addAction(
            QAction("Personnaliser", checkable=True)
        )
        matMenu.addAction(personalizeMatAction)

        self.customMatName = False
        self.filepaths = [".", "PHY-0624.docx", os.path.join(".", "PHY-0624.docx")]
        self.defaultFilePaths = self.filepaths
        self.defaultFilePathChanged()

        self.ui.matLineEdit.textChanged.connect(self.checkNumMat)

    def checkNumMat(self, connection="", prefix="CHP"):
        def findFiles(prefix):
            self.matiere = self.ui.matLineEdit.getText().translate(
                {ord(i): None for i in r'\/:*?"<>|'}
            )
            matpath = os.path.join(
                self.checkCustomMatNamePath(), self.ui.modelLineEdit.getText(),
            )

            try:
                return [
                    f  # Check and return files with these conditions:
                    for f in os.listdir(matpath)  # Inside matpath
                    if os.path.isfile(os.path.join(matpath, f))  # Is a file
                    and f.startswith(f"{self.matiere}-{prefix}")  # Good Format
                    and f.endswith(".docx")  # Is a word document (check extension)
                ]

            except FileNotFoundError:  # If the directory doesn't exists
                return []

        matched_files = findFiles(prefix)
        if not matched_files and connection:
            matched_files = findFiles("MOD")

            if matched_files:
                prefix = "MOD"

        new_name = str()

        if matched_files:
            new_name = prefix + (
                str(
                    int(
                        max(matched_files)
                        .replace(f"{self.matiere}-{prefix}", "")
                        .replace(".docx", "")
                    )
                    + 1
                )
            )

            if not self.autoNumAction.isChecked():
                auto_num = AutomaticNumberMessageBox(
                    self.window, f"{self.matiere}-{new_name}"
                )

                if auto_num.exec_():  # If user rejects
                    self.autoNumAction.setChecked(False)
                    return
                else:
                    self.autoNumAction.setChecked(True)

        elif self.autoNumAction.isChecked():
            new_name = f"{prefix}1"

        if new_name:
            self.ui.numLineEdit.setEnabled(False)
            self.ui.numLineEdit.setText(new_name)

        self.defaultFilePathChanged()

    def checkCustomMatNamePath(self):
        if self.customMatName:
            return os.getcwd()
        else:
            for mat in self.matieres.values():
                if mat[0] == self.matiere:
                    if mat[1] == "":  # S'il n'y a aucun chemin perso pour cette matière
                        return (
                            os.getcwd()
                        )  # Overwrite le chemin perso par le chemin actuel
                    else:
                        return mat[1]

    def numGenTab(self):
        self.numero = "0624"

        def isChecked(selection):
            if selection.text() == calendarAction.text():
                calendarView()
            elif selection.text() == personalizeNumAction.text():
                self.ui.numLineEdit.setEnabled(True)
                self.ui.numLineEdit.clear()
                self.ui.numLineEdit.setFocus(QtCore.Qt.FocusReason.MenuBarFocusReason)
            elif selection.text() == self.autoNumAction.text():
                self.checkNumMat()
            else:
                self.ui.numLineEdit.setEnabled(False)
                self.ui.numLineEdit.setText(selection.text())
                self.checkNumMat(prefix=selection.text()[:3])

        def calendarView():
            calendar_dialog = CalendarDialog(self.window)
            calendar_dialog.exec_()
            try:
                self.numero = calendar_dialog.date
            except AttributeError:
                pass

            self.ui.numLineEdit.setText(self.numero)

        numMenu = QMenu("numMenu", self.window)
        numMenu.triggered.connect(isChecked)
        self.ui.numToolButton.setMenu(numMenu)
        numActionGroup = QActionGroup(numMenu)
        numActionGroup.setExclusive(True)

        chapterButton = numMenu.addMenu("Chapitre")
        moduleButton = numMenu.addMenu("Module")
        for short, button in {"CHP": chapterButton, "MOD": moduleButton}.items():
            for i in range(20):
                button.addAction(
                    numActionGroup.addAction(
                        QAction(f"{short}{str(i)}", checkable=True)
                    )
                )

        calendarAction = numActionGroup.addAction(
            QAction("Choisir une date", checkable=True)
        )
        numMenu.addAction(calendarAction)
        numMenu.addSeparator()

        self.autoNumAction = QAction("Automatique", checkable=True)
        autoNumActionG = numActionGroup.addAction(self.autoNumAction)
        numMenu.addAction(autoNumActionG)

        personalizeNumAction = numActionGroup.addAction(
            QAction("Personnaliser", checkable=True)
        )
        numMenu.addAction(personalizeNumAction)

        self.ui.numLineEdit.textChanged.connect(self.defaultFilePathChanged)

    def defaultFilePathChanged(self):
        self.matiere = self.ui.matLineEdit.getText().translate(
            {ord(i): None for i in '\\/:*?"<>|'}
        )

        self.numero = self.ui.numLineEdit.getText().translate(
            {ord(i): None for i in '\\/:*?"<>|'}
        )

        matpath = self.checkCustomMatNamePath()
        self.defaultFilePaths = [
            os.path.join(
                matpath,
                self.modelConfig["models"][self.ui.modelLineEdit.getText()][
                    "folderpath"
                ],
            ),  # Chemin
            f"{self.matiere}-{self.numero}.docx",
        ]  # Fichier

        self.defaultFilePaths.append(
            os.path.join(self.defaultFilePaths[0], self.defaultFilePaths[1])
        )  # Chemin complet

        self.filepaths = self.defaultFilePaths
        self.updatePathLabel()

    def pathGenTab(self):
        def isChecked(selection):
            if selection.text() == openPathAction.text():
                if sys.platform.startswith("win"):
                    try:
                        os.startfile(self.filepaths[0])  # type: ignore
                    except:
                        pass
                else:
                    os.system(fr"open {self.filepaths[0]}")

            elif selection.text() == customPathAction.text():
                getSaveFilePath = WordSaveFileDialog(parent=self.window)
                getSaveFilePath.exec_()
                if getSaveFilePath.selectedFiles():
                    self.filepaths = [
                        getSaveFilePath.directory().path(),
                        getSaveFilePath.selectedFiles()[0].replace(
                            getSaveFilePath.directory().path(), ""
                        ),
                        getSaveFilePath.selectedFiles()[0],
                    ]
            elif selection.text() == customDirectoryAction.text():
                filepath = QFileDialog.getExistingDirectory()
                if filepath:
                    self.filepaths = [
                        filepath,
                        f"/{self.matiere}-{self.numero}.docx",
                        os.path.join(filepath, f"{self.matiere}-{self.numero}.docx"),
                    ]

            elif selection.text() == defaultPathAction.text():
                self.filepaths = self.defaultFilePaths

            self.updatePathLabel()

        def QLActivated():
            pathMenu.exec_(
                self.ui.pathPathLabel.mapToGlobal(
                    QtCore.QPoint(0, self.ui.pathPathLabel.geometry().height())
                )
            )

        pathMenu = QMenu("pathMenu", self.window)
        pathMenu.triggered.connect(isChecked)
        pathActionGroup = QActionGroup(pathMenu)

        self.ui.pathPathLabel.linkActivated.connect(QLActivated)

        openPathAction = pathActionGroup.addAction(
            QAction("Ouvrir le dossier sélectionné")
        )
        pathMenu.addAction(openPathAction)
        pathMenu.addSeparator()

        customPathAction = pathActionGroup.addAction(QAction("Enregistrer sous..."))
        pathMenu.addAction(customPathAction)

        customDirectoryAction = pathActionGroup.addAction(
            QAction("Choisir le dossier de sortie")
        )
        pathMenu.addAction(customDirectoryAction)
        pathMenu.addSeparator()

        defaultPathAction = pathActionGroup.addAction(
            QAction("Restaurer la valeur par défaut")
        )
        pathMenu.addAction(defaultPathAction)

    def updatePathLabel(self):
        fp = (
            self.filepaths[2].replace("/", " > ").replace("\\", " > ")
        )  # Bypass f-string \\ restriction
        self.ui.pathPathLabel.setText(
            QtCore.QCoreApplication.translate(
                "MainWindow",
                fr"""<html><head/><body><p><a href="none"><span style=" font-size:11pt; text-decoration: underline; color:\#f0f0f0;">{fp}</span></a></p></body></html>""",
            )
        )

    def configTab(self):
        def saveVariable():
            self.auteur = self.ui.auteurLineEdit.getText()
            self.niveau = self.ui.niveauLineEdit.getText()

            self.matieres = {}

            for row in range(self.ui.matiereTable.tableWidget.rowCount()):
                matiere = self.ui.matiereTable.tableWidget.item(row, 0)
                mat = self.ui.matiereTable.tableWidget.item(row, 1)
                path = self.ui.matiereTable.tableWidget.item(row, 2)
                if matiere and mat:
                    if matiere.text() and mat.text():
                        path_text = path.text() if path else ""
                        self.matieres[matiere.text()] = [
                            mat.text(),
                            path_text,
                        ]

            self.writeJSON()
            self.firstLaunch()

        self.ui.configSaveButton.clicked.connect(saveVariable)

    def modelTab(self):
        self.modelForm = {
            "titre": [self.ui.titreModelCheckBox, self.ui.titreModelLineEdit],
            "soustitre": [
                self.ui.soustitreModelCheckBox,
                self.ui.soustitreModelLineEdit,
            ],
            "matiere": [self.ui.matiereModelCheckBox, self.ui.matiereModelLineEdit],
            "numero": [self.ui.numeroModelCheckBox, self.ui.numeroModelLineEdit],
            "section": [self.ui.sectionModelCheckBox, self.ui.sectionModelLineEdit],
            "auteur": [self.ui.auteurModelCheckBox, self.ui.auteurModelLineEdit],
            "niveau": [self.ui.niveauModelCheckBox, self.ui.niveauModelLineEdit],
        }

        self.modelPathForm = {
            "model_file": self.ui.modelPathModelLabel,
            "destination": self.ui.modelDestinationLineEdit,
        }

        self.modelStopSaving = False

        def add_row_menu():
            dialog = QInputDialog(self.window)

            dialog.setWindowTitle("Nouveau")
            dialog.setLabelText("Nom du modèle:")
            dialog.setCancelButtonText("Annuler")

            # Code de sortie (1=OK), texte
            ok, text_entered = dialog.exec_(), str(dialog.textValue())

            if ok and text_entered:
                if not self.ui.modelListWidget.findItems(
                    text_entered, QtCore.Qt.MatchFlags.MatchExactly
                ):
                    self.ui.modelListWidget.addItem(text_entered)

                    self.modelConfig["models"][text_entered] = {
                        "filepath": os.path.join(
                            os.getcwd(), "models", "Documents de Révision.docx"
                        ),
                        "folderpath": "Documents de Révision",
                        "values": {
                            "auteur": "Auteur",
                            "matiere": "Matière",
                            "niveau": "Niveau",
                            "numero": "Numéro",
                            "section": "Section",
                            "soustitre": "Sous-Titre",
                            "titre": "Titre",
                        },
                    }
                else:
                    QMessageBox.critical(
                        self.window, "Nouveau", "Il existe déjà un modèle avec ce nom"
                    )

        def remove_row():
            self.modelConfig["models"].pop(self.ui.modelListWidget.currentItem().text())
            self.ui.modelListWidget.takeItem(self.ui.modelListWidget.currentRow())

        def reset_rows():
            self.ui.modelListWidget.clear()
            self.modelConfig["models"] = self.modelConfig["default_models"]

            for model in self.modelConfig["models"]:
                self.ui.modelListWidget.addItem(model)

        def model_selection_changed(row):
            # Désactive tout si rien n'est sélectionné
            state = row != -1

            for component in (
                self.ui.modelListMinus,
                self.ui.modelValuesGroupBox,
                self.ui.modelPathsGroupBox,
                self.ui.modelDefaultPushButton,
            ):
                component.setEnabled(state)
            for checkBox, lineEdit in self.modelForm.values():
                checkBox.setChecked(state)
                lineEdit.setEnabled(state)
                lineEdit.clear()

            if not state:
                return

            model = self.ui.modelListWidget.item(row).text()
            model_config = self.modelConfig["models"][model]

            self.modelStopSaving = True

            if model_config["values"]:
                for form_value in self.modelForm:
                    if model_config["values"][form_value]:
                        self.modelForm[form_value][0].setChecked(True)
                        self.modelForm[form_value][1].setEnabled(True)
                        self.modelForm[form_value][1].setText(
                            model_config["values"][form_value]
                        )
                    else:
                        self.modelForm[form_value][0].setChecked(False)
                        self.modelForm[form_value][1].setEnabled(False)
                        self.modelForm[form_value][1].clear()

                if model == self.modelConfig["default"]:
                    self.ui.modelDefaultPushButton.setEnabled(False)

                self.modelPathForm["model_file"].setText(
                    " > ".join(
                        os.path.normpath(model_config["filepath"]).split(os.path.sep)
                    )
                )

                self.modelPathForm["destination"].setText(model_config["folderpath"])

            else:  # Rien n'est enregistré
                self.modelPathForm["model_file"].setText(
                    " > ".join(
                        os.path.normpath(
                            os.path.join(os.getcwd(), f"{model}.docx")
                        ).split(os.path.sep)
                    )
                )
                self.modelPathForm["destination"].setPlaceholderText(model)

            self.modelStopSaving = False

        def value_form_changed():
            if self.modelStopSaving:
                return
            if self.ui.modelListWidget.currentRow() < 0:
                return

            model = self.ui.modelListWidget.currentItem().text()

            for checkBox, lineEdit in self.modelForm.values():
                text = lineEdit.getText()
                lineEdit.setEnabled(checkBox.isChecked())

                if not checkBox.isChecked():
                    text = None

                self.modelConfig["models"][model]["values"][checkBox.text()] = text

            self.modelConfig["models"][model]["filepath"] = os.path.normpath(
                self.ui.modelPathModelLabel.text().replace(" > ", os.path.sep)
            )

            self.modelConfig["models"][model][
                "folderpath"
            ] = self.ui.modelDestinationLineEdit.getText()

        def model_choose_path():
            # Prend le nom du fichier et le nettoie
            model_filename = " > ".join(
                os.path.normpath(
                    QFileDialog.getOpenFileName(
                        self.window, "Open File", os.getcwd(), "Microsoft Word (*.docx)"
                    )[0]
                ).split(os.path.sep)
            )

            if model_filename != ".":
                self.ui.modelPathModelLabel.setText(
                    model_filename
                )  # Met le nom du fichier

            value_form_changed()

        def set_default_model(item):
            # Clean
            for index in range(self.ui.modelListWidget.count()):
                self.ui.modelListWidget.item(index).setFont(QtGui.QFont())

            # Add to config & GUI
            self.modelConfig["default"] = item.text()
            item.setFont(QtGui.QFont("Consolas"))

            # Remove access to default button
            self.ui.modelDefaultPushButton.setEnabled(False)

        def save_write_values():
            self.writeJSON()
            self.modelGenTab()

        # CHECK DEFAULT MODELS
        if not self.modelConfig["models"]:
            self.modelConfig["models"] = self.modelConfig["default_models"]
            QMessageBox.information(
                self.window,
                f"Damysos - {__version__} - Modèles par défaut",
                "Aucun modèle n'a été trouvé.\n\n"
                + "Les modèles par défaut vont alors être téléchargés et configurés automatiquement.",
            )

            for model in self.modelConfig["default_models"]:
                if not os.path.isfile(os.path.join("models", f"{model}.docx")):
                    FileDownloader(f"models/{model}.docx").saveFile()

        for model in self.modelConfig["models"]:
            self.ui.modelListWidget.addItem(model)

        for index in range(self.ui.modelListWidget.count()):
            if (
                not self.modelConfig["default"]
                or not self.modelConfig["default"] in self.modelConfig["models"]
            ):
                set_default_model(self.ui.modelListWidget.item(index))
                self.writeJSON()
                self.modelGenTab()
            if (
                self.modelConfig["default"]
                == self.ui.modelListWidget.item(index).text()
            ):
                set_default_model(self.ui.modelListWidget.item(index))

        ## CONNECTIONS

        self.ui.modelListPlus.pressed.connect(add_row_menu)
        self.ui.modelListMinus.pressed.connect(remove_row)
        self.ui.modelListReset.pressed.connect(reset_rows)

        self.ui.modelListWidget.currentRowChanged.connect(model_selection_changed)

        for line in self.modelForm.values():
            line[0].stateChanged.connect(value_form_changed)
            line[1].editingFinished.connect(value_form_changed)
        self.ui.modelDestinationLineEdit.editingFinished.connect(value_form_changed)

        self.ui.modelPathPushButton.pressed.connect(model_choose_path)
        self.ui.modelDefaultPushButton.pressed.connect(
            lambda: set_default_model(self.ui.modelListWidget.currentItem())
        )

        self.ui.modelApplyPushButton.pressed.connect(save_write_values)

    def switchModel(self, model):
        model_config = self.modelConfig["models"][model]

        self.ui.modelLineEdit.setText(model)

        for groupbox in self.genGroupBox:
            if model_config["values"][groupbox]:
                self.genGroupBox[groupbox].setTitle(model_config["values"][groupbox])

            self.genGroupBox[groupbox].setEnabled(
                bool(model_config["values"][groupbox])
            )

    def modelGenTab(self):
        def model_menu_connection(selection):
            self.switchModel(selection.text())
            self.defaultFilePathChanged()

        modelMenu = QMenu("modelMenu", self.window)
        modelMenu.triggered.connect(model_menu_connection)
        self.ui.modelToolButton.setMenu(modelMenu)

        modelActionGroup = QActionGroup(modelMenu)
        modelActionGroup.setExclusive(True)

        for model in sorted(self.modelConfig["models"], key=locale.strxfrm):
            if model == self.modelConfig["default"]:
                self.switchModel(model)
            modelMenu.addAction(
                modelActionGroup.addAction(QAction(f"{model}", checkable=True))
            )
