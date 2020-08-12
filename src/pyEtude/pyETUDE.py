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
# Imports
## Project packages
from . import __version__, CONFIG_FILE, GITHUB_REPO
from .ui.pyEt_main_ui import Ui_MainWindow
from .ui.pyEt_styles_ui import STYLES

## Default packages
import json, locale, os, sys, urllib.request, urllib.error

## External packages
try:
    from PySide2 import QtCore, QtGui
    from PySide2.QtUiTools import QUiLoader
    from PySide2.QtWidgets import *
    from PySide2.QtCore import QFile

    from docxtpl import DocxTemplate
except ImportError as e:
    # Crée le message d'erreur
    error_message = f"""[!] Impossible de continuer:\n\n\t{e.msg}\n\n
[*] Avez-vous installé {e.name}?\nC'est un module nécessaire au fonctionnement de pyÉtude.\n\nEssayez la commande suivante:
\t\tpip install --update {e.name}\n\nSinon référez-vous au README.md de la page GitHub."""
    # Essaie de montrer un message d'erreur à l'aide d'un GUI par défaut
    try:
        from tkinter import Tk
        from tkinter.messagebox import showerror

        Tk().withdraw()
        showerror("pyÉtude - Configuration requise non respectée", error_message)
    except ImportError:  # Le module de GUI n'existe pas
        print(error_message)
    # Quitte le programme en indiquant l'erreur
    sys.exit(e)

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


## GENERAL FUNCTIONS
def downloadData(name, create=True):
    """## Télécharge un fichier du répertoire GitHub raw
    
    ### Arguments:\n
        \tname {str} -- Nom du fichier à prendre
    ### Keyword Arguments:\n
        \tcreate {bool} -- Crée un fichier (default: {True})
    
    ### Returns:\n
        \t[str] -- (si create=False): données décodées qui ont été prises
    """
    if create:
        try:
            urllib.request.urlretrieve(
                urllib.parse.quote(
                    fr"https://raw.githubusercontent.com/{GITHUB_REPO}/{__version__}/src/{name}",
                    safe="/:?=&",
                ),
                name,
            )
        except urllib.error.HTTPError:
            urllib.request.urlretrieve(
                urllib.parse.quote(
                    fr"https://raw.githubusercontent.com/{GITHUB_REPO}/master/src/{name}",
                    safe="/:?=&",
                ),
                name,
            )
    else:
        try:
            with urllib.request.urlopen(
                urllib.parse.quote(
                    fr"https://raw.githubusercontent.com/{GITHUB_REPO}/{__version__}/src/{name}",
                    safe="/:?=&",
                )
            ) as ur:
                return ur.read().decode()
        except urllib.error.HTTPError:
            with urllib.request.urlopen(
                urllib.parse.quote(
                    fr"https://raw.githubusercontent.com/{GITHUB_REPO}/master/src/{name}",
                    safe="/:?=&",
                )
            ) as ur:
                return ur.read().decode()


