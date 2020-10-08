# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designer_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from damysos.ui.widgets.labels import VersionLabel
from damysos.ui.widgets.line_edits import SafeAdvancedLineEdit
from damysos.ui.widgets.matiere_table import MatiereTable
from damysos.ui.widgets.line_edits import AdvancedLineEdit
from damysos.ui.widgets.advanced_tab_widget import AdvancedTabWidget
from damysos.ui.widgets.push_buttons import ConfigPushButton
from damysos.ui.widgets.push_buttons import MatiereMenuPushButton
from damysos.ui.widgets.push_buttons import NumeroMenuPushButton
from damysos.ui.widgets.labels import PathMenuLabel

from  . import designer_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(728, 471)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(728, 471))
        MainWindow.setMaximumSize(QSize(728, 471))
        MainWindow.setMouseTracking(False)
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = AdvancedTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 711, 451))
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.genTab = QWidget()
        self.genTab.setObjectName(u"genTab")
        self.infoGroupBox = QGroupBox(self.genTab)
        self.infoGroupBox.setObjectName(u"infoGroupBox")
        self.infoGroupBox.setGeometry(QRect(10, 10, 321, 361))
        self.titreGroupBox = QGroupBox(self.infoGroupBox)
        self.titreGroupBox.setObjectName(u"titreGroupBox")
        self.titreGroupBox.setGeometry(QRect(10, 20, 300, 61))
        self.titreLineEdit = AdvancedLineEdit(self.titreGroupBox)
        self.titreLineEdit.setObjectName(u"titreLineEdit")
        self.titreLineEdit.setGeometry(QRect(10, 21, 281, 38))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titreLineEdit.sizePolicy().hasHeightForWidth())
        self.titreLineEdit.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Garamond")
        self.titreLineEdit.setFont(font)
        self.titreLineEdit.setAlignment(Qt.AlignCenter)
        self.titreLineEdit.setClearButtonEnabled(True)
        self.soustitreGroupBox = QGroupBox(self.infoGroupBox)
        self.soustitreGroupBox.setObjectName(u"soustitreGroupBox")
        self.soustitreGroupBox.setEnabled(True)
        self.soustitreGroupBox.setGeometry(QRect(10, 80, 300, 61))
        self.soustitreLineEdit = AdvancedLineEdit(self.soustitreGroupBox)
        self.soustitreLineEdit.setObjectName(u"soustitreLineEdit")
        self.soustitreLineEdit.setGeometry(QRect(10, 21, 281, 38))
        sizePolicy1.setHeightForWidth(self.soustitreLineEdit.sizePolicy().hasHeightForWidth())
        self.soustitreLineEdit.setSizePolicy(sizePolicy1)
        self.soustitreLineEdit.setFont(font)
        self.soustitreLineEdit.setAlignment(Qt.AlignCenter)
        self.soustitreLineEdit.setClearButtonEnabled(True)
        self.matGroupBox = QGroupBox(self.infoGroupBox)
        self.matGroupBox.setObjectName(u"matGroupBox")
        self.matGroupBox.setGeometry(QRect(100, 150, 140, 61))
        self.matLineEdit = SafeAdvancedLineEdit(self.matGroupBox)
        self.matLineEdit.setObjectName(u"matLineEdit")
        self.matLineEdit.setEnabled(False)
        self.matLineEdit.setGeometry(QRect(15, 25, 98, 29))
        sizePolicy1.setHeightForWidth(self.matLineEdit.sizePolicy().hasHeightForWidth())
        self.matLineEdit.setSizePolicy(sizePolicy1)
        self.matLineEdit.setMinimumSize(QSize(0, 29))
        self.matLineEdit.setFont(font)
        self.matLineEdit.setFrame(True)
        self.matLineEdit.setAlignment(Qt.AlignCenter)
        self.matLineEdit.setClearButtonEnabled(False)
        self.matMenuButton = MatiereMenuPushButton(self.matGroupBox)
        self.matMenuButton.setObjectName(u"matMenuButton")
        self.matMenuButton.setGeometry(QRect(106, 25, 20, 29))
        self.matMenuButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.matMenuButton.raise_()
        self.matLineEdit.raise_()
        self.numGroupBox = QGroupBox(self.infoGroupBox)
        self.numGroupBox.setObjectName(u"numGroupBox")
        self.numGroupBox.setGeometry(QRect(100, 210, 140, 61))
        self.numLineEdit = SafeAdvancedLineEdit(self.numGroupBox)
        self.numLineEdit.setObjectName(u"numLineEdit")
        self.numLineEdit.setEnabled(False)
        self.numLineEdit.setGeometry(QRect(15, 25, 98, 29))
        sizePolicy1.setHeightForWidth(self.numLineEdit.sizePolicy().hasHeightForWidth())
        self.numLineEdit.setSizePolicy(sizePolicy1)
        self.numLineEdit.setFont(font)
        self.numLineEdit.setAlignment(Qt.AlignCenter)
        self.numLineEdit.setClearButtonEnabled(False)
        self.numMenuButton = NumeroMenuPushButton(self.numGroupBox)
        self.numMenuButton.setObjectName(u"numMenuButton")
        self.numMenuButton.setGeometry(QRect(106, 25, 21, 29))
        self.numMenuButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.numMenuButton.raise_()
        self.numLineEdit.raise_()
        self.sectionGroupBox = QGroupBox(self.infoGroupBox)
        self.sectionGroupBox.setObjectName(u"sectionGroupBox")
        self.sectionGroupBox.setGeometry(QRect(10, 290, 300, 61))
        self.sectionNumLabel = QLabel(self.sectionGroupBox)
        self.sectionNumLabel.setObjectName(u"sectionNumLabel")
        self.sectionNumLabel.setGeometry(QRect(20, 24, 47, 31))
        self.sectionNumLabel.setFont(font)
        self.sectionNumLabel.setStyleSheet(u"")
        self.sectionLineEdit = AdvancedLineEdit(self.sectionGroupBox)
        self.sectionLineEdit.setObjectName(u"sectionLineEdit")
        self.sectionLineEdit.setGeometry(QRect(40, 25, 251, 29))
        sizePolicy1.setHeightForWidth(self.sectionLineEdit.sizePolicy().hasHeightForWidth())
        self.sectionLineEdit.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Garamond")
        font1.setUnderline(True)
        self.sectionLineEdit.setFont(font1)
        self.sectionLineEdit.setMaxLength(32767)
        self.sectionLineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.sectionLineEdit.setClearButtonEnabled(True)
        self.infoPersoGroupBox = QGroupBox(self.genTab)
        self.infoPersoGroupBox.setObjectName(u"infoPersoGroupBox")
        self.infoPersoGroupBox.setGeometry(QRect(350, 10, 319, 151))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.infoPersoGroupBox.sizePolicy().hasHeightForWidth())
        self.infoPersoGroupBox.setSizePolicy(sizePolicy2)
        self.infoPersoGroupBox.setMinimumSize(QSize(0, 0))
        self.auteurPersoGroupBox = QGroupBox(self.infoPersoGroupBox)
        self.auteurPersoGroupBox.setObjectName(u"auteurPersoGroupBox")
        self.auteurPersoGroupBox.setGeometry(QRect(10, 20, 291, 61))
        self.auteurPersoLabel = QLabel(self.auteurPersoGroupBox)
        self.auteurPersoLabel.setObjectName(u"auteurPersoLabel")
        self.auteurPersoLabel.setGeometry(QRect(10, 25, 271, 31))
        font2 = QFont()
        font2.setFamily(u"Garamond")
        font2.setPointSize(18)
        font2.setItalic(True)
        self.auteurPersoLabel.setFont(font2)
        self.auteurPersoLabel.setTextFormat(Qt.RichText)
        self.auteurPersoLabel.setScaledContents(False)
        self.auteurPersoLabel.setAlignment(Qt.AlignCenter)
        self.niveauPersoGroupBox = QGroupBox(self.infoPersoGroupBox)
        self.niveauPersoGroupBox.setObjectName(u"niveauPersoGroupBox")
        self.niveauPersoGroupBox.setGeometry(QRect(10, 80, 291, 61))
        self.niveauPersoLabel = QLabel(self.niveauPersoGroupBox)
        self.niveauPersoLabel.setObjectName(u"niveauPersoLabel")
        self.niveauPersoLabel.setGeometry(QRect(10, 25, 271, 31))
        font3 = QFont()
        font3.setFamily(u"Garamond")
        font3.setPointSize(17)
        font3.setItalic(True)
        self.niveauPersoLabel.setFont(font3)
        self.niveauPersoLabel.setTextFormat(Qt.RichText)
        self.niveauPersoLabel.setScaledContents(True)
        self.niveauPersoLabel.setAlignment(Qt.AlignCenter)
        self.niveauPersoLabel.setWordWrap(False)
        self.modelGroupBox = QGroupBox(self.genTab)
        self.modelGroupBox.setObjectName(u"modelGroupBox")
        self.modelGroupBox.setGeometry(QRect(10, 365, 321, 71))
        self.modelLineEdit = AdvancedLineEdit(self.modelGroupBox)
        self.modelLineEdit.setObjectName(u"modelLineEdit")
        self.modelLineEdit.setEnabled(False)
        self.modelLineEdit.setGeometry(QRect(27, 30, 251, 29))
        sizePolicy1.setHeightForWidth(self.modelLineEdit.sizePolicy().hasHeightForWidth())
        self.modelLineEdit.setSizePolicy(sizePolicy1)
        self.modelLineEdit.setFont(font)
        self.modelLineEdit.setAlignment(Qt.AlignCenter)
        self.modelLineEdit.setClearButtonEnabled(False)
        self.modelToolButton = QPushButton(self.modelGroupBox)
        self.modelToolButton.setObjectName(u"modelToolButton")
        self.modelToolButton.setGeometry(QRect(270, 30, 21, 29))
        self.modelToolButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.modelToolButton.raise_()
        self.modelLineEdit.raise_()
        self.genPushButton = QPushButton(self.genTab)
        self.genPushButton.setObjectName(u"genPushButton")
        self.genPushButton.setGeometry(QRect(440, 381, 150, 55))
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.genPushButton.sizePolicy().hasHeightForWidth())
        self.genPushButton.setSizePolicy(sizePolicy3)
        self.genPushButton.setMinimumSize(QSize(150, 0))
        font4 = QFont()
        font4.setPointSize(18)
        font4.setBold(True)
        font4.setWeight(75)
        self.genPushButton.setFont(font4)
        self.genPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayoutWidget_2 = QWidget(self.genTab)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(350, 170, 323, 211))
        self.pathLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.pathLayout.setObjectName(u"pathLayout")
        self.pathLayout.setContentsMargins(0, 0, 0, 5)
        self.pathSpacer = QSpacerItem(0, 1000, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.pathLayout.addItem(self.pathSpacer)

        self.pathPathLabel = PathMenuLabel(self.verticalLayoutWidget_2)
        self.pathPathLabel.setObjectName(u"pathPathLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pathPathLabel.sizePolicy().hasHeightForWidth())
        self.pathPathLabel.setSizePolicy(sizePolicy4)
        self.pathPathLabel.setMaximumSize(QSize(321, 16777215))
        font5 = QFont()
        font5.setUnderline(True)
        self.pathPathLabel.setFont(font5)
        self.pathPathLabel.setCursor(QCursor(Qt.ArrowCursor))
        self.pathPathLabel.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.pathPathLabel.setWordWrap(True)
        self.pathPathLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.pathLayout.addWidget(self.pathPathLabel)

        self.tabWidget.addTab(self.genTab, "")
        self.configTab = QWidget()
        self.configTab.setObjectName(u"configTab")
        self.infoConfigGroupBox = QGroupBox(self.configTab)
        self.infoConfigGroupBox.setObjectName(u"infoConfigGroupBox")
        self.infoConfigGroupBox.setGeometry(QRect(10, 10, 307, 161))
        self.auteurConfig = QGroupBox(self.infoConfigGroupBox)
        self.auteurConfig.setObjectName(u"auteurConfig")
        self.auteurConfig.setGeometry(QRect(10, 20, 288, 61))
        self.auteurLineEdit = AdvancedLineEdit(self.auteurConfig)
        self.auteurLineEdit.setObjectName(u"auteurLineEdit")
        self.auteurLineEdit.setGeometry(QRect(10, 25, 269, 29))
        sizePolicy1.setHeightForWidth(self.auteurLineEdit.sizePolicy().hasHeightForWidth())
        self.auteurLineEdit.setSizePolicy(sizePolicy1)
        self.auteurLineEdit.setFont(font)
        self.auteurLineEdit.setAlignment(Qt.AlignCenter)
        self.auteurLineEdit.setClearButtonEnabled(True)
        self.niveauConfig = QGroupBox(self.infoConfigGroupBox)
        self.niveauConfig.setObjectName(u"niveauConfig")
        self.niveauConfig.setGeometry(QRect(10, 90, 288, 61))
        self.niveauLineEdit = AdvancedLineEdit(self.niveauConfig)
        self.niveauLineEdit.setObjectName(u"niveauLineEdit")
        self.niveauLineEdit.setGeometry(QRect(10, 25, 269, 29))
        sizePolicy1.setHeightForWidth(self.niveauLineEdit.sizePolicy().hasHeightForWidth())
        self.niveauLineEdit.setSizePolicy(sizePolicy1)
        self.niveauLineEdit.setFont(font)
        self.niveauLineEdit.setAlignment(Qt.AlignCenter)
        self.niveauLineEdit.setClearButtonEnabled(True)
        self.verticalLayoutWidget_4 = QWidget(self.configTab)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(330, 20, 341, 161))
        self.configSaveLayout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.configSaveLayout.setSpacing(0)
        self.configSaveLayout.setObjectName(u"configSaveLayout")
        self.configSaveLayout.setContentsMargins(30, 50, 30, 50)
        self.configSaveButton = ConfigPushButton(self.verticalLayoutWidget_4)
        self.configSaveButton.setObjectName(u"configSaveButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.configSaveButton.sizePolicy().hasHeightForWidth())
        self.configSaveButton.setSizePolicy(sizePolicy5)
        self.configSaveButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.configSaveLayout.addWidget(self.configSaveButton)

        self.matieresConfig = QGroupBox(self.configTab)
        self.matieresConfig.setObjectName(u"matieresConfig")
        self.matieresConfig.setGeometry(QRect(10, 180, 661, 261))
        self.matieresConfig.setFlat(False)
        self.matieresConfig.setCheckable(True)
        self.matieresConfig.setChecked(True)
        self.matiereTable = MatiereTable(self.matieresConfig)
        self.matiereTable.setObjectName(u"matiereTable")
        self.matiereTable.setGeometry(QRect(0, 30, 661, 231))
        self.tabWidget.addTab(self.configTab, "")
        self.modelTab = QWidget()
        self.modelTab.setObjectName(u"modelTab")
        self.modelListWidget = QListWidget(self.modelTab)
        self.modelListWidget.setObjectName(u"modelListWidget")
        self.modelListWidget.setGeometry(QRect(20, 20, 181, 341))
        self.modelListWidget.setStyleSheet(u"QListView::item{\n"
"  padding-top: 10px;\n"
"  padding-bottom:10px;\n"
"  border-radius: 4px;\n"
"  margin-top: 10px;\n"
"  margin-bottom: 10px;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"  background-color: none;\n"
"  border: 2px dashed #605e5c;\n"
"  padding-top: 10px;\n"
"  padding-bottom:10px;\n"
"}\n"
"\n"
"QListView::item:selected:hover {\n"
"  background-color: #605e5c;\n"
"  color: white;\n"
"  border-color: #969696;\n"
"}")
        self.modelListWidget.setFrameShape(QFrame.StyledPanel)
        self.modelListWidget.setDefaultDropAction(Qt.CopyAction)
        self.modelListWidget.setAlternatingRowColors(False)
        self.modelListWidget.setMovement(QListView.Static)
        self.modelListWidget.setSpacing(10)
        self.modelListWidget.setBatchSize(100)
        self.modelListWidget.setSortingEnabled(True)
        self.modelListPlus = QPushButton(self.modelTab)
        self.modelListPlus.setObjectName(u"modelListPlus")
        self.modelListPlus.setEnabled(True)
        self.modelListPlus.setGeometry(QRect(20, 370, 21, 21))
        self.modelListPlus.setCursor(QCursor(Qt.PointingHandCursor))
        self.modelListMinus = QPushButton(self.modelTab)
        self.modelListMinus.setObjectName(u"modelListMinus")
        self.modelListMinus.setEnabled(False)
        self.modelListMinus.setGeometry(QRect(47, 370, 21, 21))
        self.modelListMinus.setCursor(QCursor(Qt.PointingHandCursor))
        self.modelWikiLink = QLabel(self.modelTab)
        self.modelWikiLink.setObjectName(u"modelWikiLink")
        self.modelWikiLink.setGeometry(QRect(16, 409, 191, 31))
        font6 = QFont()
        font6.setFamily(u"Garamond")
        font6.setPointSize(12)
        self.modelWikiLink.setFont(font6)
        self.modelWikiLink.setCursor(QCursor(Qt.PointingHandCursor))
        self.modelWikiLink.setTextFormat(Qt.RichText)
        self.modelWikiLink.setOpenExternalLinks(True)
        self.modelWikiLink.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.modelListReset = QPushButton(self.modelTab)
        self.modelListReset.setObjectName(u"modelListReset")
        self.modelListReset.setEnabled(True)
        self.modelListReset.setGeometry(QRect(126, 370, 75, 21))
        self.modelListReset.setCursor(QCursor(Qt.PointingHandCursor))
        self.modelValuesGroupBox = QGroupBox(self.modelTab)
        self.modelValuesGroupBox.setObjectName(u"modelValuesGroupBox")
        self.modelValuesGroupBox.setEnabled(False)
        self.modelValuesGroupBox.setGeometry(QRect(220, 5, 451, 237))
        self.formLayoutWidget_2 = QWidget(self.modelValuesGroupBox)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 27, 431, 209))
        self.modelValuesFormLayout = QFormLayout(self.formLayoutWidget_2)
        self.modelValuesFormLayout.setObjectName(u"modelValuesFormLayout")
        self.modelValuesFormLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.modelValuesFormLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.modelValuesFormLayout.setContentsMargins(0, 0, 0, 0)
        self.titreModelLineEdit = AdvancedLineEdit(self.formLayoutWidget_2)
        self.titreModelLineEdit.setObjectName(u"titreModelLineEdit")

        self.modelValuesFormLayout.setWidget(0, QFormLayout.FieldRole, self.titreModelLineEdit)

        self.soustitreModelLineEdit = AdvancedLineEdit(self.formLayoutWidget_2)
        self.soustitreModelLineEdit.setObjectName(u"soustitreModelLineEdit")

        self.modelValuesFormLayout.setWidget(1, QFormLayout.FieldRole, self.soustitreModelLineEdit)

        self.matiereModelLineEdit = AdvancedLineEdit(self.formLayoutWidget_2)
        self.matiereModelLineEdit.setObjectName(u"matiereModelLineEdit")

        self.modelValuesFormLayout.setWidget(2, QFormLayout.FieldRole, self.matiereModelLineEdit)

        self.numeroModelLineEdit = AdvancedLineEdit(self.formLayoutWidget_2)
        self.numeroModelLineEdit.setObjectName(u"numeroModelLineEdit")

        self.modelValuesFormLayout.setWidget(3, QFormLayout.FieldRole, self.numeroModelLineEdit)

        self.sectionModelLineEdit = AdvancedLineEdit(self.formLayoutWidget_2)
        self.sectionModelLineEdit.setObjectName(u"sectionModelLineEdit")

        self.modelValuesFormLayout.setWidget(4, QFormLayout.FieldRole, self.sectionModelLineEdit)

        self.auteurModelLineEdit = AdvancedLineEdit(self.formLayoutWidget_2)
        self.auteurModelLineEdit.setObjectName(u"auteurModelLineEdit")

        self.modelValuesFormLayout.setWidget(5, QFormLayout.FieldRole, self.auteurModelLineEdit)

        self.titreModelCheckBox = QCheckBox(self.formLayoutWidget_2)
        self.titreModelCheckBox.setObjectName(u"titreModelCheckBox")
        font7 = QFont()
        font7.setFamily(u"Consolas")
        self.titreModelCheckBox.setFont(font7)
        self.titreModelCheckBox.setChecked(True)

        self.modelValuesFormLayout.setWidget(0, QFormLayout.LabelRole, self.titreModelCheckBox)

        self.soustitreModelCheckBox = QCheckBox(self.formLayoutWidget_2)
        self.soustitreModelCheckBox.setObjectName(u"soustitreModelCheckBox")
        self.soustitreModelCheckBox.setFont(font7)
        self.soustitreModelCheckBox.setChecked(True)

        self.modelValuesFormLayout.setWidget(1, QFormLayout.LabelRole, self.soustitreModelCheckBox)

        self.matiereModelCheckBox = QCheckBox(self.formLayoutWidget_2)
        self.matiereModelCheckBox.setObjectName(u"matiereModelCheckBox")
        self.matiereModelCheckBox.setFont(font7)
        self.matiereModelCheckBox.setChecked(True)

        self.modelValuesFormLayout.setWidget(2, QFormLayout.LabelRole, self.matiereModelCheckBox)

        self.numeroModelCheckBox = QCheckBox(self.formLayoutWidget_2)
        self.numeroModelCheckBox.setObjectName(u"numeroModelCheckBox")
        self.numeroModelCheckBox.setFont(font7)
        self.numeroModelCheckBox.setChecked(True)

        self.modelValuesFormLayout.setWidget(3, QFormLayout.LabelRole, self.numeroModelCheckBox)

        self.sectionModelCheckBox = QCheckBox(self.formLayoutWidget_2)
        self.sectionModelCheckBox.setObjectName(u"sectionModelCheckBox")
        self.sectionModelCheckBox.setFont(font7)
        self.sectionModelCheckBox.setChecked(True)

        self.modelValuesFormLayout.setWidget(4, QFormLayout.LabelRole, self.sectionModelCheckBox)

        self.auteurModelCheckBox = QCheckBox(self.formLayoutWidget_2)
        self.auteurModelCheckBox.setObjectName(u"auteurModelCheckBox")
        self.auteurModelCheckBox.setFont(font7)
        self.auteurModelCheckBox.setChecked(True)

        self.modelValuesFormLayout.setWidget(5, QFormLayout.LabelRole, self.auteurModelCheckBox)

        self.niveauModelCheckBox = QCheckBox(self.formLayoutWidget_2)
        self.niveauModelCheckBox.setObjectName(u"niveauModelCheckBox")
        self.niveauModelCheckBox.setFont(font7)
        self.niveauModelCheckBox.setStyleSheet(u"")
        self.niveauModelCheckBox.setChecked(True)

        self.modelValuesFormLayout.setWidget(6, QFormLayout.LabelRole, self.niveauModelCheckBox)

        self.niveauModelLineEdit = AdvancedLineEdit(self.formLayoutWidget_2)
        self.niveauModelLineEdit.setObjectName(u"niveauModelLineEdit")
        self.niveauModelLineEdit.setEnabled(False)

        self.modelValuesFormLayout.setWidget(6, QFormLayout.FieldRole, self.niveauModelLineEdit)

        self.modelPathsGroupBox = QGroupBox(self.modelTab)
        self.modelPathsGroupBox.setObjectName(u"modelPathsGroupBox")
        self.modelPathsGroupBox.setEnabled(False)
        self.modelPathsGroupBox.setGeometry(QRect(220, 240, 451, 121))
        self.modelPathsGroupBox.setStyleSheet(u"")
        self.formLayoutWidget = QWidget(self.modelPathsGroupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 30, 431, 81))
        self.modelPathsLayout = QFormLayout(self.formLayoutWidget)
        self.modelPathsLayout.setObjectName(u"modelPathsLayout")
        self.modelPathsLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.modelPathsLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.modelPathsLayout.setContentsMargins(0, 0, 0, 0)
        self.modelDestinationLabel = QLabel(self.formLayoutWidget)
        self.modelDestinationLabel.setObjectName(u"modelDestinationLabel")

        self.modelPathsLayout.setWidget(1, QFormLayout.LabelRole, self.modelDestinationLabel)

        self.modelDestinationLineEdit = SafeAdvancedLineEdit(self.formLayoutWidget)
        self.modelDestinationLineEdit.setObjectName(u"modelDestinationLineEdit")

        self.modelPathsLayout.setWidget(1, QFormLayout.FieldRole, self.modelDestinationLineEdit)

        self.modelPathModelLabel = QLabel(self.formLayoutWidget)
        self.modelPathModelLabel.setObjectName(u"modelPathModelLabel")
        self.modelPathModelLabel.setFont(font7)
        self.modelPathModelLabel.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.modelPathModelLabel.setWordWrap(True)

        self.modelPathsLayout.setWidget(0, QFormLayout.FieldRole, self.modelPathModelLabel)

        self.modelPathPushButton = QPushButton(self.formLayoutWidget)
        self.modelPathPushButton.setObjectName(u"modelPathPushButton")
        self.modelPathPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.modelPathPushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: none;\n"
