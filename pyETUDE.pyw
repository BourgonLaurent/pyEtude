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
## Default packages
import json, locale, os, sys, zipfile, urllib.request, urllib.error
## External packages
try:
    from PyQt5 import QtCore, QtGui, QtWidgets, uic
    from PyQt5.QtWidgets import *
except ImportError as e:
    # Crée le message d'erreur
    error_message = f"""[!] Impossible de continuer:\n\n\t{e.msg}\n\n
[*] Avez-vous installé {e.name}?\nC'est un module nécessaire au fonctionnement de pyÉtude.\n\nEssayez la commande suivante:
\t\tpip install {e.name}\n\nSinon référez-vous au README.md de la page GitHub."""
    # Essaie de montrer un message d'erreur à l'aide d'un GUI par défaut
    try:
        from tkinter import Tk
        from tkinter.messagebox import showerror

        Tk().withdraw()
        showerror("pyÉtude - Configuration requise non respectée", error_message)
    except ImportError: # Le module de GUI n'existe pas
        print(error_message)
    # Quitte le programme en indiquant l'erreur
    sys.exit(e)

# Accède aux fichiers depuis la racine du programme, et non l'endroit du shell
os.chdir(os.path.realpath(__file__).replace(os.path.basename(__file__), ""))

# Essaie d'aller dans une langue UTF-8
try:
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
except:
    assert EnvironmentError
    locale.setlocale(locale.LC_ALL, (None, None))

# Paramètres généraux
## Information de la version actuelle
VERSION = r'2.4.0~b5'
DEBUG = True
## Nom de fichiers importants
FILES = {
    "debug":"pyEtude.ui", # (ext: *.ui) Nom du fichier QtDesigner
    "pyuic5":"pyet_ui.py", # (ext: *.py) Nom du fichier .py généré avec pyuic5
    "config":"pyEtude.json" # (ext: *.json) Nom du fichier .json généré avec le configurateur
}
## Assets
GITHUB_LINK = r'https://raw.githubusercontent.com/BourgonLaurent/pyEtude'
STYLES = {
    "menu":"""QMenu {
                  border: 0.5px solid #787878;
                  color: #F0F0F0;
                  margin: 0px;
                }
                QMenu::separator {
                  height: 1px;
                  background-color: #444444;
                }
                QMenu::item {
                  background-color: #262626;
                  padding: 4px 4px 4px 4px;
                  /* Reserve space for selection border */
                  border: 1px transparent #32414B;
                }
                QMenu::item:selected {
                  color: #F0F0F0;
                  background-color: #605e5c;
                }""",
    "message_box":"""QWidget {
                      background-color: #262626;
                      border: 0px solid #32414B;
                      padding: 0px;
                      color: #FFFFFF;
                      selection-background-color: #1464A0;
                      selection-color: #FFFFFF;
                    }
                    QPushButton {
                      background-color: #484644;
                      border: 1px solid #605e5c;
                      color: #FFFFFF;
                      border-radius: 4px;
                      padding-left: 30px;
                      padding-right: 30px;
                      padding-top: 5px;
                      padding-bottom: 5px;
                      outline: none;
                    }
                    QPushButton:pressed {
                      background-color: #323130;
                    }
                    QPushButton:pressed:hover {
                      background-color: #323130;
                    }
                    QPushButton:hover {
                      background-color: #605e5c;
                    }""",
    "calendar":"""QAbstractItemView {
                      alternate-background-color: #484644;
                      color: #F0F0F0;
                      border: 1px solid #32414B;
                      border-radius: 4px;
                    }
                    QWidget {
                      background-color: #262626;
                      border: 0px solid #444444;
                      padding: 0px;
                      color: #FFFFFF;
                      selection-background-color: #444444;
                      selection-color: #FFFFFF;
                    }
                    QWidget::item:selected {
                      background-color: #1464A0;
                    }
                    QWidget::item:hover {
                      background-color: #148CD2;
                      color: #32414B;
                    }
                    QCalendarWidget {
                      border: 1px solid #32414B;
                      border-radius: 4px;
                    }""",
    "line_edit":"""QLineEdit {
                        border-top-right-radius: 0px;
                        border-bottom-right-radius: 0px;
                    }"""}
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
            urllib.request.urlretrieve(fr"{GITHUB_LINK}/{VERSION}/{name}", name)
        except urllib.error.HTTPError:
            urllib.request.urlretrieve(fr"{GITHUB_LINK}/master/{name}", name)
    else:
        try:
            with urllib.request.urlopen(fr"{GITHUB_LINK}/{VERSION}/{name}") as ur:
                return ur.read().decode()
        except urllib.error.HTTPError:
            with urllib.request.urlopen(fr"{GITHUB_LINK}/master/{name}") as ur:
                return ur.read().decode()

