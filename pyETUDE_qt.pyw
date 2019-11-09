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
import json, locale, os, re, sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *

os.chdir(os.path.realpath(__file__).replace(os.path.basename(__file__), ""))  # Accède aux fichiers depuis la racine du programme, et non l'endroit du shell

try:
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
except:
    assert EnvironmentError
    locale.setlocale(locale.LC_ALL, (None, None))

VERSION = r"2.1.0~b5"
DEBUG = True

class frontEnd:
    def __init__(self):
        if DEBUG:
            self.Ui, self.Window = uic.loadUiType("pyEtude.ui")
            self.app = QApplication([])
            self.window = self.Window()
            self.ui = self.Ui()
            self.ui.setupUi(self.window)
        else:
            import pyet_ui
            self.app = QApplication([])
            self.window = QtWidgets.QMainWindow()
            self.ui = pyet_ui.Ui_MainWindow()
            self.ui.setupUi(self.window)


        self.firstLaunch()
        
        if self.configDone:
            self.genTab()
        self.configTab()
        self.aboutTab()

        self.window.setWindowTitle("pyÉtude - v" + VERSION)
        self.window.show()
        self.app.exec_()
    
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
            self.ui.matieresPersoCheckBox.setChecked(True)
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
    
    def matGenTab(self):
        def isChecked(selection):
            if selection.text() == "Personnaliser":
                self.ui.matLineEdit.setEnabled(True)
                self.ui.matLineEdit.clear()
                self.ui.matLineEdit.setFocus()
            else:
                self.ui.matLineEdit.setEnabled(False)
                self.ui.matLineEdit.setText(self.matieres[selection.text()][0])
        
        matMenu = QMenu("matMenu")
        matMenu.triggered.connect(isChecked)
        self.ui.matToolButton.setMenu(matMenu)
        matActionGroup = QActionGroup(matMenu, exclusive=True)

        for mat in sorted(self.matieres, key=locale.strxfrm):
            matMenu.addAction(matActionGroup.addAction(QAction(f"{mat}", checkable=True)))

        matMenu.addSeparator()
        personalizeMatAction = matActionGroup.addAction(QAction("Personnaliser", checkable=True))
        matMenu.addAction(personalizeMatAction)

    def numGenTab(self):
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
        
        chapterButton = numMenu.addMenu("Chapitre")
        for i in range(20):
            chapterButton.addAction(numActionGroup.addAction(QAction(f"CHP{str(i)}", checkable=True)))
        
        calendarAction = numActionGroup.addAction(QAction("Choisir une date", checkable=True))
        numMenu.addAction(calendarAction)
        numMenu.addSeparator()

        personalizeNumAction = numActionGroup.addAction(QAction("Personnaliser", checkable=True))
        numMenu.addAction(personalizeNumAction)

    def pathGenTab(self):
        def mPEvent(QMEvent):
            pathMenu.move(self.ui.pathPathLabel.mapToGlobal(QtCore.QPoint(0, 12)) + QMEvent.pos())
            pathMenu.show()
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
                if getSaveFilePath.selectedFiles() != "":
                    self.filepaths = [getSaveFilePath.directory().path(), getSaveFilePath.selectedFiles()[0]]
            
            elif selection.text() == customDirectoryAction.text():
                filepath = QFileDialog.getExistingDirectory()
                if filepath != "":
                    self.filepaths = [filepath, filepath + "/" + self.filename]
            
            elif selection.text() == defaultPathAction.text():
                self.filepaths = self.defaultFilePaths
            
            self.updatePathLabel()
        
        pathMenu = QMenu("pathMenu")
        pathMenu.triggered.connect(isChecked)
        pathActionGroup = QActionGroup(pathMenu)
        self.ui.pathPathLabel.mousePressEvent = mPEvent
        self.filename = "CHP-3.docx"
        self.filepaths = ["Aucun chemin de sauvegarde", "Aucun chemin de sauvegarde"]
        self.defaultFilePaths = self.filepaths

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
        self.ui.pathPathLabel.setText(self.filepaths[1])

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
                if matiere != None and mat != None and path != None:
                    if matiere.text() != "" and mat.text() != "":
                        self.matieres[matiere.text().replace("&","")] = [mat.text().replace("&",""), path.text().replace("&","")]
            writeJSON()
            self.firstLaunch()
        
        def writeJSON():
            json_data = dict()
            json_data["auteur"] = self.auteur
            json_data["secondaire"] = self.sec
            json_data["matieres"] = dict()

            if self.ui.matieresPersoCheckBox.isChecked() == True:  # Vérifie s'il y a des matières personnalisées
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
            self.ui.matiereTableWidget.removeRow(self.ui.matiereTableWidget.rowCount()-1)
        def resetRows():
            self.setMatieres(self.matieresDefault)
        def browseDirectory():
            if self.ui.matiereTableWidget.currentColumn() == 2:
                row = self.ui.matiereTableWidget.currentRow()
                filename = QFileDialog.getExistingDirectory()
                self.ui.matiereTableWidget.setItem(row, 2, QTableWidgetItem(filename))
        
        self.ui.matiereTablePlus.clicked.connect(addRow)
        self.ui.matiereTableMinus.clicked.connect(delRow)
        self.ui.matiereTableReset.clicked.connect(resetRows)

        self.ui.matiereTableBrowse.clicked.connect(browseDirectory)

    def aboutTab(self):
        self.ui.varVersionLabel.setText(QtCore.QCoreApplication.translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">{VERSION}</span></p></body></html>"))
    def esperLimit(self, lineedit):
        lineedit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp(r"[^&]+"), lineedit)) # Empêche l'utilisation des esperluètes "&"

if __name__ == "__main__":
    fe = frontEnd()