"    border: none;\n"
"    color: #FFFFFF;\n"
"    border-radius: 4px;\n"
"    padding: 3px;\n"
"    outline: none;\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: none;\n"
"    border: none;\n"
"    color: #787878;\n"
"    border-radius: 4px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: none;\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"    background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: none;\n"
"}\n"
"\n"
"QPushButton:selected {\n"
"    background: none;\n"
"    color: #32414B;\n"
"    border: none;\n"
"}")

        self.modelPathsLayout.setWidget(0, QFormLayout.LabelRole, self.modelPathPushButton)

        self.modelDefaultPushButton = QPushButton(self.modelTab)
        self.modelDefaultPushButton.setObjectName(u"modelDefaultPushButton")
        self.modelDefaultPushButton.setEnabled(False)
        self.modelDefaultPushButton.setGeometry(QRect(220, 370, 131, 21))
        self.modelDefaultPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.modelApplyPushButton = QPushButton(self.modelTab)
        self.modelApplyPushButton.setObjectName(u"modelApplyPushButton")
        self.modelApplyPushButton.setEnabled(True)
        self.modelApplyPushButton.setGeometry(QRect(470, 370, 201, 63))
        self.modelApplyPushButton.setFont(font6)
        self.modelApplyPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabWidget.addTab(self.modelTab, "")
        self.aboutTab = QWidget()
        self.aboutTab.setObjectName(u"aboutTab")
        self.verticalLayoutWidget = QWidget(self.aboutTab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 681, 451))
        self.aboutLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.aboutLayout.setObjectName(u"aboutLayout")
        self.aboutLayout.setContentsMargins(0, 0, 0, 0)
        self.titleLabel = QLabel(self.verticalLayoutWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setTextFormat(Qt.AutoText)
        self.titleLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.aboutLayout.addWidget(self.titleLabel)

        self.versionLabel = VersionLabel(self.verticalLayoutWidget)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setAlignment(Qt.AlignCenter)

        self.aboutLayout.addWidget(self.versionLabel)

        self.gitHubLabel = QLabel(self.verticalLayoutWidget)
        self.gitHubLabel.setObjectName(u"gitHubLabel")
        self.gitHubLabel.setAlignment(Qt.AlignCenter)
        self.gitHubLabel.setOpenExternalLinks(True)
        self.gitHubLabel.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.aboutLayout.addWidget(self.gitHubLabel)

        self.tabWidget.addTab(self.aboutTab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.infoGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Informations", None))
        self.titreGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Titre", None))
        self.titreLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Les Lois de Newton", None))
        self.soustitreGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sous-Titre", None))
        self.soustitreLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Newton, grand physicien", None))
        self.matGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mati\u00e8re", None))
        self.matLineEdit.setText("")
        self.matLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PHY", None))
        self.matMenuButton.setText("")
        self.numGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Num\u00e9ro", None))
        self.numLineEdit.setText("")
        self.numLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0624", None))
        self.numMenuButton.setText("")
        self.sectionGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Premi\u00e8re Section", None))
        self.sectionNumLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; text-decoration: underline;\">1.</span></p></body></html>", None))
        self.sectionLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"La Loi de l'Inertie", None))
