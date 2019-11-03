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
import os, json
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

os.chdir(os.path.realpath(__file__).replace(os.path.basename(__file__), ""))  # Accède aux fichiers depuis la racine du programme, et non l'endroit du shell

VERSION = "2.1.0~b4"

class frontEnd:
    def __init__(self):
        self.Ui, self.Window = uic.loadUiType("pyEtude.ui")

        self.app = QApplication([])  # pylint: disable=undefined-variable

        self.window = self.Window()
        self.ui = self.Ui()
        self.ui.setupUi(self.window)

        self.configTab()
        self.aboutTab()

        self.firstLaunch()
        

        self.window.setWindowTitle("pyÉtude - v" + VERSION)
        self.window.show()
        self.app.exec_()
    
    def firstLaunch(self):
        self.matieresDefault = {
            "Anglais":["ANG", ""],
            "Arts":["ART", ""],
            "Chimie":["CHM", ""],
            "Éducation Financière":["EFI", ""],
            "Éducation Physique":["EDP", ""],
            "Éthique et Culture Religieuse":["ECR", ""],
            "Français":["FRA", ""],
            "Mathématiques":["MAT", ""],
            "Monde Contemporain":["MDC", ""],
            "Physique":["PHY", ""]
            }
        if os.path.isfile("./pyEtude.json") == True:
            # Donne accès au générateur
            self.ui.tabWidget.setTabEnabled(0, True)
            self.ui.tabWidget.setTabToolTip(0, "Créer un document")
            self.ui.tabWidget.setCurrentIndex(0)
            self.readJSON()
        else:
            assert FileNotFoundError
            # Empêche l'accès au générateur
            self.ui.tabWidget.setTabEnabled(0, False)
            self.ui.tabWidget.setTabToolTip(0, "Veuillez utilisez le Configurateur")
            self.ui.tabWidget.setCurrentIndex(1)
            self.setMatieres(self.matieresDefault)

    def setMatieres(self, datadict):
        for i in range(0,self.ui.matiereTableWidget.rowCount()+1):  # Enlève les vieilles données
            self.ui.matiereTableWidget.removeRow(self.ui.matiereTableWidget.rowCount()-1)
        for i, key in enumerate(datadict):  # met les données du dictionnaire
            self.ui.matiereTableWidget.insertRow(self.ui.matiereTableWidget.rowCount())
            self.ui.matiereTableWidget.setItem(i, 0, QTableWidgetItem(key))  # pylint: disable=undefined-variable
            self.ui.matiereTableWidget.setItem(i, 1, QTableWidgetItem(datadict[key][0]))  # pylint: disable=undefined-variable
            self.ui.matiereTableWidget.setItem(i, 2, QTableWidgetItem(datadict[key][1]))  # pylint: disable=undefined-variable
    
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
        
        print(jsonData)

    def aboutTab(self):
        self.ui.varVersionLabel.setText(QtCore.QCoreApplication.translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">{VERSION}</span></p></body></html>"))

    def configTab(self):
        def saveVariable():
            if self.ui.auteurLineEdit.text() != "":
                self.auteur = self.ui.auteurLineEdit.text()
            else:
                self.auteur = self.ui.auteurLineEdit.placeholderText()
            
            if self.ui.secLineEdit.text() != "":
                self.sec = self.ui.secLineEdit.text()
            else:
                self.sec = self.ui.secLineEdit.placeholderText()
            
            self.matieres = {}

            for row in range(self.ui.matiereTableWidget.rowCount()):
                matiere = self.ui.matiereTableWidget.item(row, 0)
                mat = self.ui.matiereTableWidget.item(row, 1)
                path = self.ui.matiereTableWidget.item(row, 2)
                if matiere != None and mat != None and path != None:
                    if matiere.text() != "" and mat.text() != "":
                        self.matieres[matiere.text()] = [mat.text(), path.text()]
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
        
        self.ui.matiereTablePlus.clicked.connect(addRow)
        self.ui.matiereTableMinus.clicked.connect(delRow)
    
    def esperLimit(self, lineedit):
        lineedit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp(r"[^&]+"), lineedit)) # Empêche l'utilisation des esperluètes "&"

if __name__ == "__main__":
    fe = frontEnd()