def checkUpdates(window):
    """## Vérifie les nouvelles versions du logiciek
    
    ### Arguments:\n
        \twindow {PyQt5.QtWidgets.QWidget} -- Instance QWidget auquel la boîte de dialogue s'attachera
    """
    with urllib.request.urlopen(
        urllib.parse.quote(
            fr"https://api.github.com/repos/{GITHUB_REPO}/releases/latest",
            safe="/:?=&",
        )
    ) as ur:
        content = json.loads(ur.read().decode("utf-8"))

    if content["tag_name"] > f"v{__version__}":
        alert = QMessageBox(window)
        alert.setIcon(QMessageBox.Warning)

        alert.setWindowTitle(f"pyÉtude - v{__version__} - Nouvelle version")

        alert.setText(f"Une version plus récente de pyÉtude a été trouvée.")
        alert.setInformativeText(
            f"Version actuelle: v{__version__}<br>Version la plus récente: {content['tag_name']}<br><br><a style='color: white;' href='https://github.com/{GITHUB_REPO}/releases'>Téléchargez-la sur GitHub</a>"
        )

        alert.exec_()


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
        checkUpdates(self.window)

    def executeGUI(self):
        """## Génère et lance le GUI"""
        # Vérifie si c'est la première fois que le programme est exécuté
        self.firstLaunch()

        # Mise en place de l'onglet de configuration
        self.configTab()
        # Mise en place de l'onglet d'information
        self.aboutTab()

        # Assigne le nom de la fenêtre
        self.window.setWindowTitle("pyÉtude - v" + __version__)
        # Affiche la fenêtre
        self.window.show()
        # Lance le fonctionnement en arrière-plan de l'application
        self.app.exec_()

    def esperLimit(self, lineedit):
        lineedit.setValidator(
            QtGui.QRegExpValidator(QtCore.QRegExp(r"[^&\\/]+"), lineedit)
        )  # Empêche l'utilisation des esperluètes "&"

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
            # Active l'onglet du générateur
            self.ui.tabWidget.setTabEnabled(0, True)
            self.ui.tabWidget.setTabToolTip(0, "Créer un document")
            self.ui.tabWidget.setCurrentIndex(0)

            # self.ui.matieresConfig.setChecked(True)

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
            # Empêche l'accès au générateur
            self.ui.tabWidget.setTabEnabled(0, False)
            self.ui.tabWidget.setTabToolTip(0, "Veuillez utilisez le Configurateur")
            self.ui.tabWidget.setTabEnabled(2, False)
            self.ui.tabWidget.setTabToolTip(0, "Veuillez utilisez le Configurateur")

            self.ui.tabWidget.setCurrentIndex(1)

            # Assigne les matières par défaut dans le tableau
            self.setMatieres(self.matieresDefault)

    def setMatieres(self, datadict: dict):
        """## Insère le dictionnaire donné dans le tableau self.ui.matiereTableWidget
        
        ### Arguments:\n
            \tdatadict {dict} -- Dictionnaire des matières
        """
        # Supprime toutes les anciennes rangées
        for i in range(0, self.ui.matiereTableWidget.rowCount() + 1):
            self.ui.matiereTableWidget.removeRow(
                self.ui.matiereTableWidget.rowCount() - 1
            )
        # Insère les données du dictionnaire dans le tableau
        for i, key in enumerate(sorted(datadict, key=locale.strxfrm)):
            self.ui.matiereTableWidget.insertRow(self.ui.matiereTableWidget.rowCount())
            self.ui.matiereTableWidget.setItem(i, 0, QTableWidgetItem(key))
            self.ui.matiereTableWidget.setItem(i, 1, QTableWidgetItem(datadict[key][0]))
            self.ui.matiereTableWidget.setItem(i, 2, QTableWidgetItem(datadict[key][1]))

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
        if (
            self.ui.matieresConfig.isChecked() == True
        ):  # Vérifie s'il y a des matières personnalisées
            for key, value in self.matieres.items():
                json_data["matieres"][key] = value

        if hasattr(self, "modelConfig"):
            json_data["modeles"] = self.modelConfig

        with open(
            CONFIG_FILE, "w", encoding="utf-8"
        ) as json_f:  # Crée le fichier de configuration
            json.dump(
                json_data, json_f, sort_keys=True, indent=4
            )  # Formatte le fichier JSON

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
        for le in (self.ui.matLineEdit, self.ui.numLineEdit):
            le.setStyleSheet(STYLES["line_edit"])
        # Empêche l'utilisation de l'esperluète '&' dans les entrées de texte
        for le in (
            self.ui.matLineEdit,
            self.ui.numLineEdit,
            self.ui.sectionLineEdit,
            self.ui.soustitreLineEdit,
            self.ui.titreLineEdit,
        ):
            self.esperLimit(le)

        # Mise en place de l'emplacement de sauvegarde
        self.pathGenTab()

        # Connection du bouton 'Générer' à sa fonction
        self.ui.genPushButton.pressed.connect(self.createDocument)

    def getLineEditValue(self, lineedit):
        return lineedit.text() or lineedit.placeholderText()

    def createDocument(self):
        self.model = self.getLineEditValue(self.ui.modelLineEdit)
        model_config = self.modelConfig["models"][self.model]

        if not self.model:
            QMessageBox.critical(
                self.window,
                f"pyÉtude - {__version__} - Générateur",
                "Aucun modèle n'est sélectionné",
            )
            return FileNotFoundError

        if not os.path.isfile(model_config["filepath"]):
            QMessageBox.critical(
                self.window,
                f"pyÉtude - {__version__} - Modèle",
                f"Le modèle: {self.model} n'a pas été trouvé.\n\nVeuillez vous assurez qu'il est bien dans l'emplacement sélectionné",
            )
            return FileNotFoundError

        if os.path.isfile(self.filepaths[2]):
            numMatMessageBox = QMessageBox(self.window)
            numMatMessageBox.setIcon(QMessageBox.Information)
            numMatMessageBox.setWindowTitle(
                f"pyÉtude - {__version__} - Fichier Existant Trouvé"
            )
            numMatMessageBox.setText(
                f"pyÉtude a trouvé un fichier ayant le même nom.\nSouhaitez-vous écraser le fichier actuel?\n\n*ATTENTION CETTE ACTION EST IRRÉVERSIBLE*\n\nFichier qui sera écrasé: {self.filepaths[2]}"
            )
            buttonOpen = numMatMessageBox.addButton(QMessageBox.Yes)
            buttonOpen.setText("Oui")
            buttonIgnore = numMatMessageBox.addButton(QMessageBox.No)
            buttonIgnore.setText("Non")
            numMatMessageBox.exec_()

            if numMatMessageBox.clickedButton().text() == "Non":
                return FileExistsError

        if not os.path.isdir(self.filepaths[0]) and not os.path.exists(
            self.filepaths[0]
        ):
            os.mkdir(self.filepaths[0])

        values = {
            "titre": self.getLineEditValue(self.ui.titreLineEdit),
            "soustitre": self.getLineEditValue(self.ui.soustitreLineEdit),
            "matiere": self.matiere,
            "numero": self.numero,
            "section": self.getLineEditValue(self.ui.sectionLineEdit),
            "auteur": self.auteur,
            "niveau": self.niveau,
        }

        values = {i: values[i] for i in values if model_config["values"][i]}

        document = Document(
            values,
            self.modelConfig["models"][self.model]["filepath"],
            self.filepaths[2],
            self.window,
        )

        document.packWord()
        document.sendAlert()

    def matGenTab(self):
        def isChecked(selection):
            if selection.text() == "Personnaliser":
                self.ui.matLineEdit.setEnabled(True)
                self.ui.matLineEdit.clear()
                self.ui.matLineEdit.setFocus()
                self.customMatName = True
            else:
                self.customMatName = False
                self.ui.matLineEdit.setEnabled(False)
                self.ui.matLineEdit.setText(self.matieres[selection.text()][0])

                if selection.text() == "Automatique":
                    self.checkNumMat(automatic=True)

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
            self.matiere = self.getLineEditValue(self.ui.matLineEdit).translate(
                {ord(i): None for i in r'\/:*?"<>|'}
            )
            matpath = os.path.join(
                self.checkCustomMatNamePath(),
                self.getLineEditValue(self.ui.modelLineEdit),
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

        newName = str()

        if matched_files:
            new_suggested_file = (
                int(
                    max(matched_files)
                    .replace(f"{self.matiere}-{prefix}", "")
                    .replace(".docx", "")
                )
                + 1
            )

            if not self.autoNumAction.isChecked():
                numMatMessageBox = QMessageBox(self.window)
                numMatMessageBox.setIcon(QMessageBox.Information)
                numMatMessageBox.setWindowTitle(
                    f"pyÉtude - {__version__} - Fichiers Trouvés"
                )
                numMatMessageBox.setText(
                    f"pyÉtude a trouvé des documents existants pour cette matière.\nSouhaitez-vous poursuivre la numérotation trouvée?\n\n\tNouveau fichier: {self.matiere}-{prefix}{new_suggested_file}"
                )
                buttonOpen = numMatMessageBox.addButton(QMessageBox.Yes)
                buttonOpen.setText("Oui")
                buttonIgnore = numMatMessageBox.addButton(QMessageBox.No)
                buttonIgnore.setText("Non")
                numMatMessageBox.exec_()

                if numMatMessageBox.clickedButton().text() == buttonIgnore.text():
                    return

            newName = f"{prefix}{new_suggested_file}"

        elif self.autoNumAction.isChecked():
            newName = f"{prefix}1"

        if newName:
            self.ui.numLineEdit.setEnabled(False)
            self.ui.numLineEdit.setText(newName)

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
                self.ui.numLineEdit.setFocus()
            else:
                self.ui.numLineEdit.setEnabled(False)
                self.ui.numLineEdit.setText(selection.text())
                self.checkNumMat(prefix=selection.text()[:3])

        def calendarView():
            self.ui.numLineEdit.setEnabled(False)
            calendarView = QDialog(self.window)
            calendarView.setWindowFlags(
                QtCore.Qt.Dialog
                | QtCore.Qt.MSWindowsFixedSizeDialogHint
                | QtCore.Qt.WindowMinimizeButtonHint
            )

            calendar = QCalendarWidget(calendarView)
            calendar.setGeometry(QtCore.QRect(0, 0, 312, 183))
            calendar.setFirstDayOfWeek(QtCore.Qt.Monday)
            calendar.setGridVisible(True)
            calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
            calendar.setObjectName("numCalendarWidget")

            calwe_format = QtGui.QTextCharFormat()
            calwe_format.setForeground(QtGui.QColor("#148CD2"))
            calendar.setWeekdayTextFormat(QtCore.Qt.Saturday, calwe_format)
            calendar.setWeekdayTextFormat(QtCore.Qt.Sunday, calwe_format)

            def qdateToString(qdate):
                self.numero = qdate.toString("MMdd")
                self.ui.numLineEdit.setText(self.numero)
                calendarView.done(0)

            calendar.clicked.connect(qdateToString)
            calendarView.setWindowTitle("Veuillez choisir une date")
            calendarView.exec_()

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
        self.matiere = self.getLineEditValue(self.ui.matLineEdit).translate(
            {ord(i): None for i in '\\/:*?"<>|'}
        )

        self.numero = self.getLineEditValue(self.ui.numLineEdit).translate(
            {ord(i): None for i in '\\/:*?"<>|'}
        )

        matpath = self.checkCustomMatNamePath()
        self.defaultFilePaths = [
            os.path.join(
                matpath,
                self.modelConfig["models"][
                    self.getLineEditValue(self.ui.modelLineEdit)
                ]["folderpath"],
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
                if sys.platform == "win32":
                    try:
                        os.startfile(self.filepaths[0])
                    except:
                        pass
                else:
                    os.system(fr"open {self.filepaths[0]}")

            elif selection.text() == customPathAction.text():
                getSaveFilePath = QFileDialog()
                getSaveFilePath.setNameFilters(["Microsoft Word (*.docx)"])
                getSaveFilePath.setAcceptMode(QFileDialog.AcceptSave)
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
            self.auteur = self.getLineEditValue(self.ui.auteurLineEdit).replace("&", "")
            self.niveau = self.getLineEditValue(self.ui.niveauLineEdit).replace("&", "")

            self.matieres = {}

            for row in range(self.ui.matiereTableWidget.rowCount()):
                matiere = self.ui.matiereTableWidget.item(row, 0)
                mat = self.ui.matiereTableWidget.item(row, 1)
                path = self.ui.matiereTableWidget.item(row, 2)
                if matiere and mat:
                    if matiere.text() and mat.text():
                        path_text = path.text().replace("&", "") if path else ""
                        self.matieres[matiere.text().replace("&", "")] = [
                            mat.text().replace("&", ""),
                            path_text,
                        ]

            self.writeJSON()
            self.firstLaunch()

        # Empêche l'utilisation des esperluètes "&"
        self.esperLimit(self.ui.auteurLineEdit)
        self.esperLimit(self.ui.niveauLineEdit)

        self.ui.configSaveButton.clicked.connect(saveVariable)

        self.matieresConfig()

    def matieresConfig(self):
        def addRow():
            self.ui.matiereTableWidget.insertRow(self.ui.matiereTableWidget.rowCount())

        def delRow():
            self.ui.matiereTableWidget.removeRow(
                (
                    self.ui.matiereTableWidget.rowCount() - 1
                    if self.ui.matiereTableWidget.currentRow() == -1
                    else self.ui.matiereTableWidget.currentRow()
                )
            )

        def resetRows():
            self.setMatieres(self.matieresDefault)

        def checkBrowse():
            self.ui.matiereTableBrowse.setEnabled(
                self.ui.matiereTableWidget.currentColumn() == 2
            )

        def browseDirectory():
            if self.ui.matiereTableWidget.currentColumn() == 2:
                filename = QFileDialog.getExistingDirectory()
                self.ui.matiereTableWidget.setItem(
                    self.ui.matiereTableWidget.currentRow(),
                    2,
                    QTableWidgetItem(filename),
                )

        self.ui.matiereTablePlus.clicked.connect(addRow)
        self.ui.matiereTableMinus.clicked.connect(delRow)
        self.ui.matiereTableReset.clicked.connect(resetRows)

        self.ui.matiereTableBrowse.setEnabled(False)
        self.ui.matiereTableWidget.clicked.connect(checkBrowse)
        self.ui.matiereTableBrowse.clicked.connect(browseDirectory)

    def aboutTab(self):
        self.ui.varVersionLabel.setText(
            QtCore.QCoreApplication.translate(
                "MainWindow",
                f'<html><head/><body><p><span style=" font-size:12pt; font-style:italic;">{__version__}</span></p></body></html>',
            )
        )

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
                    text_entered, QtCore.Qt.MatchExactly
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
                text = self.getLineEditValue(lineEdit)
                lineEdit.setEnabled(checkBox.isChecked())

                if not checkBox.isChecked():
                    text = None

                self.modelConfig["models"][model]["values"][checkBox.text()] = text

            self.modelConfig["models"][model]["filepath"] = os.path.normpath(
                self.ui.modelPathModelLabel.text().replace(" > ", os.path.sep)
            )

            self.modelConfig["models"][model]["folderpath"] = self.getLineEditValue(
                self.ui.modelDestinationLineEdit
            )

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
                f"pyÉtude - {__version__} - Modèles par défaut",
                "Aucun modèle n'a été trouvé.\n\nLes modèles par défaut vont alors être téléchargés et configurés automatiquement.",
            )

            for model in self.modelConfig["default_models"]:
                if not os.path.isfile(os.path.join("models", f"{model}.docx")):
                    downloadData(f"models/{model}.docx")

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


class Document:
    def __init__(self, values, model, filepath, window=""):
        self.values = values
        self.model = model
        self.filepath = filepath
        self.window = window

        self.document = DocxTemplate(self.model)

    def packWord(self):
        self.document.render(self.values)
        self.document.save(self.filepath)

    def sendAlert(self):
        if self.window:  # Si démarré avec Qt
            docMessageBox = QMessageBox(self.window)
            docMessageBox.setIcon(QMessageBox.Information)
            docMessageBox.setWindowTitle(f"pyÉtude - {__version__} - Document généré")

            docMessageBox.setText(
                f"Le document a été créé:\n{self.filepath}\n\nVoulez-vous l'ouvrir?"
            )

            buttonOpen = docMessageBox.addButton(QMessageBox.Open)
            buttonOpen.setText("Ouvrir le fichier")

            buttonIgnore = docMessageBox.addButton(QMessageBox.No)
            buttonIgnore.setText("Non")

            docMessageBox.exec_()

            if docMessageBox.clickedButton().text() == "Ouvrir le fichier":
                if sys.platform.startswith("win32"):
                    try:
                        os.startfile(self.filepath)
                    except:
                        pass
                else:
                    os.system(f'open "{self.filepath}"')
            else:
                assert ConnectionRefusedError
        else:  # Si démarré à partir avec l'invite de commande
            print(f"\nLe document a été créé: {self.filepath}")