class frontEnd:
    """## GUI de l'application, s'occupe de montrer à l'utilisateur les options possibles

    ### Méthodes:\n
        \t__init__ -- Prépare l'environnement de travail selon le mode DEBUG
        \texecuteGUI -- Génère et lance le GUI
    """
    def __init__(self):
        """## Prépare l'environnement de travail selon le mode DEBUG"""
        # Crée une application vide
        self.app = QApplication([])
        # Change les opérations selon le mode DEBUG
        if DEBUG:
            # Vérifie que le fichier a le format approprié
            if not FILES["debug"].endswith(".ui"):
                raise FileNotFoundError
            # Vérifie si le fichier existe sinon le télécharge en ligne
            if not os.path.isfile(FILES["debug"]):
                downloadData(FILES["debug"])
            
            # Sauvegarde les paramètres du fichier FILES["debug"]
            self.Ui, self.Window = uic.loadUiType(FILES["debug"])
            
            # Crée des instances de la fenêtre générée avec le fichier FILES["debug"]
            self.window = self.Window()
            self.ui = self.Ui()
        else:
            # Vérifie que le fichier a le format approprié
            if not FILES["debug"].endswith(".py"):
                raise FileNotFoundError
            # Vérifie si le fichier existe sinon le télécharge en ligne
            if not os.path.isfile(FILES["pyuic5"]):
                downloadData(FILES["pyuic5"])
            
            # Importe les paramètres du fichier FILES["pyuic5"]
            import pyet_ui

             # Crée des instances de la fenêtre générée avec le fichier FILES["pyuic5"]
            self.window = QtWidgets.QMainWindow()
            self.ui = pyet_ui.Ui_MainWindow()
        
        # Associe le design à l'interface graphique
        self.ui.setupUi(self.window)
        # Spécifie l'apparence générale universelle de l'interface
        self.app.setStyle("Fusion")
        
    def executeGUI(self):
        """## Génère et lance le GUI"""
        # Vérifie si c'est la première fois que le programme est exécuté
        self.firstLaunch()

        # Mise en place de l'onglet de configuration
        self.configTab()
        # Mise en place de l'onglet d'information
        self.aboutTab()

        # Assigne le nom de la fenêtre
        self.window.setWindowTitle("pyÉtude - v" + VERSION)
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
            "Physique": ["PHY", ""]
            }
        # Vérifie si la configuration a déjà été faite
        if os.path.isfile(os.path.join("./", FILES["config"])):
            # Active l'onglet du générateur
            self.ui.tabWidget.setTabEnabled(0, True)
            self.ui.tabWidget.setTabToolTip(0, "Créer un document")
            self.ui.tabWidget.setCurrentIndex(0)
            self.ui.matieresConfig.setChecked(True)

            # Lit le document de configuration et assigne:
            # self.auteur, self.niveau, self.matieres
            self.readJSON()
            # Asssigne les matières selon le fichier de configuration dans le tableau
            self.setMatieres(self.matieres)

            # Met le nom de l'auteur et du niveau selon le fichier de configuration
            self.ui.auteurLineEdit.setText(self.auteur)
            self.ui.niveauLineEdit.setText(self.niveau)
        
            # Configuration terminée, met en place l'onglet de génération
            self.genTab()
        else:
            assert FileNotFoundError
            # Empêche l'accès au générateur
            self.ui.tabWidget.setTabEnabled(0, False)
            self.ui.tabWidget.setTabToolTip(0, "Veuillez utilisez le Configurateur")
            self.ui.tabWidget.setCurrentIndex(1)
            
            # Assigne les matières par défaut dans le tableau
            self.setMatieres(self.matieresDefault)

    def setMatieres(self, datadict:dict):
        """## Insère le dictionnaire donné dans le tableau self.ui.matiereTableWidget
        
        ### Arguments:\n
            \tdatadict {dict} -- Dictionnaire des matières
        """
        # Supprime toutes les anciennes rangées
        for i in range(0,self.ui.matiereTableWidget.rowCount()+1):  
            self.ui.matiereTableWidget.removeRow(self.ui.matiereTableWidget.rowCount()-1)
        # Insère les données du dictionnaire dans le tableau
        for i, key in enumerate(sorted(datadict, key=locale.strxfrm)):  
            self.ui.matiereTableWidget.insertRow(self.ui.matiereTableWidget.rowCount())
            self.ui.matiereTableWidget.setItem(i, 0, QTableWidgetItem(key))
            self.ui.matiereTableWidget.setItem(i, 1, QTableWidgetItem(datadict[key][0]))
            self.ui.matiereTableWidget.setItem(i, 2, QTableWidgetItem(datadict[key][1]))
    
    def readJSON(self):
        """## Lit le fichier de configuration .json et lui attribue les informations contenues"""
        # Prends le dictionnaire du fichier de configuration
        with open(FILES["config"]) as json_f:
            jsonData = json.load(json_f)
        # Attribue l'auteur et le niveau
        self.auteur = jsonData["auteur"]
        self.niveau = jsonData["niveau"]
        # Vérifie si des matières personnalisées exsitent
        if not jsonData["matieres"]:
            self.matieres = self.matieresDefault
        else:
            self.matieres = jsonData["matieres"]

    def genTab(self):
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
        for le in (self.ui.matLineEdit, self.ui.numLineEdit, self.ui.sectionLineEdit, self.ui.soustitreLineEdit, self.ui.titreLineEdit):
            self.esperLimit(le)
        
        # Mise en place de l'emplacement de sauvegarde
        self.pathGenTab()

        # Connection du bouton 'Générer' à sa fonction
        self.ui.genPushButton.pressed.connect(self.createDocument)
    
    def getLineEditValue(self, lineedit):
        value = lineedit.text()
        if value == "":
            value = lineedit.placeholderText()
        
        return value

    def createDocument(self):
        self.titre = self.getLineEditValue(self.ui.titreLineEdit)
        self.soustitre = self.getLineEditValue(self.ui.soustitreLineEdit)
        self.section = self.getLineEditValue(self.ui.sectionLineEdit)
        
        self.model = "model.docx"
        if not os.path.isfile(self.model):
            modelMessageBox = QMessageBox()
            modelMessageBox.setIcon(QMessageBox.Information)
            modelMessageBox.setWindowTitle(f"pyÉtude - {VERSION} - Modèle")
            modelMessageBox.setText(f"Le modèle: {self.model} n'a pas été trouvé.\nIl sera téléchargé automatiquement.")
            modelMessageBox.addButton(QMessageBox.Ok)
            modelMessageBox.exec_()
            downloadData(self.model)
        
        if os.path.isfile(self.filepaths[2]):
            assert FileExistsError

            numMatMessageBox = QMessageBox()
            numMatMessageBox.setIcon(QMessageBox.Information)
            numMatMessageBox.setWindowTitle(f"pyÉtude - {VERSION} - Fichier Existant Trouvé")
            numMatMessageBox.setStyleSheet(STYLES["message_box"])
            numMatMessageBox.setText(f"pyÉtude a trouvé un fichier ayant le même nom.\nSouhaitez-vous écraser le fichier actuel?\n\n*ATTENTION CETTE ACTION EST IRRÉVERSIBLE*\n\nFichier qui sera écrasé: {self.filepaths[2]}")
            buttonOpen = numMatMessageBox.addButton(QMessageBox.Yes)
            buttonOpen.setText("Oui")
            buttonIgnore = numMatMessageBox.addButton(QMessageBox.No)
            buttonIgnore.setText("Non")
            numMatMessageBox.exec_()

            if numMatMessageBox.clickedButton().text() == "Non":
                return ConnectionAbortedError
        Document(self.titre, self.soustitre, self.auteur, self.niveau,
                            self.matiere, self.numero, self.section,
                            self.model, self.filepaths[2])
        

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
        
        self.matiere = "PHY"

        matMenu = QMenu("matMenu")
        matMenu.triggered.connect(isChecked)
        self.ui.matToolButton.setMenu(matMenu)
        matActionGroup = QActionGroup(matMenu)
        matActionGroup.setExclusive(True)

        matMenu.setStyleSheet(STYLES["menu"])

        for mat in sorted(self.matieres, key=locale.strxfrm):
            matMenu.addAction(matActionGroup.addAction(QAction(f"{mat}", checkable=True)))

        matMenu.addSeparator()
        personalizeMatAction = matActionGroup.addAction(QAction("Personnaliser", checkable=True))
        matMenu.addAction(personalizeMatAction)

        self.customMatName = False
        self.filepaths = [".", "PHY-0624.docx", os.path.join(".","PHY-0624.docx")]
        self.defaultFilePaths = self.filepaths
        self.defaultFilePathChanged()

        self.ui.matLineEdit.textChanged.connect(self.checkNumMat)

    def checkNumMat(self, connection="", prefix="CHP"):
        def findFiles(prefix):
            self.matiere = self.getLineEditValue(self.ui.matLineEdit).translate({ord(i): None for i in '\\/:*?"<>|'})
            matpath = self.checkCustomMatNamePath()
            matched_files = []
            for filename in [f for f in os.listdir(matpath) if os.path.isfile(os.path.join(matpath, f))]:  # Does not look in other folders
                if filename.startswith(f"{self.matiere}-{prefix}") and filename.endswith(".docx"):
                        matched_files.append(filename)
            return matched_files
        
        matched_files = findFiles(prefix)
        if matched_files == [] and connection != "":
            prefix = "MOD"
            matched_files = findFiles(prefix)
        
        if matched_files:
            new_suggested_file = int(max(matched_files).replace(f"{self.matiere}-{prefix}", "").replace(".docx", "")) + 1
            
            numMatMessageBox = QMessageBox()
            numMatMessageBox.setIcon(QMessageBox.Information)
            numMatMessageBox.setWindowTitle(f"pyÉtude - {VERSION} - Fichiers Trouvés")
            numMatMessageBox.setStyleSheet(STYLES["message_box"])
            numMatMessageBox.setText(f"pyÉtude a trouvé des documents existants pour cette matière.\nSouhaitez-vous poursuivre la numérotation trouvée?\n\n\tNouveau fichier: {self.matiere}-{prefix}{new_suggested_file}")
            buttonOpen = numMatMessageBox.addButton(QMessageBox.Yes)
            buttonOpen.setText("Oui")
            buttonIgnore = numMatMessageBox.addButton(QMessageBox.No)
            buttonIgnore.setText("Non")
            numMatMessageBox.exec_()
            if numMatMessageBox.clickedButton().text() == "Oui":
                self.ui.numLineEdit.setEnabled(False)
                self.ui.numLineEdit.setText(f"{prefix}{new_suggested_file}")
            else:
                assert ConnectionRefusedError
        
        self.defaultFilePathChanged()
    
    def checkCustomMatNamePath(self):
        if self.customMatName:
            return os.getcwd()
        else:
            for mat in self.matieres.values():
                if mat[0] == self.matiere:
                    if mat[1] == "":  # S'il n'y a aucun chemin perso pour cette matière
                        return os.getcwd()  # Overwrite le chemin perso par le chemin actuel
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
                self.checkNumMat(None, selection.text()[:3])
        
        def calendarView():
            self.ui.numLineEdit.setEnabled(False)
            calendarView = QDialog()
            calendarView.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.MSWindowsFixedSizeDialogHint | QtCore.Qt.WindowMinimizeButtonHint)

            calendar = QCalendarWidget(calendarView)
            calendar.setGeometry(QtCore.QRect(0, 0, 312, 183))
            calendar.setFirstDayOfWeek(QtCore.Qt.Monday)
            calendar.setGridVisible(True)
            calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
            calendar.setObjectName("numCalendarWidget")

            calendarView.setStyleSheet(STYLES["calendar"])

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
        
        numMenu = QMenu("numMenu")
        numMenu.triggered.connect(isChecked)
        self.ui.numToolButton.setMenu(numMenu)
        numActionGroup = QActionGroup(numMenu)
        numActionGroup.setExclusive(True)

        numMenu.setStyleSheet(STYLES["menu"])
        
        chapterButton = numMenu.addMenu("Chapitre")
        moduleButton = numMenu.addMenu("Module")
        for short, button in {"CHP":chapterButton, "MOD":moduleButton}.items():
            for i in range(20):
                button.addAction(numActionGroup.addAction(QAction(f"{short}{str(i)}", checkable=True)))
        
        calendarAction = numActionGroup.addAction(QAction("Choisir une date", checkable=True))
        numMenu.addAction(calendarAction)
        numMenu.addSeparator()

        autoNumAction = numActionGroup.addAction(QAction("Automatique", checkable=True))
        numMenu.addAction(autoNumAction)

        personalizeNumAction = numActionGroup.addAction(QAction("Personnaliser", checkable=True))
        numMenu.addAction(personalizeNumAction)

        self.ui.numLineEdit.textChanged.connect(self.defaultFilePathChanged)
    
    def defaultFilePathChanged(self):
        self.matiere = self.getLineEditValue(self.ui.matLineEdit).translate({ord(i): None for i in '\\/:*?"<>|'})

        self.numero = self.getLineEditValue(self.ui.numLineEdit).translate({ord(i): None for i in '\\/:*?"<>|'})
        
        matpath = self.checkCustomMatNamePath()
        self.defaultFilePaths = [matpath, f"{self.matiere}-{self.numero}.docx", os.path.join(matpath, f"{self.matiere}-{self.numero}.docx")] # Chemin, fichier, chemin complet

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
                    os.system(fr'open {self.filepaths[0]}')
            
            elif selection.text() == customPathAction.text():
                getSaveFilePath = QFileDialog()
                getSaveFilePath.setNameFilters(["Microsoft Word (*.docx)"])
                getSaveFilePath.setAcceptMode(QFileDialog.AcceptSave)
                getSaveFilePath.exec_()
                if getSaveFilePath.selectedFiles() != []:
                    self.filepaths = [getSaveFilePath.directory().path(), getSaveFilePath.selectedFiles()[0].replace(getSaveFilePath.directory().path(), ""),getSaveFilePath.selectedFiles()[0]]
            elif selection.text() == customDirectoryAction.text():
                filepath = QFileDialog.getExistingDirectory()
                if filepath != "":
                    self.filepaths = [filepath, f"/{self.matiere}-{self.numero}.docx", os.path.join(filepath, f"{self.matiere}-{self.numero}.docx")]
            
            elif selection.text() == defaultPathAction.text():
                self.filepaths = self.defaultFilePaths
            self.updatePathLabel()
        
        def QLActivated():
            pathMenu.exec(self.ui.pathPathLabel.mapToGlobal(QtCore.QPoint(0, self.ui.pathPathLabel.geometry().height())))
        pathMenu = QMenu("pathMenu")
        pathMenu.triggered.connect(isChecked)
        pathActionGroup = QActionGroup(pathMenu)

        pathMenu.setStyleSheet(STYLES["menu"])

        self.ui.pathPathLabel.linkActivated.connect(QLActivated)

        openPathAction = pathActionGroup.addAction(QAction("Ouvrir le dossier sélectionné"))
        pathMenu.addAction(openPathAction)
        pathMenu.addSeparator()

        customPathAction = pathActionGroup.addAction(QAction("Enregistrer sous..."))
        pathMenu.addAction(customPathAction)

        customDirectoryAction = pathActionGroup.addAction(QAction("Choisir le dossier de sortie"))
        pathMenu.addAction(customDirectoryAction)
        pathMenu.addSeparator()

        defaultPathAction = pathActionGroup.addAction(QAction("Restaurer la valeur par défaut"))
        pathMenu.addAction(defaultPathAction)

    def updatePathLabel(self):
        fp = self.filepaths[2].replace("/", " > ").replace("\\", " > ")  # Bypass f-string \\ restriction
        self.ui.pathPathLabel.setText(QtCore.QCoreApplication.translate("MainWindow", fr"""<html><head/><body><p><a href="none"><span style=" font-size:11pt; text-decoration: underline; color:\#f0f0f0;">{fp}</span></a></p></body></html>"""))

    def configTab(self):
        def saveVariable():
            if self.ui.auteurLineEdit.text() != "":
                self.auteur = self.ui.auteurLineEdit.text().replace("&","")
            else:
                self.auteur = self.ui.auteurLineEdit.placeholderText().replace("&","")
            
            if self.ui.niveauLineEdit.text() != "":
                self.niveau = self.ui.niveauLineEdit.text().replace("&","")
            else:
                self.niveau = self.ui.niveauLineEdit.placeholderText().replace("&","")
            
            self.matieres = {}

            for row in range(self.ui.matiereTableWidget.rowCount()):
                matiere = self.ui.matiereTableWidget.item(row, 0)
                mat = self.ui.matiereTableWidget.item(row, 1)
                path = self.ui.matiereTableWidget.item(row, 2)
                if matiere != None and mat != None:
                    if matiere.text() != "" and mat.text() != "":
                        if path == None:
                            path_text = ""
                        else:
                            path_text = path.text().replace("&","")
                        self.matieres[matiere.text().replace("&","")] = [mat.text().replace("&",""), path_text]
            writeJSON()
            self.firstLaunch()
        
        def writeJSON():
            json_data = dict()
            json_data["auteur"] = self.auteur
            json_data["niveau"] = self.niveau
            json_data["matieres"] = dict()

            if self.ui.matieresConfig.isChecked() == True:  # Vérifie s'il y a des matières personnalisées
                for key, value in self.matieres.items():
                    json_data["matieres"][key] = value
            
            with open(FILES["config"], "w", encoding="utf-8") as json_f:  # Crée le fichier de configuration
                json.dump(json_data, json_f, sort_keys=True, indent=4)  # Formatte le fichier JSON

        # Empêche l'utilisation des esperluètes "&"
        self.esperLimit(self.ui.auteurLineEdit)
        self.esperLimit(self.ui.niveauLineEdit)

        self.ui.configSaveButton.clicked.connect(saveVariable)

        self.matieresConfig()

    def matieresConfig(self):
        def addRow():
            self.ui.matiereTableWidget.insertRow(self.ui.matiereTableWidget.rowCount())
        def delRow():
            if self.ui.matiereTableWidget.currentRow() == -1:  # if no row is selected
                self.ui.matiereTableWidget.removeRow(self.ui.matiereTableWidget.rowCount()-1)
            else:
                self.ui.matiereTableWidget.removeRow(self.ui.matiereTableWidget.currentRow())
        def resetRows():
            self.setMatieres(self.matieresDefault)
        
        def checkBrowse():
            if self.ui.matiereTableWidget.currentColumn() == 2:
                self.ui.matiereTableBrowse.setEnabled(True)
            else:
                self.ui.matiereTableBrowse.setEnabled(False)
        def browseDirectory():
            if self.ui.matiereTableWidget.currentColumn() == 2:
                filename = QFileDialog.getExistingDirectory()
                self.ui.matiereTableWidget.setItem(self.ui.matiereTableWidget.currentRow(), 2, QTableWidgetItem(filename))

        self.ui.matiereTablePlus.clicked.connect(addRow)
        self.ui.matiereTableMinus.clicked.connect(delRow)
        self.ui.matiereTableReset.clicked.connect(resetRows)

        self.ui.matiereTableBrowse.setEnabled(False)
        self.ui.matiereTableWidget.clicked.connect(checkBrowse)
        self.ui.matiereTableBrowse.clicked.connect(browseDirectory)

    def aboutTab(self):
        self.ui.varVersionLabel.setText(QtCore.QCoreApplication.translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">{VERSION}</span></p></body></html>"))
    
    def esperLimit(self, lineedit):
        lineedit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp(r"[^&\\/]+"), lineedit)) # Empêche l'utilisation des esperluètes "&"