#if QT_CONFIG(tooltip)
        self.infoPersoGroupBox.setToolTip(QCoreApplication.translate("MainWindow", u"Pour modifier les informations, veuillez aller dans le Configurateur", None))
#endif // QT_CONFIG(tooltip)
        self.infoPersoGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Informations Personnelles", None))
        self.auteurPersoGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Auteur", None))
        self.auteurPersoLabel.setText(QCoreApplication.translate("MainWindow", u"Auteur", None))
        self.niveauPersoGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Niveau", None))
        self.niveauPersoLabel.setText(QCoreApplication.translate("MainWindow", u"Niveau", None))
        self.modelGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mod\u00e8le", None))
        self.modelLineEdit.setText("")
        self.modelLineEdit.setPlaceholderText("")
        self.modelToolButton.setText("")
        self.genPushButton.setText(QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rer", None))
        self.pathPathLabel.setText(QCoreApplication.translate("MainWindow", u"Aucun chemin de sauvegarde", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.genTab), QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rateur", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.genTab), QCoreApplication.translate("MainWindow", u"Cr\u00e9er un document", None))
#endif // QT_CONFIG(tooltip)
        self.infoConfigGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Informations Personnelles", None))
        self.auteurConfig.setTitle(QCoreApplication.translate("MainWindow", u"Auteur", None))
        self.auteurLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Laurent Bourgon", None))
        self.niveauConfig.setTitle(QCoreApplication.translate("MainWindow", u"Niveau", None))
        self.niveauLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Secondaire 5 - 2019-2020", None))
        self.configSaveButton.setText(QCoreApplication.translate("MainWindow", u"Appliquer et Enregistrer", None))
        self.matieresConfig.setTitle(QCoreApplication.translate("MainWindow", u"Mati\u00e8res Personnalis\u00e9es", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.configTab), QCoreApplication.translate("MainWindow", u"Configurateur", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.configTab), QCoreApplication.translate("MainWindow", u"Modifier les Informations", None))
#endif // QT_CONFIG(tooltip)
        self.modelListPlus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.modelListMinus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.modelWikiLink.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/BourgonLaurent/Damysos/wiki/Comment-cr%C3%A9er-son-propre-mod%C3%A8le\"><span style=\" text-decoration: underline; color:#f0f0f0;\">Comment cr\u00e9er vos propres mod\u00e8les?</span></a></p></body></html>", None))
        self.modelListReset.setText(QCoreApplication.translate("MainWindow", u"R\u00e9initialiser", None))
        self.modelValuesGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Valeurs", None))
        self.titreModelLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Titre", None))
        self.soustitreModelLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sous-Titre", None))
        self.matiereModelLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mati\u00e8re", None))
        self.numeroModelLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Num\u00e9ro", None))
        self.sectionModelLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Section", None))
        self.auteurModelLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Auteur", None))
        self.titreModelCheckBox.setText(QCoreApplication.translate("MainWindow", u"titre", None))
        self.soustitreModelCheckBox.setText(QCoreApplication.translate("MainWindow", u"soustitre", None))
        self.matiereModelCheckBox.setText(QCoreApplication.translate("MainWindow", u"matiere", None))
        self.numeroModelCheckBox.setText(QCoreApplication.translate("MainWindow", u"numero", None))
        self.sectionModelCheckBox.setText(QCoreApplication.translate("MainWindow", u"section", None))
        self.auteurModelCheckBox.setText(QCoreApplication.translate("MainWindow", u"auteur", None))
        self.niveauModelCheckBox.setText(QCoreApplication.translate("MainWindow", u"niveau", None))
        self.niveauModelLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Niveau", None))
        self.modelPathsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Emplacements", None))
        self.modelDestinationLabel.setText(QCoreApplication.translate("MainWindow", u"Dossier de destination", None))
        self.modelPathModelLabel.setText(QCoreApplication.translate("MainWindow", u"Aucun fichier s\u00e9lectionn\u00e9", None))
        self.modelPathPushButton.setText(QCoreApplication.translate("MainWindow", u"Fichier Mod\u00e8le", None))
        self.modelDefaultPushButton.setText(QCoreApplication.translate("MainWindow", u"Mod\u00e8le par d\u00e9faut", None))
        self.modelApplyPushButton.setText(QCoreApplication.translate("MainWindow", u"Appliquer et Enregistrer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.modelTab), QCoreApplication.translate("MainWindow", u"Mod\u00e8les", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.modelTab), QCoreApplication.translate("MainWindow", u"Cr\u00e9er et g\u00e9rer les mod\u00e8les", None))
#endif // QT_CONFIG(tooltip)
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">Damysos</span></p></body></html>", None))
        self.gitHubLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/BourgonLaurent/Damysos/blob/master/LICENSE\"><span style=\" text-decoration: underline; color:#f0f0f0;\">\u00a9 Laurent Bourgon Sous la license MIT</span></a></p><p><span style=\" color:#f0f0f0;\"><br/></span></p><p><a href=\"https://github.com/BourgonLaurent/Damysos\"><span style=\" text-decoration: underline; color:#f0f0f0;\">Projet GitHub</span></a></p><p><a href=\"https://github.com/BourgonLaurent/Damysos#faq\"><span style=\" text-decoration: underline; color:#f0f0f0;\">Vous avez un probl\u00e8me?</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), QCoreApplication.translate("MainWindow", u"\u00c0 Propos", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.aboutTab), QCoreApplication.translate("MainWindow", u"\u00c0 Propos", None))
#endif // QT_CONFIG(tooltip)
        pass
    # retranslateUi

