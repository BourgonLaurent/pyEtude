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

from .widgets.version_label import VersionLabel
from .widgets.line_edits import SafeAdvancedLineEdit
from .widgets.matiere_table import MatiereTable
from .widgets.line_edits import AdvancedLineEdit
from .widgets.advanced_tab_widget import AdvancedTabWidget
from .widgets.push_buttons import ConfigPushButton


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
        MainWindow.setStyleSheet(u"QWidget {\n"
"  background-color: #262626;\n"
"  border: 0px solid #444444;\n"
"  padding: 0px;\n"
"  color: #FFFFFF;\n"
"  selection-background-color: #444444;\n"
"  selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QWidget:disabled {\n"
"  background-color: #252424;\n"
"  color: #787878;\n"
"  selection-background-color: #14506E;\n"
"  selection-color: #787878;\n"
"}\n"
"\n"
"/* QWidget::item:selected {\n"
"  background-color: none;\n"
"}\n"
"\n"
"QWidget::item:hover {\n"
"  background-color: #148CD2;\n"
"  color: #32414B;\n"
"} */\n"
"\n"
"/* QMainWindow ------------------------------------------------------------\n"
"\n"
"This adjusts the splitter in the dock widget, not qsplitter\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmainwindow\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMainWindow::separator {\n"
"  background-color: #32414B;\n"
"  border: 0px solid #19232D;\n"
"  spacing: 0px;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QMainWindow::separato"
                        "r:hover {\n"
"  background-color: #505F69;\n"
"  border: 0px solid #148CD2;\n"
"}\n"
"\n"
"QMainWindow::separator:horizontal {\n"
"  width: 5px;\n"
"  margin-top: 2px;\n"
"  margin-bottom: 2px;\n"
"  image: url(\":/qss_icons/rc/toolbar_separator_vertical.png\");\n"
"}\n"
"\n"
"QMainWindow::separator:vertical {\n"
"  height: 5px;\n"
"  margin-left: 2px;\n"
"  margin-right: 2px;\n"
"  image: url(\":/qss_icons/rc/toolbar_separator_horizontal.png\");\n"
"}\n"
"\n"
"/* QToolTip ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtooltip\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolTip {\n"
"  background-color: #2b2b2b;\n"
"  border: 1px solid #767676;\n"
"  color: #FFFFFF;\n"
"  /* Remove padding, for fix combo box tooltip */\n"
"  padding: 0px;\n"
"  /* Reducing transparency to read better */\n"
"  opacity: 230;\n"
"}\n"
"\n"
"/* QStatusBar ------------------------------------------"
                        "-------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qstatusbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QStatusBar {\n"
"  border: 1px solid #32414B;\n"
"  /* Fixes Spyder #9120, #9121 */\n"
"  background: #32414B;\n"
"}\n"
"\n"
"QStatusBar QToolTip {\n"
"  background-color: #148CD2;\n"
"  border: 1px solid #19232D;\n"
"  color: #19232D;\n"
"  /* Remove padding, for fix combo box tooltip */\n"
"  padding: 0px;\n"
"  /* Reducing transparency to read better */\n"
"  opacity: 230;\n"
"}\n"
"\n"
"QStatusBar QLabel {\n"
"  /* Fixes Spyder #9120, #9121 */\n"
"  background: transparent;\n"
"}\n"
"\n"
"/* QCheckBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcheckbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QCheckBox {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  spacing: 4px;\n"
""
                        "  outline: none;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QCheckBox QWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"  margin-left: 4px;\n"
"  margin-right: 4px;\n"
"  height: 13px;\n"
"  width: 13px;\n"
"  border: 1px solid #605e5c;\n"
"  background: #323130;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  border: 1px solid #605e5c;\n"
"  background: #484644;\n"
"}\n"
"\n"
"/* QGroupBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qgroupbox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QGroupBox {\n"
"  font-weight: bold;\n"
"  border: 1px solid #444444;\n"
"  border-radius: 4px;\n"
"  padding: 4px;\n"
"  margin-top: 16px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  l"
                        "eft: 3px;\n"
"  padding-left: 3px;\n"
"  padding-right: 5px;\n"
"  padding-top: 8px;\n"
"  padding-bottom: 16px;\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"  margin-left: 2px;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  background-color: #262626;\n"
"  border: 1px solid #605e5c;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QGroupBox::indicator:checked {\n"
"  background-color: #484644;\n"
"  border: 3px solid #605e5c;\n"
"}\n"
"\n"
"/* QRadioButton -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qradiobutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QRadioButton {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  spacing: 4px;\n"
"  padding: 0px;\n"
"  border: none;\n"
"  outline: none;\n"
"}\n"
"\n"
"QRadioButton:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QRadioButton:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"  border: none;\n"
"  outline: none;\n"
""
                        "}\n"
"\n"
"QRadioButton QWidget {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  spacing: 0px;\n"
"  padding: 0px;\n"
"  outline: none;\n"
"  border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"  border: none;\n"
"  outline: none;\n"
"  margin-left: 4px;\n"
"  height: 16px;\n"
"  width: 16px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"  image: url(\":/qss_icons/rc/radio_unchecked.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover, QRadioButton::indicator:unchecked:focus, QRadioButton::indicator:unchecked:pressed {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/rc/radio_unchecked_focus.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled {\n"
"  image: url(\":/qss_icons/rc/radio_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/rc/radio_checked.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover, QRadioButton::indicator:chec"
                        "ked:focus, QRadioButton::indicator:checked:pressed {\n"
"  border: none;\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/rc/radio_checked_focus.png\");\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled {\n"
"  outline: none;\n"
"  image: url(\":/qss_icons/rc/radio_checked_disabled.png\");\n"
"}\n"
"\n"
"/* QMenuBar ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenubar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMenuBar {\n"
"  background-color: #32414B;\n"
"  padding: 2px;\n"
"  border: 1px solid #19232D;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QMenuBar:focus {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"  background: transparent;\n"
"  padding: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  padding: 4px;\n"
"  background: transparent;\n"
"  border: 0px solid #32414B;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"  padding: 4px;\n"
"  border"
                        ": 0px solid #32414B;\n"
"  background-color: #148CD2;\n"
"  color: #F0F0F0;\n"
"  margin-bottom: 0px;\n"
"  padding-bottom: 0px;\n"
"}\n"
"\n"
"/* QMenu ------------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qmenu\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QMenu {\n"
"    border: 0.5px solid #787878;\n"
"    color: #F0F0F0;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background-color: #444444;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: #262626;\n"
"    padding: 4px 4px 4px 4px;\n"
"    /* Reserve space for selection border */\n"
"    border: 1px transparent #32414B;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    color: #F0F0F0;\n"
"    background-color: #605e5c;\n"
"}\n"
"\n"
"/* QAbstractItemView ------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox\n"
""
                        "\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractItemView {\n"
"  alternate-background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QAbstractItemView QLineEdit {\n"
"  padding: 2px;\n"
"}\n"
"\n"
"/* QAbstractScrollArea ----------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractScrollArea {\n"
"  background-color: #262626;\n"
"  border: 1px solid #969696;\n"
"  border-radius: 4px;\n"
"  padding: 2px;\n"
"  /* fix #159 */\n"
"  min-height: 1.25em;\n"
"  /* fix #159 */\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QAbstractScrollArea:disabled {\n"
"  color: #262626;\n"
"}\n"
"\n"
"/* QScrollArea ------------------------------------------------------------\n"
"\n"
"----------------------------------------------------------------"
                        "----------- */\n"
"QScrollArea QWidget QWidget:disabled {\n"
"  background-color: #262626;\n"
"}\n"
"\n"
"/* QScrollBar -------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qscrollbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"\n"
"QScrollBar:vertical {\n"
"  background-color: #484644;\n"
"  width: 16px;\n"
"  margin: 16px 2px 16px 2px;\n"
"  border: 1px solid #444444;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: #787878;\n"
"  border: 1px solid #787878;\n"
"  min-height: 8px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"  background-color: #969696;\n"
"  border: 1px solid #484644;\n"
"  border-radius: 4px;\n"
"  min-height: 8px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  w"
                        "idth: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_up_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_up.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"  background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: non"
                        "e;\n"
"}\n"
"\n"
"/* QTextEdit --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-specific-widgets\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTextEdit {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QTextEdit:selected {\n"
"  background: none;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* QPlainTextEdit ---------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QPlainTextEdit {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QPlainTextEdit:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QPlainTextEdit:selected {\n"
"  background: none;\n"
"  color"
                        ": #32414B;\n"
"}\n"
"\n"
"/* QSizeGrip --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsizegrip\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSizeGrip {\n"
"  background: transparent;\n"
"  width: 12px;\n"
"  height: 12px;\n"
"  image: url(\":/qss_icons/rc/window_grip.png\");\n"
"}\n"
"\n"
"/* QStackedWidget ---------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QStackedWidget {\n"
"  padding: 2px;\n"
"  border: 1px solid #32414B;\n"
"  border: 1px solid #19232D;\n"
"}\n"
"\n"
"/* QToolBar ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolBar {\n"
"  background-color: #32414B;\n"
"  border-bottom: 1px "
                        "solid #19232D;\n"
"  padding: 2px;\n"
"  font-weight: bold;\n"
"}\n"
"\n"
"QToolBar QToolButton {\n"
"  background-color: #32414B;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QToolBar QToolButton:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolBar QToolButton:checked {\n"
"  border: 1px solid #19232D;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QToolBar QToolButton:checked:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"  width: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_move_horizontal.png\");\n"
"}\n"
"\n"
"QToolBar::handle:vertical {\n"
"  height: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_move_horizontal.png\");\n"
"}\n"
"\n"
"QToolBar::separator:horizontal {\n"
"  width: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_separator_horizontal.png\");\n"
"}\n"
"\n"
"QToolBar::separator:vertical {\n"
"  height: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_separator_vertical.png\");\n"
"}\n"
"\n"
"QToolButton#qt_toolbar_ext_button {\n"
""
                        "  background: #32414B;\n"
"  border: 0px;\n"
"  color: #F0F0F0;\n"
"  image: url(\":/qss_icons/rc/arrow_right.png\");\n"
"}\n"
"\n"
"/* QAbstractSpinBox -------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QAbstractSpinBox {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  /* This fixes 103, 111 */\n"
"  padding-top: 2px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-bottom: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-radius: 4px;\n"
"  /* min-width: 5px; removed to fix 109 */\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button {\n"
"  background-color: transparent #19232D;\n"
"  subcontrol-origin: border;\n"
"  subcontrol-position: top right;\n"
"  border-left: 1px solid #32414B;\n"
"  margin: 1px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow, QAbstractSpinBox::up-arrow:disabled, QAbstractSpinBox::up-arrow:off {\n"
"  image: url(\":/qss_icons/rc/arrow_up_disab"
                        "led.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:hover {\n"
"  image: url(\":/qss_icons/rc/arrow_up.png\");\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button {\n"
"  background-color: transparent #19232D;\n"
"  subcontrol-origin: border;\n"
"  subcontrol-position: bottom right;\n"
"  border-left: 1px solid #32414B;\n"
"  margin: 1px;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow, QAbstractSpinBox::down-arrow:disabled, QAbstractSpinBox::down-arrow:off {\n"
"  image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:hover {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"}\n"
"\n"
"QAbstractSpinBox:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QAbstractSpinBox:selected {\n"
"  background: none;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* DISPLAYS --------------------------------"
                        "------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QLabel -----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLabel {\n"
"  background-color: #262626;\n"
"  border: 0px solid #32414B;\n"
"  padding: 2px;\n"
"  margin: 0px;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLabel::disabled {\n"
"  background-color: #262626;\n"
"  border: 0px solid #32414B;\n"
"  color: #787878;\n"
"}\n"
"\n"
"/* QTextBrowser -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qabstractscrollarea\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTextBrowser {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
""
                        "}\n"
"\n"
"QTextBrowser:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser:hover, QTextBrowser:!hover, QTextBrowser::selected, QTextBrowser::pressed {\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"/* QGraphicsView ----------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QGraphicsView {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QGraphicsView:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QGraphicsView:hover, QGraphicsView:!hover, QGraphicsView::selected, QGraphicsView::pressed {\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"/* QCalendarWidget --------------------------------------------------------\n"
"\n"
"-------------------------------"
                        "-------------------------------------------- */\n"
"QCalendarWidget QAbstractItemView {\n"
"    alternate-background-color: #484644;\n"
"    color: #F0F0F0;\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"    background-color: #262626;\n"
"    border: 0px solid #444444;\n"
"    padding: 0px;\n"
"    color: #FFFFFF;\n"
"    selection-background-color: #444444;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QCalendarWidget QWidget::item:selected {\n"
"    background-color: #1464A0;\n"
"}\n"
"\n"
"QCalendarWidget QWidget::item:hover {\n"
"    background-color: #148CD2;\n"
"    color: #32414B;\n"
"}\n"
"\n"
"QCalendarWidget {\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* QLCDNumber -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLCDNumber {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLCD"
                        "Number:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"/* QProgressBar -----------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qprogressbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QProgressBar {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"  background-color: none;\n"
"  color: #19232D;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QProgressBar::chunk:disabled {\n"
"  background-color: #14506E;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* BUTTONS --"
                        "-------------------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QPushButton ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qpushbutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QPushButton {\n"
"  background-color: #484644;\n"
"  border: 1px solid #605e5c;\n"
"  color: #FFFFFF;\n"
"  border-radius: 4px;\n"
"  padding: 3px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"  background-color: #323130;\n"
"  border: 1px solid #32414B;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"  padding: 3px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"  background-color: #32414B;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  padding: 3px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QPushButton:checked:disabled {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
""
                        "  color: #787878;\n"
"  border-radius: 4px;\n"
"  padding: 3px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QPushButton:checked:selected {\n"
"  background: none;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"QPushButton:checked:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: center right;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #323130;\n"
"}\n"
"QPushButton:pressed:hover {\n"
"  background-color: #323130;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #605e5c;\n"
"}\n"
"\n"
"QPushButton:selected {\n"
"  background: none;\n"
"  color: #32414B;\n"
"  border: 1px solid #444444;\n"
"}\n"
"\n"
"/* QToolButton ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbutton\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolButton {\n"
"  background-color: transpa"
                        "rent;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  padding: 2px;\n"
"  /* The subcontrols below are used only in the MenuButtonPopup mode */\n"
"  /* The subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"  background-color: transparent;\n"
"  border: 1px solid none;\n"
"}\n"
"\n"
"QToolButton:checked:disabled {\n"
"  border: 1px solid #14506E;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"  margin: 1px;\n"
"  background-color: transparent;\n"
"  border: 1px solid none;\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"  border: none;\n"
"}\n"
"\n"
"QToolButton:disabled:hover {\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] {\n"
"  padding: 2px;\n"
"  /* Only for MenuButtonPopup */\n"
"  padding-right: 12px;\n"
"  /* Make way for the popup button */\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] {\n"
" "
                        " padding: 2px;\n"
"  /* Only for InstantPopup */\n"
"  padding-right: 12px;\n"
"  /* Make way for the popup button */\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QToolButton::menu-button {\n"
"  padding: 2px;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"  border-top-right-radius: 4px;\n"
"  border-bottom-right-radius: 4px;\n"
"  /* 16px width + 4px for border = 20px allocated above */\n"
"  width: 16px;\n"
"  outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-button:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolButton::menu-button:checked:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolButton::menu-indicator {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  top: -8px;\n"
"  /* Shift it a bit */\n"
"  left: -4px;\n"
"  /* Shift it a bit */\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
""
                        "  border: 1px solid #32414B;\n"
"}\n"
"\n"
"/* QCommandLinkButton -----------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QCommandLinkButton {\n"
"  background-color: transparent;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QCommandLinkButton:disabled {\n"
"  background-color: transparent;\n"
"  color: #787878;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* INPUTS - NO FIELDS ----------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QComboBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QComboBox {\n"
"  bo"
                        "rder: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  selection-background-color: none;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  /* Fixes #103, #111 */\n"
"  min-height: 1.5em;\n"
"  /* padding-top: 2px;     removed to fix #132 */\n"
"  /* padding-bottom: 2px;  removed to fix #132 */\n"
"  /* min-width: 75px;      removed to fix #109 */\n"
"  /* Needed to remove indicator - fix #132 */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"  background-color: #19232D;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"  selection-color: #148CD2;\n"
"  selection-background-color: #32414B;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"  selection-background-color: #19232D;\n"
"}\n"
"\n"
"QComboBox::indicator {\n"
"  background-color: transparent;\n"
"  selection-background-color: transparent;\n"
"  color: transparent;\n"
"  selection-color: tran"
                        "sparent;\n"
"  /* Needed to remove indicator - fix #132 */\n"
"}\n"
"\n"
"QComboBox::indicator:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox::item:alternate {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QComboBox::item:checked {\n"
"  font-weight: bold;\n"
"}\n"
"\n"
"QComboBox::item:selected {\n"
"  border: 0px solid transparent;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 20px;\n"
"  border-left-width: 0px;\n"
"  border-left-color: #32414B;\n"
"  border-left-style: solid;\n"
"  border-top-right-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"  image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover, QComboBox::down-arrow:focus {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"}\n"
"\n"
"/* QSlider ---------------------------------------------------------"
                        "-------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qslider\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSlider:disabled {\n"
"  background: #19232D;\n"
"}\n"
"\n"
"QSlider:focus {\n"
"  border: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"  background: #32414B;\n"
"  border: 1px solid #32414B;\n"
"  height: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"  background: #32414B;\n"
"  border: 1px solid #32414B;\n"
"  width: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"  background: none;\n"
"  border: 1px solid #32414B;\n"
"  width: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical :disabled {\n"
"  background: #14506E;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"  background: none;\n"
"  border: 1px solid #32414B;\n"
"  height: 4px;\n"
"  margin: 0px;\n"
"  border-radius: 4px;\n"
"}\n"
""
                        "\n"
"QSlider::sub-page:horizontal:disabled {\n"
"  background: #14506E;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"  background: #787878;\n"
"  border: 1px solid #32414B;\n"
"  width: 8px;\n"
"  height: 8px;\n"
"  margin: -8px 0px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"  background: #148CD2;\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"  background: #787878;\n"
"  border: 1px solid #32414B;\n"
"  width: 8px;\n"
"  height: 8px;\n"
"  margin: 0 -8px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"  background: #148CD2;\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"/* QLineEdit --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlineedit\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLineEdit {\n"
"  background-color: #262626;\n"
"  padding-top: 2px;\n"
"  /* This QLineEdit fi"
                        "x  103, 111 */\n"
"  padding-bottom: 2px;\n"
"  /* This QLineEdit fix  103, 111 */\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-style: solid;\n"
"  border: 1px solid #605e5c;\n"
"  border-radius: 4px;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"  background-color: #323130;\n"
"  color: #787878;\n"
"  border: 1px solid #444444;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"  border: 1px solid #969696;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLineEdit:selected {\n"
"  background: #969696;\n"
"  border: 1px solid #969696;\n"
"}\n"
"\n"
"/* QTabWiget --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTabWidget {\n"
"  padding: 2px;\n"
"  selection-background-color: #32414B;\n"
"  /* Add wanted borders - fix #141, #126, #123 */\n"
"}\n"
"\n"
"QTabWidget QWidget {\n"
"  background-color: #363636;\n"
""
                        "  border: 0px solid #605e5c;\n"
"}\n"
"\n"
"QTabWidget QPushButton {\n"
"  background-color: #484644;\n"
"  border: 1px solid #605e5c;\n"
"}\n"
"\n"
"QTabWidget QPushButton::pressed {\n"
"  border: 1px solid #444444;\n"
"}\n"
"\n"
"QTabWidget QPushButton::disabled {\n"
"  border: 1px solid #444444;\n"
"}\n"
"\n"
"QTabWidget QScrollArea {\n"
"  background-color: #484644;\n"
"}\n"
"\n"
"QTabWidget QWidget QWidget\n"
"QTableView,\n"
"QTabWidget QTreeView,\n"
"QTabWidget QListView,\n"
"QTabWidget QGroupBox,\n"
"QTabWidget QLineEdit,\n"
"QTabWidget QComboBox,\n"
"QTabWidget QFontComboBox,\n"
"QTabWidget QTextEdit,\n"
"QTabWidget QSpinBox,\n"
"QTabWidget QDoubleSpinBox {\n"
"  border: 1px solid #444444;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"  border: 1px solid #605e5c;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  /* Fixes double border inside pane wit pyqt5 */\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabWidget::pane:selected {\n"
"  background-color: #FFFFFF;\n"
"  border: 1px solid #605e5c;\n"
"}\n"
"\n"
"/* QTabB"
                        "ar ----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTabBar {\n"
"  qproperty-drawBase: 0;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  padding: 2px;\n"
"  border: 0;\n"
"  /* left: 5px; move to the right by 5px - removed for fix */\n"
"}\n"
"\n"
"QTabBar::close-button {\n"
"  border: 0;\n"
"  margin: 2px;\n"
"  padding: 2px;\n"
"  image: url(\":/qss_icons/rc/window_close.png\");\n"
"}\n"
"\n"
"QTabBar::close-button:hover {\n"
"  image: url(\":/qss_icons/rc/window_close_focus.png\");\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"  image: url(\":/qss_icons/rc/window_close_pressed.png\");\n"
"}\n"
"\n"
"/* QTabBar::tab - selected ------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"----------------------------"
                        "----------------------------------------------- */\n"
"\n"
"QTabBar::tab {\n"
"  color: #FFFFFF;\n"
"  background-color: #323130;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  padding-top: 12px;\n"
"  padding-bottom: 12px;\n"
"  border-top-left-radius: 4px;\n"
"  border-bottom-left-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"  color: #F0F0F0;\n"
"  background-color: #484644;\n"
"  border-right: 3px solid #FFFFFF;\n"
"}\n"
"\n"
"QTabBar::tab:selected:hover {\n"
"  border-right: 3px solid #FFFFFF;\n"
"  border-top-right-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"  border-right: 3px solid #FFFFFF;\n"
"  border-top-right-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:disabled {\n"
"  border-left: 3px solid #252424;\n"
"  color: #787878;\n"
"  background-color: #252424;\n"
"}\n"
"\n"
"QTabBar QToolButton {\n"
"  /* Fixes #136 */\n"
"  background-color: "
                        "#FFFFFF;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:enabled {\n"
"  image: url(\":/qss_icons/rc/arrow_left.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:disabled {\n"
"  image: url(\":/qss_icons/rc/arrow_left_disabled.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"  image: url(\":/qss_icons/rc/arrow_right.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"  image: url(\":/qss_icons/rc/arrow_right_disabled.png\");\n"
"}\n"
"\n"
"/* QDockWiget -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QDockWidget {\n"
"  outline: 1px solid #32414B;\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  titlebar-close-icon: url(\":/qss_icons/rc/window_close.png\");\n"
"  titlebar-normal-icon: url(\":/qss_icons/rc/window_undock.png\");\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"  /* Bette"
                        "r size for title bar */\n"
"  padding: 6px;\n"
"  border: none;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QDockWidget::close-button {\n"
"  background-color: #32414B;\n"
"  border-radius: 4px;\n"
"  border: none;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover {\n"
"  image: url(\":/qss_icons/rc/window_close_focus.png\");\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed {\n"
"  image: url(\":/qss_icons/rc/window_close_pressed.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button {\n"
"  background-color: #32414B;\n"
"  border-radius: 4px;\n"
"  border: none;\n"
"}\n"
"\n"
"QDockWidget::float-button:hover {\n"
"  image: url(\":/qss_icons/rc/window_undock_focus.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button:pressed {\n"
"  image: url(\":/qss_icons/rc/window_undock_pressed.png\");\n"
"}\n"
"\n"
"/* QTreeView QListView QTableView -----------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtreeview\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-"
                        "qlistview\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtableview\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTreeView:branch:selected, QTreeView:branch:hover {\n"
"  background: url(\":/qss_icons/rc/transparent.png\");\n"
"}\n"
"\n"
"QTreeView:branch:has-siblings:!adjoins-item {\n"
"  border-image: url(\":/qss_icons/rc/branch_line.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:has-siblings:adjoins-item {\n"
"  border-image: url(\":/qss_icons/rc/branch_more.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:!has-children:!has-siblings:adjoins-item {\n"
"  border-image: url(\":/qss_icons/rc/branch_end.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:has-children:!has-siblings:closed, QTreeView:branch:closed:has-children:has-siblings {\n"
"  border-image: none;\n"
"  image: url(\":/qss_icons/rc/branch_closed.png\");\n"
"}\n"
"\n"
"QTreeView:branch:open:has-children:!has-siblings, QTreeView:branch:open:has-children:has-siblings {\n"
"  border-image: none;\n"
"  image"
                        ": url(\":/qss_icons/rc/branch_open.png\");\n"
"}\n"
"\n"
"QTreeView:branch:has-children:!has-siblings:closed:hover, QTreeView:branch:closed:has-children:has-siblings:hover {\n"
"  image: url(\":/qss_icons/rc/branch_closed_focus.png\");\n"
"}\n"
"\n"
"QTreeView:branch:open:has-children:!has-siblings:hover, QTreeView:branch:open:has-children:has-siblings:hover {\n"
"  image: url(\":/qss_icons/rc/branch_open_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:checked,\n"
"QListView::indicator:checked {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:checked:hover, QTreeView::indicator:checked:focus, QTreeView::indicator:checked:pressed,\n"
"QListView::indicator:checked:hover,\n"
"QListView::indicator:checked:focus,\n"
"QListView::indicator:checked:pressed {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:unchecked,\n"
"QListView::indicator:unchecked {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked.png\");\n"
"}"
                        "\n"
"\n"
"QTreeView::indicator:unchecked:hover, QTreeView::indicator:unchecked:focus, QTreeView::indicator:unchecked:pressed,\n"
"QListView::indicator:unchecked:hover,\n"
"QListView::indicator:unchecked:focus,\n"
"QListView::indicator:unchecked:pressed {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:indeterminate,\n"
"QListView::indicator:indeterminate {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:indeterminate:hover, QTreeView::indicator:indeterminate:focus, QTreeView::indicator:indeterminate:pressed,\n"
"QListView::indicator:indeterminate:hover,\n"
"QListView::indicator:indeterminate:focus,\n"
"QListView::indicator:indeterminate:pressed {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate_focus.png\");\n"
"}\n"
"\n"
"QTreeView,\n"
"QListView,\n"
"QTableView,\n"
"QColumnView {\n"
"  background-color: #484644;\n"
"  alternate-background-color: #262626;\n"
"  color: #F0F0F0;\n"
"  /* gridline-"
                        "color: #FFFFFF; */\n"
"  /* border-radius: 4px; */\n"
"}\n"
"\n"
"QTreeView:disabled,\n"
"QListView:disabled,\n"
"QTableView:disabled,\n"
"QColumnView:disabled {\n"
"  background-color: #363636;\n"
"  alternate-background-color: #262626;\n"
"  color: #787878;\n"
"}\n"
"\n"
"QTreeView:selected,\n"
"QListView:selected,\n"
"QTableView:selected,\n"
"QColumnView:selected {\n"
"  background: #484644;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"QTreeView::hover,\n"
"QListView::hover,\n"
"QTableView::hover,\n"
"QColumnView::hover {\n"
"  background-color: #363636;\n"
"  border: 1px solid #969696;\n"
"}\n"
"\n"
"QTreeView::item:pressed,\n"
"QListView::item:pressed,\n"
"QTableView::item:pressed,\n"
"QColumnView::item:pressed {\n"
"  background-color: #969696;\n"
"}\n"
"\n"
"QTreeView::item:selected:hover,\n"
"QListView::item:selected:hover,\n"
"QTableView::item:selected:hover,\n"
"QColumnView::item:selected:hover {\n"
"  background: #969696;\n"
"  color: #363636;\n"
"}\n"
"\n"
"QTreeView::item:selected:active,\n"
"QListView::i"
                        "tem:selected:active,\n"
"QTableView::item:selected:active,\n"
"QColumnView::item:selected:active {\n"
"  background-color: #969696;\n"
"}\n"
"\n"
"QTreeView::item:selected:disabled,\n"
"QListView::item:selected:disabled,\n"
"QTableView::item:selected:disabled,\n"
"QColumnView::item:selected:disabled {\n"
"  background-color: #969696;\n"
"}\n"
"\n"
"QTreeView::item:!selected:hover,\n"
"QListView::item:!selected:hover,\n"
"QTableView::item:!selected:hover,\n"
"QColumnView::item:!selected:hover {\n"
"  outline: 0;\n"
"  color: #ffffff;\n"
"  background-color: #605e5c;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"  background-color: #363636;\n"
"  border: 1px transparent #969696;\n"
"  border-radius: 0px;\n"
"}\n"
"\n"
"/* QHeaderView ------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qheaderview\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QHeaderView {\n"
"  background-color: #484644;"
                        "\n"
"  border: 0px transparent;\n"
"  padding: 0px;\n"
"  margin: 0px;\n"
"  border-radius: 0px;\n"
"}\n"
"\n"
"QHeaderView:disabled {\n"
"  background-color: #32414B;\n"
"  border: 0px transparent;\n"
"  padding: 2px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"  background-color: #484644;\n"
"  color: #F0F0F0;\n"
"  padding: 2px;\n"
"  border-radius: 0px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"\n"
"\n"
"QHeaderView::down-arrow {\n"
"  /* Those settings (border/width/height/background-color) solve bug */\n"
"  /* transparent arrow background and size */\n"
"  background-color: #32414B;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"  background-color: #32414B;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  image: url(\":/qss_icons/rc/arrow_up.png\");\n"
"}\n"
"\n"
"/* QToolBox --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbox\n"
"\n"
"--"
                        "------------------------------------------------------------------------- */\n"
"QToolBox {\n"
"  padding: 0px;\n"
"  border: 0px;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QToolBox::selected {\n"
"  padding: 0px;\n"
"  border: 2px solid none;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"  background-color: #19232D;\n"
"  border: 1px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QToolBox::tab:disabled {\n"
"  color: #787878;\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"  background-color: #505F69;\n"
"  border-bottom: 2px solid none;\n"
"}\n"
"\n"
"QToolBox::tab:selected:disabled {\n"
"  background-color: #32414B;\n"
"  border-bottom: 2px solid #14506E;\n"
"}\n"
"\n"
"QToolBox::tab:!selected {\n"
"  background-color: #32414B;\n"
"  border-bottom: 2px solid #32414B;\n"
"}\n"
"\n"
"QToolBox::tab:!selected:disabled {\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"  border-color: #148CD2;\n"
"  border-bottom: 2px sol"
                        "id #148CD2;\n"
"}\n"
"\n"
"QToolBox QScrollArea QWidget QWidget {\n"
"  padding: 0px;\n"
"  border: 0px;\n"
"  background-color: #262626;\n"
"}\n"
"\n"
"/* QFrame -----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe\n"
"\n"
"--------------------------------------------------------------------------- */\n"
".QFrame {\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
".QFrame[frameShape=\"0\"] {\n"
"  border-radius: 4px;\n"
"  border: 1px transparent #32414B;\n"
"}\n"
"\n"
".QFrame[height=\"3\"], .QFrame[width=\"3\"] {\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"/* QSplitter --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsplitter\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSplitter {\n"
"  background-color: #32414B;\n"
"  spacing: 0px;\n"
"  padding: 0px;\n"
"  marg"
                        "in: 0px;\n"
"}\n"
"\n"
"QSplitter::separator {\n"
"  background-color: #32414B;\n"
"  border: 0px solid #19232D;\n"
"  spacing: 0px;\n"
"  padding: 1px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QSplitter::separator:hover {\n"
"  background-color: #787878;\n"
"}\n"
"\n"
"QSplitter::separator:horizontal {\n"
"  width: 5px;\n"
"  image: url(\":/qss_icons/rc/line_vertical.png\");\n"
"}\n"
"\n"
"QSplitter::separator:vertical {\n"
"  height: 5px;\n"
"  image: url(\":/qss_icons/rc/line_horizontal.png\");\n"
"}\n"
"\n"
"/* QDateEdit --------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QDateEdit {\n"
"  selection-background-color: none;\n"
"  border-style: solid;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-top: 2px;\n"
"  /* This fixes 103, 111 */\n"
"  padding-bottom: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  min-width: 10px;\n"
"}\n"
"\n"
"QDat"
                        "eEdit:on {\n"
"  selection-background-color: none;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 20px;\n"
"  border-top-right-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"  image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow:on, QDateEdit::down-arrow:hover, QDateEdit::down-arrow:focus {\n"
"  image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"}\n"
"\n"
"QDateEdit QAbstractItemView {\n"
"  background-color: #19232D;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"  selection-background-color: none;\n"
"}\n"
"\n"
"QAbstractView:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QAbstractView:selected {\n"
"  background: none;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"PlotWidget {\n"
"  /* Fix cut labels in plots #134 */\n"
"  padding: 0px;\n"
"}")
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
        self.titreLineEdit.setGeometry(QRect(12, 25, 281, 29))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titreLineEdit.sizePolicy().hasHeightForWidth())
        self.titreLineEdit.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(12)
        self.titreLineEdit.setFont(font)
        self.titreLineEdit.setAlignment(Qt.AlignCenter)
        self.titreLineEdit.setClearButtonEnabled(True)
        self.soustitreGroupBox = QGroupBox(self.infoGroupBox)
        self.soustitreGroupBox.setObjectName(u"soustitreGroupBox")
        self.soustitreGroupBox.setEnabled(True)
        self.soustitreGroupBox.setGeometry(QRect(10, 80, 300, 61))
        self.soustitreLineEdit = AdvancedLineEdit(self.soustitreGroupBox)
        self.soustitreLineEdit.setObjectName(u"soustitreLineEdit")
        self.soustitreLineEdit.setGeometry(QRect(12, 25, 281, 29))
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
        self.matToolButton = QPushButton(self.matGroupBox)
        self.matToolButton.setObjectName(u"matToolButton")
        self.matToolButton.setGeometry(QRect(106, 25, 20, 29))
        self.matToolButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.matToolButton.raise_()
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
        self.numToolButton = QPushButton(self.numGroupBox)
        self.numToolButton.setObjectName(u"numToolButton")
        self.numToolButton.setGeometry(QRect(106, 25, 21, 29))
        self.numToolButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.numToolButton.raise_()
        self.numLineEdit.raise_()
        self.sectionGroupBox = QGroupBox(self.infoGroupBox)
        self.sectionGroupBox.setObjectName(u"sectionGroupBox")
        self.sectionGroupBox.setGeometry(QRect(10, 290, 300, 61))
        self.sectionNumLabel = QLabel(self.sectionGroupBox)
        self.sectionNumLabel.setObjectName(u"sectionNumLabel")
        self.sectionNumLabel.setGeometry(QRect(20, 24, 47, 31))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(14)
        font1.setUnderline(True)
        self.sectionNumLabel.setFont(font1)
        self.sectionNumLabel.setStyleSheet(u"")
        self.sectionLineEdit = AdvancedLineEdit(self.sectionGroupBox)
        self.sectionLineEdit.setObjectName(u"sectionLineEdit")
        self.sectionLineEdit.setGeometry(QRect(40, 25, 251, 29))
        sizePolicy1.setHeightForWidth(self.sectionLineEdit.sizePolicy().hasHeightForWidth())
        self.sectionLineEdit.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(12)
        font2.setUnderline(True)
        self.sectionLineEdit.setFont(font2)
        self.sectionLineEdit.setMaxLength(32767)
        self.sectionLineEdit.setAlignment(Qt.AlignCenter)
        self.sectionLineEdit.setClearButtonEnabled(True)
        self.pathPathLabel = QLabel(self.genTab)
        self.pathPathLabel.setObjectName(u"pathPathLabel")
        self.pathPathLabel.setGeometry(QRect(350, 170, 321, 211))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pathPathLabel.sizePolicy().hasHeightForWidth())
        self.pathPathLabel.setSizePolicy(sizePolicy2)
        self.pathPathLabel.setMaximumSize(QSize(321, 16777215))
        font3 = QFont()
        font3.setUnderline(True)
        self.pathPathLabel.setFont(font3)
        self.pathPathLabel.setCursor(QCursor(Qt.ArrowCursor))
        self.pathPathLabel.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.pathPathLabel.setWordWrap(True)
        self.pathPathLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.infoPersoGroupBox = QGroupBox(self.genTab)
        self.infoPersoGroupBox.setObjectName(u"infoPersoGroupBox")
        self.infoPersoGroupBox.setGeometry(QRect(350, 10, 319, 151))
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.infoPersoGroupBox.sizePolicy().hasHeightForWidth())
        self.infoPersoGroupBox.setSizePolicy(sizePolicy3)
        self.infoPersoGroupBox.setMinimumSize(QSize(0, 0))
        self.auteurPersoGroupBox = QGroupBox(self.infoPersoGroupBox)
        self.auteurPersoGroupBox.setObjectName(u"auteurPersoGroupBox")
        self.auteurPersoGroupBox.setGeometry(QRect(10, 20, 291, 61))
        self.auteurPersoLabel = QLabel(self.auteurPersoGroupBox)
        self.auteurPersoLabel.setObjectName(u"auteurPersoLabel")
        self.auteurPersoLabel.setGeometry(QRect(10, 25, 271, 31))
        font4 = QFont()
        font4.setFamily(u"Times New Roman")
        font4.setPointSize(18)
        font4.setItalic(True)
        self.auteurPersoLabel.setFont(font4)
        self.auteurPersoLabel.setTextFormat(Qt.RichText)
        self.auteurPersoLabel.setScaledContents(False)
        self.auteurPersoLabel.setAlignment(Qt.AlignCenter)
        self.niveauPersoGroupBox = QGroupBox(self.infoPersoGroupBox)
        self.niveauPersoGroupBox.setObjectName(u"niveauPersoGroupBox")
        self.niveauPersoGroupBox.setGeometry(QRect(10, 80, 291, 61))
        self.niveauPersoLabel = QLabel(self.niveauPersoGroupBox)
        self.niveauPersoLabel.setObjectName(u"niveauPersoLabel")
        self.niveauPersoLabel.setGeometry(QRect(10, 25, 271, 31))
        font5 = QFont()
        font5.setFamily(u"Times New Roman")
        font5.setPointSize(17)
        font5.setItalic(True)
        self.niveauPersoLabel.setFont(font5)
        self.niveauPersoLabel.setTextFormat(Qt.RichText)
        self.niveauPersoLabel.setScaledContents(True)
        self.niveauPersoLabel.setAlignment(Qt.AlignCenter)
        self.niveauPersoLabel.setWordWrap(False)
        self.horizontalLayoutWidget = QWidget(self.genTab)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(340, 390, 331, 51))
        self.genButtonLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.genButtonLayout.setObjectName(u"genButtonLayout")
        self.genButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.genPushButton = QPushButton(self.horizontalLayoutWidget)
        self.genPushButton.setObjectName(u"genPushButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.genPushButton.sizePolicy().hasHeightForWidth())
        self.genPushButton.setSizePolicy(sizePolicy4)
        self.genPushButton.setMinimumSize(QSize(150, 0))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.genPushButton.setFont(font6)
        self.genPushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.genButtonLayout.addWidget(self.genPushButton)

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
        self.tabWidget.addTab(self.genTab, "")
        self.configTab = QWidget()
        self.configTab.setObjectName(u"configTab")
        self.infoPerso = QGroupBox(self.configTab)
        self.infoPerso.setObjectName(u"infoPerso")
        self.infoPerso.setGeometry(QRect(10, 10, 307, 161))
        self.auteurConfig = QGroupBox(self.infoPerso)
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
        self.niveauConfig = QGroupBox(self.infoPerso)
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
        font7 = QFont()
        font7.setPointSize(12)
        self.configSaveButton.setFont(font7)
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
        self.modelWikiLink.setGeometry(QRect(16, 409, 280, 31))
        self.modelWikiLink.setFont(font7)
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
        self.formLayoutWidget_2.setGeometry(QRect(10, 30, 431, 230))
        self.modelValuesFormLayout = QFormLayout(self.formLayoutWidget_2)
        self.modelValuesFormLayout.setObjectName(u"modelValuesFormLayout")
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
        font8 = QFont()
        font8.setFamily(u"Consolas")
        self.titreModelCheckBox.setFont(font8)
        self.titreModelCheckBox.setChecked(True)

        self.modelValuesFormLayout.setWidget(0, QFormLayout.LabelRole, self.titreModelCheckBox)

        self.soustitreModelCheckBox = QCheckBox(self.formLayoutWidget_2)
        self.soustitreModelCheckBox.setObjectName(u"soustitreModelCheckBox")
        self.soustitreModelCheckBox.setFont(font8)
        self.soustitreModelCheckBox.setChecked(True)

        self.modelValuesFormLayout.setWidget(1, QFormLayout.LabelRole, self.soustitreModelCheckBox)

        self.matiereModelCheckBox = QCheckBox(self.formLayoutWidget_2)
        self.matiereModelCheckBox.setObjectName(u"matiereModelCheckBox")
        self.matiereModelCheckBox.setFont(font8)
        self.matiereModelCheckBox.setChecked(True)

        self.modelValuesFormLayout.setWidget(2, QFormLayout.LabelRole, self.matiereModelCheckBox)

        self.numeroModelCheckBox = QCheckBox(self.formLayoutWidget_2)
        self.numeroModelCheckBox.setObjectName(u"numeroModelCheckBox")
        self.numeroModelCheckBox.setFont(font8)
        self.numeroModelCheckBox.setChecked(True)

        self.modelValuesFormLayout.setWidget(3, QFormLayout.LabelRole, self.numeroModelCheckBox)

        self.sectionModelCheckBox = QCheckBox(self.formLayoutWidget_2)
        self.sectionModelCheckBox.setObjectName(u"sectionModelCheckBox")
        self.sectionModelCheckBox.setFont(font8)
        self.sectionModelCheckBox.setChecked(True)

        self.modelValuesFormLayout.setWidget(4, QFormLayout.LabelRole, self.sectionModelCheckBox)

        self.auteurModelCheckBox = QCheckBox(self.formLayoutWidget_2)
        self.auteurModelCheckBox.setObjectName(u"auteurModelCheckBox")
        self.auteurModelCheckBox.setFont(font8)
        self.auteurModelCheckBox.setChecked(True)

        self.modelValuesFormLayout.setWidget(5, QFormLayout.LabelRole, self.auteurModelCheckBox)

        self.niveauModelCheckBox = QCheckBox(self.formLayoutWidget_2)
        self.niveauModelCheckBox.setObjectName(u"niveauModelCheckBox")
        self.niveauModelCheckBox.setFont(font8)
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
        self.modelPathModelLabel.setFont(font8)
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
        self.modelDefaultPushButton.setGeometry(QRect(220, 370, 111, 21))
        self.modelDefaultPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.modelApplyPushButton = QPushButton(self.modelTab)
        self.modelApplyPushButton.setObjectName(u"modelApplyPushButton")
        self.modelApplyPushButton.setEnabled(True)
        self.modelApplyPushButton.setGeometry(QRect(470, 370, 201, 61))
        self.modelApplyPushButton.setFont(font7)
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

        self.tabWidget.setCurrentIndex(1)


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
        self.matToolButton.setText("")
        self.numGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Num\u00e9ro", None))
        self.numLineEdit.setText("")
        self.numLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0624", None))
        self.numToolButton.setText("")
        self.sectionGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Premi\u00e8re Section", None))
        self.sectionNumLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; text-decoration: underline;\">1.</span></p></body></html>", None))
        self.sectionLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"La Loi de l'Inertie", None))
        self.pathPathLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"none\"><span style=\" font-size:11pt; text-decoration: underline; color:#f0f0f0;\">Aucun chemin de sauvegarde</span></a></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.infoPersoGroupBox.setToolTip(QCoreApplication.translate("MainWindow", u"Pour modifier les informations, veuillez aller dans le Configurateur", None))
#endif // QT_CONFIG(tooltip)
        self.infoPersoGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Informations Personnelles", None))
        self.auteurPersoGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Auteur", None))
        self.auteurPersoLabel.setText(QCoreApplication.translate("MainWindow", u"Auteur", None))
        self.niveauPersoGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Niveau", None))
        self.niveauPersoLabel.setText(QCoreApplication.translate("MainWindow", u"Niveau", None))
        self.genPushButton.setText(QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rer", None))
        self.modelGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mod\u00e8le", None))
        self.modelLineEdit.setText("")
        self.modelLineEdit.setPlaceholderText("")
        self.modelToolButton.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.genTab), QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rateur", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.genTab), QCoreApplication.translate("MainWindow", u"Cr\u00e9er un document", None))
#endif // QT_CONFIG(tooltip)
        self.infoPerso.setTitle(QCoreApplication.translate("MainWindow", u"Informations Personnelles", None))
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