class Document:
    def __init__(self, titre, soustitre, auteur, niveau, matiere, numero, section, model, filepath):
        self.titre = titre
        self.soustitre = soustitre
        self.auteur = auteur
        self.niveau = niveau
        self.matiere = matiere
        self.numero = numero
        self.section = section
        self.model = model
        self.filepath = filepath

        self.options = {"pyETUDE_Titre": titre,
                    "pyETUDE_SousTitre": soustitre,
                    "pyETUDE_Matiere": matiere,
                    "pyETUDE_Auteur": auteur,
                    "pyETUDE_Niv": niveau,
                    "pyETUDE_Num": numero}
        self.sections = {"sectionpy": section}

        self.folder = f"{matiere}-{numero}_tmpyETUDE"

        self.main()

    def main(self):
        self.exportWord(self.model, self.folder)

        self.modifyOptions(os.path.join(self.folder, "word", "document.xml"), self.options)
        self.modifyOptions(os.path.join(self.folder, "word", "header1.xml"), self.options)
        self.modifyOptions(os.path.join(self.folder, "word", "footer1.xml"), self.options)

        self.modifyOptions(os.path.join(self.folder, "word", "document.xml"), self.sections)

        self.packWord(self.folder, self.filepath)
        self.cleanTemp(self.folder)

    def exportWord(self, model:str, folder:str) -> str:
        """## Extract the specified `.zip` file

        ### Arguments:\n
            \tmodel {str} -- file that will be extracted (Do not forget the .docx!)
            \tfolder {str} -- folder that will receive the extracted file

        ### Returns:\n
            \tstr -- the name of the folder where it was extracted
        """

        with zipfile.ZipFile(model, "r") as model_file:
            model_file.extractall(folder)
            model_file.close()
        return folder

    def modifyOptions(self, path:str, info:dict) -> str:
        """## Send command to {self.searchAndReplace} for all values in a dictionnary
        
        ### Arguments:\n
            \tpath {str} -- The path of the file to be modified
            \tinfo {dict} -- A dictionnary in this format {"to search":"to replace"}
        
        ### Returns:\n
            \tstr -- Returns the name of the file modified
        """
        for search, replace in info.items():
            self.searchAndReplace(path, search, replace)
        return path

    def searchAndReplace(self, infile:str, search:str, replace:str) -> str:
        """## Search the specified file with the keyword given and replaces it with the third argument
        
        ### Arguments:\n
            \tinfile {str} -- The file to change
            \tsearch {str} -- The word to replace
            \treplace {str} -- The word that will be replaced by {search}

        ### Returns:\n
            \tstr -- Returns the name of the file modified
        """
        if os.path.isfile(infile):
            with open(infile, "r", encoding="utf8") as in_f:
                data_f = in_f.read()
                with open(infile, "w", encoding='utf8') as out_f:
                    out_f.write(data_f.replace(search, replace))
        else:
            raise FileNotFoundError
        return infile


    def packWord(self, folder:str, final:str) -> str:
        """## Zip the folder specified
        This will only zip the contents of the folder, not the base folder

        ### Arguments:\n
            \tfolder {str} -- the folder that will be zipped
            \tfinal {str} -- the name of the archive (Do not forget the .docx!)

        ### Returns:\n
            \tstr -- the name of the zip file that was created
        """
        locale.setlocale(locale.LC_ALL, (None, None))  # Fix compatibility with locale
        with zipfile.ZipFile(final, "w", compression=zipfile.ZIP_DEFLATED) as zip_file:
            for root, dirs, files in os.walk(folder):  # pylint: disable=unused-variable
                # zip_file.write(os.path.join(root, "."))

                for File in files:
                    filePath = os.path.join(root, File)
                    inZipPath = filePath.replace(folder, "", 1).lstrip("\\/")
                    zip_file.write(filePath, inZipPath)
        print(f"\nLe document a été créé: {self.filepath}")  # Si démarré à partir de l'invite de commande
        
        docMessageBox = QMessageBox()
        docMessageBox.setIcon(QMessageBox.Information)
        docMessageBox.setWindowTitle(f"pyÉtude - {VERSION} - Document généré")

        docMessageBox.setStyleSheet(STYLES["message_box"])


        docMessageBox.setText(f"Le document a été créé:\n{self.filepath}\n\nVoulez-vous l'ouvrir?")

        buttonOpen = docMessageBox.addButton(QMessageBox.Open)
        buttonOpen.setText("Ouvrir le fichier")

        buttonIgnore = docMessageBox.addButton(QMessageBox.No)
        buttonIgnore.setText("Non")

        docMessageBox.exec_()

        if docMessageBox.clickedButton().text() == "Ouvrir le fichier":
            if sys.platform == "win32":
                    try:
                        os.startfile(self.filepath)
                    except:
                        pass
            else:
                os.system(fr'open {self.filepath}')
        else:
            assert ConnectionRefusedError

        return final

    def cleanTemp(self, folder:str) -> str:
        """## Clean the temporary folder
        DANGEROUS: THIS WILL DELETE ALL THE FILES IN THE SPECIFIED FOLDER!!
        
        ### Arguments:\n
            \tfolder {str} -- The folder that will be deleted
        
        ### Raises:\n
            \tNotADirectoryError: The specified folder is not a folder
        
        ### Returns:\n
            \tstr -- Returns the name of the folder deleted
        """
        if os.path.isdir(folder):
            for root, dirs, files in os.walk(folder, topdown=False):
                for File in files:
                    os.remove(os.path.join(root, File))
                for Dir in dirs:
                    os.rmdir(os.path.join(root, Dir))
            os.rmdir(folder)
        else:
            raise NotADirectoryError
        
        return folder


if __name__ == "__main__":
    fe = frontEnd()
    fe.executeGUI()