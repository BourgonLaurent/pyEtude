# -*- coding: utf-8 -*-
"""
                 ███████╗████████╗██╗   ██╗██████╗ ███████╗
                 ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝
██████╗ ██╗   ██╗█████╗     ██║   ██║   ██║██║  ██║█████╗  
██╔══██╗╚██╗ ██╔╝██╔══╝     ██║   ██║   ██║██║  ██║██╔══╝  
██████╔╝ ╚████╔╝ ███████╗   ██║   ╚██████╔╝██████╔╝███████╗
██╔═══╝   ╚██╔╝  ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
██║        ██║   MIT © Laurent Bourgon 2019
╚═╝        ╚═╝   
"""
import json, locale, os, sys, zipfile, urllib.request, urllib.error
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *

os.chdir(os.path.realpath(__file__).replace(os.path.basename(__file__), ""))  # Accède aux fichiers depuis la racine du programme, et non l'endroit du shell

try:
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
except:
    assert EnvironmentError
    locale.setlocale(locale.LC_ALL, (None, None))

VERSION = r"2.2.0"
DEBUG = False


class frontEnd:
    def __init__(self):
        if DEBUG:
            if not os.path.isfile("pyEtude.ui"):
                self.downloadData("pyEtude.ui")
            self.Ui, self.Window = uic.loadUiType("pyEtude.ui")
            self.app = QApplication([])
            self.window = self.Window()
            self.ui = self.Ui()
        else:
            if not os.path.isfile("pyet_ui.py"):
                self.downloadData("pyet_ui.py")
            import pyet_ui
            self.app = QApplication([])
            self.window = QtWidgets.QMainWindow()
            self.ui = pyet_ui.Ui_MainWindow()
            
        self.ui.setupUi(self.window)
        self.app.setStyle("Fusion")

        self.firstLaunch()
        
        if self.configDone:
            self.genTab()
        self.configTab()
        self.aboutTab()

        self.window.setWindowTitle("pyÉtude - v" + VERSION)
        self.window.show()
        self.app.exec_()
    
    def downloadData(self, name, create=True):
        """## Télécharge un fichier du répertoire GitHub raw
        
        ### Arguments:\n
            \tname {str} -- Nom du fichier à prendre
        ### Keyword Arguments:\n
            \tcreate {bool} -- Crée un fichier (default: {True})
        
        ### Returns:\n
            \t[str] -- (Seulement si create=False): données décodées qui ont été prises
        """
        if create:
            try:
                urllib.request.urlretrieve(fr"https://raw.githubusercontent.com/BourgonLaurent/pyEtude/{VERSION}/{name}", name)
            except urllib.error.HTTPError:
                urllib.request.urlretrieve(fr"https://raw.githubusercontent.com/BourgonLaurent/pyEtude/master/{name}", name)
        else:
            try:
                with urllib.request.urlopen(fr"https://raw.githubusercontent.com/BourgonLaurent/pyEtude/{VERSION}/{name}") as ur:
                    return ur.read().decode()
            except urllib.error.HTTPError:
                with urllib.request.urlopen(fr"https://raw.githubusercontent.com/BourgonLaurent/pyEtude/master/{name}") as ur:
                    return ur.read().decode()

    def firstLaunch(self):
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
        if os.path.isfile("./pyEtude.json"):
            self.configDone = True
            # Donne accès au générateur
            self.ui.tabWidget.setTabEnabled(0, True)
            self.ui.tabWidget.setTabToolTip(0, "Créer un document")
            self.ui.tabWidget.setCurrentIndex(0)
            self.ui.matieresConfig.setChecked(True)
            self.readJSON()
            self.ui.auteurLineEdit.setText(self.auteur)
            self.ui.secLineEdit.setText(self.sec)
            self.genTab()
        else:
            assert FileNotFoundError
            # Empêche l'accès au générateur
            self.ui.tabWidget.setTabEnabled(0, False)
            self.ui.tabWidget.setTabToolTip(0, "Veuillez utilisez le Configurateur")
            self.ui.tabWidget.setCurrentIndex(1)
            self.setMatieres(self.matieresDefault)
            self.configDone = False

    def setMatieres(self, datadict):
        for i in range(0,self.ui.matiereTableWidget.rowCount()+1):  # Enlève les vieilles données
            self.ui.matiereTableWidget.removeRow(self.ui.matiereTableWidget.rowCount()-1)
        for i, key in enumerate(sorted(datadict, key=locale.strxfrm)):  # met les données du dictionnaire
            self.ui.matiereTableWidget.insertRow(self.ui.matiereTableWidget.rowCount())
            self.ui.matiereTableWidget.setItem(i, 0, QTableWidgetItem(key))
            self.ui.matiereTableWidget.setItem(i, 1, QTableWidgetItem(datadict[key][0]))
            self.ui.matiereTableWidget.setItem(i, 2, QTableWidgetItem(datadict[key][1]))
    
    def readJSON(self):
        with open("pyEtude.json") as json_f:
            jsonData = json.load(json_f)
        
        self.auteur = jsonData["auteur"]
        self.sec = jsonData["secondaire"]
        if not jsonData["matieres"]:
            self.matieres = self.matieresDefault
            self.setMatieres(self.matieresDefault)
        else:
            self.matieres = jsonData["matieres"]
            self.setMatieres(self.matieres)

    def genTab(self):
        self.matGenTab()
        self.numGenTab()

        self.ui.auteurPersoLabel.setText(self.auteur)
        self.ui.secPersoLabel.setText(self.sec)
        for le in (self.ui.matLineEdit, self.ui.numLineEdit, self.ui.sectionLineEdit, self.ui.soustitreLineEdit, self.ui.titreLineEdit):
            self.esperLimit(le)
        
        self.pathGenTab()

        self.createdOnce = False
        self.ui.genPushButton.pressed.connect(self.createDocument)
    
    def createDocument(self):
        if not self.createdOnce:
            def getValue(lineedit):
                value = lineedit.text()
                if value == "":
                    value = lineedit.placeholderText()
                return value

            self.titre = getValue(self.ui.titreLineEdit)
            self.soustitre = getValue(self.ui.soustitreLineEdit)
            self.section = getValue(self.ui.sectionLineEdit)
            
            self.model = "model.docx"

            if not os.path.isfile(self.model):
                modelMessageBox = QMessageBox()
                modelMessageBox.setIcon(QMessageBox.Information)
                modelMessageBox.setWindowTitle(f"pyÉtude - {VERSION} - Modèle")

                modelMessageBox.setText(f"Le model: {self.model} n'a pas été trouvé.\nIl sera téléchargé automatiquement.")
                modelMessageBox.addButton(QMessageBox.Ok)
                modelMessageBox.exec_()

                self.downloadData(self.model)
            
            Document(self.titre, self.soustitre, self.auteur, self.sec,
            self.matiere, self.numero, self.section, self.model, self.filepaths[2])
            self.createdOnce = True
        else:
            self.createdOnce = False

    def matGenTab(self):
        self.matiere = "PHY"
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
                # self.defaultFilePathChanged()
        
        matMenu = QMenu("matMenu")
        matMenu.triggered.connect(isChecked)
        self.ui.matToolButton.setMenu(matMenu)
        matActionGroup = QActionGroup(matMenu, exclusive=True)

        matMenu.setStyleSheet("""QMenu {
                              border: 0.5px solid #787878;
                              color: #F0F0F0;
                              margin: 0px;
                            }
                            QMenu::separator {
                              height: 1px;
                              background-color: #505F69;
                            }
                            QMenu::item {
                              background-color: #32414B;
                              padding: 4px 0px 4px 24px;
                              /* Reserve space for selection border */
                              border: 1px transparent #32414B;
                            }
                            QMenu::item:selected {
                              color: #F0F0F0;
                              background-color: #505F69;
                            }""")

        for mat in sorted(self.matieres, key=locale.strxfrm):
            matMenu.addAction(matActionGroup.addAction(QAction(f"{mat}", checkable=True)))

        matMenu.addSeparator()
        personalizeMatAction = matActionGroup.addAction(QAction("Personnaliser", checkable=True))
        matMenu.addAction(personalizeMatAction)

        self.customMatName = False
        self.filepaths = [".", "/PHY-0920.docx", "./PHY-0920.docx"]
        self.defaultFilePaths = self.filepaths
        self.defaultFilePathChanged()

        self.ui.matLineEdit.textChanged.connect(self.defaultFilePathChanged)

    def numGenTab(self):
        self.numero = "0920"
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
        
        def calendarView():
            self.ui.numLineEdit.setEnabled(False)
            calendarView = QDialog()

            calendar = QCalendarWidget(calendarView)
            calendar.setGeometry(QtCore.QRect(0, 0, 312, 183))
            calendar.setFirstDayOfWeek(QtCore.Qt.Monday)
            calendar.setGridVisible(True)
            calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
            calendar.setObjectName("numCalendarWidget")
            calendarView.setStyleSheet("""
                                    QAbstractItemView {
                                      alternate-background-color: #19232D;
                                      color: #F0F0F0;
                                      border: 1px solid #32414B;
                                      border-radius: 4px;
                                    }
                                    QWidget {
                                      background-color: #19232D;
                                      border: 0px solid #32414B;
                                      padding: 0px;
                                      color: #F0F0F0;
                                      selection-background-color: #1464A0;
                                      selection-color: #F0F0F0;
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
                                    }
                                    QCalendarWidget QAbstractItemView:disabled {
                                      color: #787878;
                                    }""")
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
        numActionGroup = QActionGroup(numMenu, exclusive=True)
        # numMenu.move(0, 0)  # numMenu.mapToGlobal(QtCore.QPoint(0, self.ui.numToolButton.geometry().height()))

        numMenu.setStyleSheet("""QMenu {
                              border: 0.5px solid #787878;
                              color: #F0F0F0;
                              margin: 0px;
                            }
                            QMenu::separator {
                              height: 1px;
                              background-color: #505F69;
                            }
                            QMenu::item {
                              background-color: #32414B;
                              padding: 4px 0px 4px 24px;
                              /* Reserve space for selection border */
                              border: 1px transparent #32414B;
                            }
                            QMenu::item:selected {
                              color: #F0F0F0;
                              background-color: #505F69;
                            }""")
        
        chapterButton = numMenu.addMenu("Chapitre")
        for i in range(20):
            chapterButton.addAction(numActionGroup.addAction(QAction(f"CHP{str(i)}", checkable=True)))
        
        calendarAction = numActionGroup.addAction(QAction("Choisir une date", checkable=True))
        numMenu.addAction(calendarAction)
        numMenu.addSeparator()

        personalizeNumAction = numActionGroup.addAction(QAction("Personnaliser", checkable=True))
        numMenu.addAction(personalizeNumAction)

        self.ui.numLineEdit.textChanged.connect(self.defaultFilePathChanged)
    
    def defaultFilePathChanged(self):
        self.matiere = self.ui.matLineEdit.text().translate({ord(i): None for i in '\\/:*?"<>|'})
        if self.matiere == "":
            self.matiere = self.ui.matLineEdit.placeholderText()

        self.numero = self.ui.numLineEdit.text().translate({ord(i): None for i in '\\/:*?"<>|'})
        if self.numero == "":
            self.numero = self.ui.numLineEdit.placeholderText()
        
        if self.customMatName:
            self.defaultFilePaths = [os.getcwd(), f"{self.matiere}-{self.numero}.docx", f"{os.getcwd()}/{self.matiere}-{self.numero}.docx"]
        else:
            for mat in self.matieres.values():
                if mat[0] == self.matiere:
                    if mat[1] == "":
                        mat[1] = os.getcwd()
                    self.defaultFilePaths = [mat[1], f"/{self.matiere}-{self.numero}.docx", f"{mat[1]}/{self.matiere}-{self.numero}.docx"]

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
                    self.filepaths = [filepath, f"/{self.matiere}-{self.numero}.docx", f"{filepath}/{self.matiere}-{self.numero}.docx"]
            
            elif selection.text() == defaultPathAction.text():
                self.filepaths = self.defaultFilePaths
            pathMenu.setVisible(False)
            self.updatePathLabel()
        
        def QLActivated():
            if not self.pathRanOnce:
                pathMenu.exec(self.ui.pathPathLabel.mapToGlobal(QtCore.QPoint(0, self.ui.pathPathLabel.geometry().height())))
                self.pathRanOnce = True
            else:
                self.pathRanOnce = False
        pathMenu = QMenu("pathMenu")
        pathMenu.triggered.connect(isChecked)
        pathActionGroup = QActionGroup(pathMenu)

        pathMenu.setStyleSheet("""QMenu {
                              border: 0.5px solid #787878;
                              color: #F0F0F0;
                              margin: 0px;
                            }
                            QMenu::separator {
                              height: 1px;
                              background-color: #505F69;
                            }
                            QMenu::item {
                              background-color: #32414B;
                              padding: 4px 10px 4px 24px;
                              /* Reserve space for selection border */
                              border: 1px transparent #32414B;
                            }
                            QMenu::item:selected {
                              color: #F0F0F0;
                              background-color: #505F69;
                            }""")

        self.pathRanOnce = False
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
        # self.ui.pathPathLabel.setText(self.filepaths[2].replace("/", " > ").replace("\\", " > "))
        fp = self.filepaths[2].replace("/", " > ").replace("\\", " > ")
        self.ui.pathPathLabel.setText(QtCore.QCoreApplication.translate("MainWindow", fr"""<html><head/><body><p><a href="none"><span style=" font-size:11pt; text-decoration: underline; color:\#f0f0f0;">{fp}</span></a></p></body></html>"""))

    def configTab(self):
        def saveVariable():
            if self.ui.auteurLineEdit.text() != "":
                self.auteur = self.ui.auteurLineEdit.text().replace("&","")
            else:
                self.auteur = self.ui.auteurLineEdit.placeholderText().replace("&","")
            
            if self.ui.secLineEdit.text() != "":
                self.sec = self.ui.secLineEdit.text().replace("&","")
            else:
                self.sec = self.ui.secLineEdit.placeholderText().replace("&","")
            
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
            json_data["secondaire"] = self.sec
            json_data["matieres"] = dict()

            if self.ui.matieresConfig.isChecked() == True:  # Vérifie s'il y a des matières personnalisées
                for key, value in self.matieres.items():
                    json_data["matieres"][key] = value
            
            with open("pyEtude.json", "w", encoding="utf-8") as json_f:  # Crée le fichier de configuration
                json.dump(json_data, json_f, sort_keys=True, indent=4)  # Formatte le fichier JSON

        # Empêche l'utilisation des esperluètes "&"
        self.esperLimit(self.ui.auteurLineEdit)
        self.esperLimit(self.ui.secLineEdit)

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
    def __init__(self, titre, soustitre, auteur, secondaire, matiere, numero, section, model, filepath):
        self.titre = titre
        self.soustitre = soustitre
        self.auteur = auteur
        self.secondaire = secondaire
        self.matiere = matiere
        self.numero = numero
        self.section = section
        self.model = model
        self.filepath = filepath

        self.options = {"pyETUDE_Titre": titre,
                    "pyETUDE_SousTitre": soustitre,
                    "pyETUDE_Matiere": matiere,
                    "pyETUDE_Auteur": auteur,
                    "pyETUDE_Sec": secondaire,
                    "pyETUDE_Num": numero}
        self.sections = {"sectionpy": section}

        self.folder = f"{matiere}-{numero}_tmpyETUDE"

        self.main()

    def main(self):
        self.exportWord(self.model, self.folder)

        # self.modifyOptions(os.path.join(self.folder, "docProps", "core.xml"), self.options)
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
        with zipfile.ZipFile(final, "w") as zip_file:
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

        docMessageBox.setText(f"Le document a été créé: {self.filepath}\n\nVoulez-vous l'ouvrir?")

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