# -*- coding: utf-8 -*-
import os

os.chdir(os.path.realpath(__file__).replace(os.path.basename(__file__), ""))  # Accède aux fichiers depuis la racine du programme, et non l'endroit du shell

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets


VERSION = "2.1.0~b2"

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
        if os.path.isfile("./pyEtude_qt.json") == True:
            # Donne accès au générateur
            self.ui.tabWidget.setTabEnabled(0, True)
            self.ui.tabWidget.setTabToolTip(0, "Créer un document")
            self.ui.tabWidget.setCurrentIndex(0)
        else:
            assert FileNotFoundError
            # Empêche l'accès au générateur
            self.ui.tabWidget.setTabEnabled(0, False)
            self.ui.tabWidget.setTabToolTip(0, "Veuillez utilisez le Configurateur")
            self.ui.tabWidget.setCurrentIndex(1)


    
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
            
            print(self.auteur + self.sec)
        # Empêche l'utilisation des esperluètes "&"
        self.esperLimit(self.ui.auteurLineEdit)
        self.esperLimit(self.ui.secLineEdit)

        self.ui.configSaveButton.clicked.connect(saveVariable)
    
    def esperLimit(self, lineedit):
        lineedit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp(r"[^&]+"), lineedit)) # Empêche l'utilisation des esperluètes "&"

if __name__ == "__main__":
    fe = frontEnd()