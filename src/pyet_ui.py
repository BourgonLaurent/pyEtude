# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyEtude.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(728, 471)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(728, 471))
        MainWindow.setMaximumSize(QtCore.QSize(728, 471))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("QWidget {\n"
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
"QMainWindow::separator:hover {\n"
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
"/* QStatusBar -------------------------------------------------------------\n"
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
"  height: 16px;\n"
"  width: 16px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover, QCheckBox::indicator:unchecked:focus, QCheckBox::indicator:unchecked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover, QCheckBox::indicator:checked:focus, QCheckBox::indicator:checked:pressed {\n"
"  border: none;\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:disabled {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate_disabled.png\");\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus, QCheckBox::indicator:indeterminate:hover, QCheckBox::indicator:indeterminate:pressed {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate_focus.png\");\n"
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
"  left: 3px;\n"
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
"QRadioButton::indicator:checked:hover, QRadioButton::indicator:checked:focus, QRadioButton::indicator:checked:pressed {\n"
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
"  border: 0px solid #32414B;\n"
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
"  border: 0px solid #32414B;\n"
"  color: #F0F0F0;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"  height: 1px;\n"
"  background-color: #505F69;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QMenu::icon {\n"
"  margin: 0px;\n"
"  padding-left: 4px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"  background-color: #32414B;\n"
"  padding: 4px 24px 4px 24px;\n"
"  /* Reserve space for selection border */\n"
"  border: 1px transparent #32414B;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"  width: 12px;\n"
"  height: 12px;\n"
"  padding-left: 6px;\n"
"  /* non-exclusive indicator = check box style indicator (see QActionGroup::setExclusive) */\n"
"  /* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked {\n"
"  image: url(\":/qss_icons/rc/radio_unchecked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"  image: url(\":/qss_icons/rc/radio_unchecked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"  image: url(\":/qss_icons/rc/radio_checked.png\");\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected {\n"
"  image: url(\":/qss_icons/rc/radio_checked_disabled.png\");\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"  margin: 5px;\n"
"  image: url(\":/qss_icons/rc/arrow_right.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"/* QAbstractItemView ------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qcombobox\n"
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
"--------------------------------------------------------------------------- */\n"
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
"  width: 12px;\n"
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
"  background: none;\n"
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
"  color: #32414B;\n"
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
"  border-bottom: 1px solid #19232D;\n"
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
"  image: url(\":/qss_icons/rc/arrow_up_disabled.png\");\n"
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
"/* DISPLAYS --------------------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"/* QLabel -----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qframe\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLabel {\n"
"  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 2px;\n"
"  margin: 0px;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLabel::disabled {\n"
"  background-color: #19232D;\n"
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
"--------------------------------------------------------------------------- */\n"
"QCalendarWidget {\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QCalendarWidget:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
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
"QLCDNumber:disabled {\n"
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
"/* BUTTONS ---------------------------------------------------------------- */\n"
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
"  background-color: transparent;\n"
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
"  padding: 2px;\n"
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
"  border: 1px solid #32414B;\n"
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
"  selection-color: transparent;\n"
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
"/* QSlider ----------------------------------------------------------------\n"
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
"  background-color: #19232D;\n"
"  padding-top: 2px;\n"
"  /* This QLineEdit fix  103, 111 */\n"
"  padding-bottom: 2px;\n"
"  /* This QLineEdit fix  103, 111 */\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-style: solid;\n"
"  border: 1px solid #3c65a4;\n"
"  border-radius: 4px;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"  background-color: #323130;\n"
"  color: #787878;\n"
"  border: 1px solid #444444;\n"
"  border-right: 0px solid;\n"
"  border-top-right-radius: 0px;\n"
"  border-bottom-right-radius: 0px;\n"
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
"/* QTabBar ----------------------------------------------------------------\n"
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
"--------------------------------------------------------------------------- */\n"
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
"  background-color: #FFFFFF;\n"
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
"  /* Better size for title bar */\n"
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
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlistview\n"
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
"  image: url(\":/qss_icons/rc/branch_open.png\");\n"
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
"}\n"
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
"  /* gridline-color: #FFFFFF; */\n"
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
"QListView::item:selected:active,\n"
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
"  background-color: #484644;\n"
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
"--------------------------------------------------------------------------- */\n"
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
"  border-bottom: 2px solid #148CD2;\n"
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
"  margin: 0px;\n"
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
"QDateEdit:on {\n"
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
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 711, 451))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setObjectName("tabWidget")
        self.genTab = QtWidgets.QWidget()
        self.genTab.setObjectName("genTab")
        self.infoGroupBox = QtWidgets.QGroupBox(self.genTab)
        self.infoGroupBox.setGeometry(QtCore.QRect(10, 10, 321, 371))
        self.infoGroupBox.setObjectName("infoGroupBox")
        self.titreGroupBox = QtWidgets.QGroupBox(self.infoGroupBox)
        self.titreGroupBox.setGeometry(QtCore.QRect(10, 20, 291, 61))
        self.titreGroupBox.setObjectName("titreGroupBox")
        self.titreLineEdit = QtWidgets.QLineEdit(self.titreGroupBox)
        self.titreLineEdit.setGeometry(QtCore.QRect(12, 25, 269, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titreLineEdit.sizePolicy().hasHeightForWidth())
        self.titreLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        self.titreLineEdit.setFont(font)
        self.titreLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.titreLineEdit.setClearButtonEnabled(True)
        self.titreLineEdit.setObjectName("titreLineEdit")
        self.soustitreGroupBox = QtWidgets.QGroupBox(self.infoGroupBox)
        self.soustitreGroupBox.setGeometry(QtCore.QRect(10, 80, 291, 61))
        self.soustitreGroupBox.setObjectName("soustitreGroupBox")
        self.soustitreLineEdit = QtWidgets.QLineEdit(self.soustitreGroupBox)
        self.soustitreLineEdit.setGeometry(QtCore.QRect(12, 25, 269, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.soustitreLineEdit.sizePolicy().hasHeightForWidth())
        self.soustitreLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        self.soustitreLineEdit.setFont(font)
        self.soustitreLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.soustitreLineEdit.setClearButtonEnabled(True)
        self.soustitreLineEdit.setObjectName("soustitreLineEdit")
        self.matGroupBox = QtWidgets.QGroupBox(self.infoGroupBox)
        self.matGroupBox.setGeometry(QtCore.QRect(100, 150, 131, 61))
        self.matGroupBox.setObjectName("matGroupBox")
        self.matLineEdit = QtWidgets.QLineEdit(self.matGroupBox)
        self.matLineEdit.setEnabled(False)
        self.matLineEdit.setGeometry(QtCore.QRect(10, 25, 98, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matLineEdit.sizePolicy().hasHeightForWidth())
        self.matLineEdit.setSizePolicy(sizePolicy)
        self.matLineEdit.setMinimumSize(QtCore.QSize(0, 29))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        self.matLineEdit.setFont(font)
        self.matLineEdit.setText("")
        self.matLineEdit.setFrame(True)
        self.matLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.matLineEdit.setClearButtonEnabled(False)
        self.matLineEdit.setObjectName("matLineEdit")
        self.matToolButton = QtWidgets.QPushButton(self.matGroupBox)
        self.matToolButton.setGeometry(QtCore.QRect(101, 25, 20, 29))
        self.matToolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.matToolButton.setText("")
        self.matToolButton.setObjectName("matToolButton")
        self.matToolButton.raise_()
        self.matLineEdit.raise_()
        self.numGroupBox = QtWidgets.QGroupBox(self.infoGroupBox)
        self.numGroupBox.setGeometry(QtCore.QRect(100, 210, 131, 61))
        self.numGroupBox.setObjectName("numGroupBox")
        self.numLineEdit = QtWidgets.QLineEdit(self.numGroupBox)
        self.numLineEdit.setEnabled(False)
        self.numLineEdit.setGeometry(QtCore.QRect(10, 25, 98, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numLineEdit.sizePolicy().hasHeightForWidth())
        self.numLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        self.numLineEdit.setFont(font)
        self.numLineEdit.setText("")
        self.numLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.numLineEdit.setClearButtonEnabled(False)
        self.numLineEdit.setObjectName("numLineEdit")
        self.numToolButton = QtWidgets.QPushButton(self.numGroupBox)
        self.numToolButton.setGeometry(QtCore.QRect(101, 25, 21, 29))
        self.numToolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.numToolButton.setText("")
        self.numToolButton.setObjectName("numToolButton")
        self.numToolButton.raise_()
        self.numLineEdit.raise_()
        self.sectionGroupBox = QtWidgets.QGroupBox(self.infoGroupBox)
        self.sectionGroupBox.setGeometry(QtCore.QRect(10, 300, 291, 61))
        self.sectionGroupBox.setObjectName("sectionGroupBox")
        self.sectionNumLabel = QtWidgets.QLabel(self.sectionGroupBox)
        self.sectionNumLabel.setGeometry(QtCore.QRect(20, 24, 47, 31))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        font.setUnderline(True)
        self.sectionNumLabel.setFont(font)
        self.sectionNumLabel.setStyleSheet("")
        self.sectionNumLabel.setObjectName("sectionNumLabel")
        self.sectionLineEdit = QtWidgets.QLineEdit(self.sectionGroupBox)
        self.sectionLineEdit.setGeometry(QtCore.QRect(40, 25, 241, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sectionLineEdit.sizePolicy().hasHeightForWidth())
        self.sectionLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        font.setUnderline(True)
        self.sectionLineEdit.setFont(font)
        self.sectionLineEdit.setMaxLength(32767)
        self.sectionLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.sectionLineEdit.setClearButtonEnabled(True)
        self.sectionLineEdit.setObjectName("sectionLineEdit")
        self.pathPathLabel = QtWidgets.QLabel(self.genTab)
        self.pathPathLabel.setGeometry(QtCore.QRect(350, 170, 321, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pathPathLabel.sizePolicy().hasHeightForWidth())
        self.pathPathLabel.setSizePolicy(sizePolicy)
        self.pathPathLabel.setMaximumSize(QtCore.QSize(321, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.pathPathLabel.setFont(font)
        self.pathPathLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pathPathLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.pathPathLabel.setWordWrap(True)
        self.pathPathLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.pathPathLabel.setObjectName("pathPathLabel")
        self.infoPersoGroupBox = QtWidgets.QGroupBox(self.genTab)
        self.infoPersoGroupBox.setGeometry(QtCore.QRect(350, 10, 319, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoPersoGroupBox.sizePolicy().hasHeightForWidth())
        self.infoPersoGroupBox.setSizePolicy(sizePolicy)
        self.infoPersoGroupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.infoPersoGroupBox.setObjectName("infoPersoGroupBox")
        self.auteurPersoGroupBox = QtWidgets.QGroupBox(self.infoPersoGroupBox)
        self.auteurPersoGroupBox.setGeometry(QtCore.QRect(10, 20, 291, 61))
        self.auteurPersoGroupBox.setObjectName("auteurPersoGroupBox")
        self.auteurPersoLabel = QtWidgets.QLabel(self.auteurPersoGroupBox)
        self.auteurPersoLabel.setGeometry(QtCore.QRect(10, 25, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(18)
        font.setItalic(True)
        self.auteurPersoLabel.setFont(font)
        self.auteurPersoLabel.setTextFormat(QtCore.Qt.RichText)
        self.auteurPersoLabel.setScaledContents(False)
        self.auteurPersoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.auteurPersoLabel.setObjectName("auteurPersoLabel")
        self.niveauPersoGroupBox = QtWidgets.QGroupBox(self.infoPersoGroupBox)
        self.niveauPersoGroupBox.setGeometry(QtCore.QRect(10, 80, 291, 61))
        self.niveauPersoGroupBox.setObjectName("niveauPersoGroupBox")
        self.niveauPersoLabel = QtWidgets.QLabel(self.niveauPersoGroupBox)
        self.niveauPersoLabel.setGeometry(QtCore.QRect(10, 25, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(17)
        font.setItalic(True)
        self.niveauPersoLabel.setFont(font)
        self.niveauPersoLabel.setTextFormat(QtCore.Qt.RichText)
        self.niveauPersoLabel.setScaledContents(True)
        self.niveauPersoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.niveauPersoLabel.setWordWrap(False)
        self.niveauPersoLabel.setObjectName("niveauPersoLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.genTab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 390, 661, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.genButtonLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.genButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.genButtonLayout.setObjectName("genButtonLayout")
        self.genPushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genPushButton.sizePolicy().hasHeightForWidth())
        self.genPushButton.setSizePolicy(sizePolicy)
        self.genPushButton.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.genPushButton.setFont(font)
        self.genPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.genPushButton.setObjectName("genPushButton")
        self.genButtonLayout.addWidget(self.genPushButton)
        self.tabWidget.addTab(self.genTab, "")
        self.configTab = QtWidgets.QWidget()
        self.configTab.setObjectName("configTab")
        self.infoPerso = QtWidgets.QGroupBox(self.configTab)
        self.infoPerso.setGeometry(QtCore.QRect(10, 10, 307, 161))
        self.infoPerso.setObjectName("infoPerso")
        self.auteurConfig = QtWidgets.QGroupBox(self.infoPerso)
        self.auteurConfig.setGeometry(QtCore.QRect(10, 20, 288, 61))
        self.auteurConfig.setObjectName("auteurConfig")
        self.auteurLineEdit = QtWidgets.QLineEdit(self.auteurConfig)
        self.auteurLineEdit.setGeometry(QtCore.QRect(10, 25, 269, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auteurLineEdit.sizePolicy().hasHeightForWidth())
        self.auteurLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        self.auteurLineEdit.setFont(font)
        self.auteurLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.auteurLineEdit.setClearButtonEnabled(True)
        self.auteurLineEdit.setObjectName("auteurLineEdit")
        self.niveauConfig = QtWidgets.QGroupBox(self.infoPerso)
        self.niveauConfig.setGeometry(QtCore.QRect(10, 90, 288, 61))
        self.niveauConfig.setObjectName("niveauConfig")
        self.niveauLineEdit = QtWidgets.QLineEdit(self.niveauConfig)
        self.niveauLineEdit.setGeometry(QtCore.QRect(10, 25, 269, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.niveauLineEdit.sizePolicy().hasHeightForWidth())
        self.niveauLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(12)
        self.niveauLineEdit.setFont(font)
        self.niveauLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.niveauLineEdit.setClearButtonEnabled(True)
        self.niveauLineEdit.setObjectName("niveauLineEdit")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.configTab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(330, 20, 341, 161))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.configSaveLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.configSaveLayout.setContentsMargins(30, 50, 30, 50)
        self.configSaveLayout.setSpacing(0)
        self.configSaveLayout.setObjectName("configSaveLayout")
        self.configSaveButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configSaveButton.sizePolicy().hasHeightForWidth())
        self.configSaveButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.configSaveButton.setFont(font)
        self.configSaveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.configSaveButton.setObjectName("configSaveButton")
        self.configSaveLayout.addWidget(self.configSaveButton)
        self.matieresConfig = QtWidgets.QGroupBox(self.configTab)
        self.matieresConfig.setGeometry(QtCore.QRect(10, 180, 661, 261))
        self.matieresConfig.setFlat(False)
        self.matieresConfig.setCheckable(True)
        self.matieresConfig.setChecked(True)
        self.matieresConfig.setObjectName("matieresConfig")
        self.matiereTableWidget = QtWidgets.QTableWidget(self.matieresConfig)
        self.matiereTableWidget.setEnabled(True)
        self.matiereTableWidget.setGeometry(QtCore.QRect(10, 30, 641, 191))
        self.matiereTableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.matiereTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.matiereTableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.matiereTableWidget.setAutoScroll(False)
        self.matiereTableWidget.setAutoScrollMargin(0)
        self.matiereTableWidget.setDragEnabled(True)
        self.matiereTableWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.matiereTableWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.matiereTableWidget.setAlternatingRowColors(True)
        self.matiereTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.matiereTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.matiereTableWidget.setShowGrid(False)
        self.matiereTableWidget.setWordWrap(False)
        self.matiereTableWidget.setCornerButtonEnabled(True)
        self.matiereTableWidget.setRowCount(15)
        self.matiereTableWidget.setObjectName("matiereTableWidget")
        self.matiereTableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.matiereTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.matiereTableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.matiereTableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.matiereTableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.matiereTableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.matiereTableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.matiereTableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.matiereTableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.matiereTableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.matiereTableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.matiereTableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.matiereTableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.matiereTableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.matiereTableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.matiereTableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.matiereTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.matiereTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.matiereTableWidget.setHorizontalHeaderItem(2, item)
        self.matiereTableWidget.horizontalHeader().setDefaultSectionSize(175)
        self.matiereTableWidget.horizontalHeader().setHighlightSections(True)
        self.matiereTableWidget.horizontalHeader().setStretchLastSection(True)
        self.matiereTableWidget.verticalHeader().setVisible(False)
        self.matiereTableWidget.verticalHeader().setHighlightSections(False)
        self.matiereTableWidget.verticalHeader().setSortIndicatorShown(False)
        self.matiereTableWidget.verticalHeader().setStretchLastSection(False)
        self.matiereTablePlus = QtWidgets.QPushButton(self.matieresConfig)
        self.matiereTablePlus.setEnabled(True)
        self.matiereTablePlus.setGeometry(QtCore.QRect(10, 230, 21, 21))
        self.matiereTablePlus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.matiereTablePlus.setObjectName("matiereTablePlus")
        self.matiereTableMinus = QtWidgets.QPushButton(self.matieresConfig)
        self.matiereTableMinus.setEnabled(True)
        self.matiereTableMinus.setGeometry(QtCore.QRect(33, 230, 21, 21))
        self.matiereTableMinus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.matiereTableMinus.setObjectName("matiereTableMinus")
        self.matiereTableReset = QtWidgets.QPushButton(self.matieresConfig)
        self.matiereTableReset.setEnabled(True)
        self.matiereTableReset.setGeometry(QtCore.QRect(63, 230, 75, 21))
        self.matiereTableReset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.matiereTableReset.setObjectName("matiereTableReset")
        self.matiereTableBrowse = QtWidgets.QPushButton(self.matieresConfig)
        self.matiereTableBrowse.setEnabled(True)
        self.matiereTableBrowse.setGeometry(QtCore.QRect(576, 230, 75, 21))
        self.matiereTableBrowse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.matiereTableBrowse.setObjectName("matiereTableBrowse")
        self.tabWidget.addTab(self.configTab, "")
        self.aboutTab = QtWidgets.QWidget()
        self.aboutTab.setObjectName("aboutTab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.aboutTab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 681, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.aboutLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.aboutLayout.setContentsMargins(0, 0, 0, 0)
        self.aboutLayout.setObjectName("aboutLayout")
        self.titleLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.titleLabel.setTextFormat(QtCore.Qt.AutoText)
        self.titleLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.aboutLayout.addWidget(self.titleLabel)
        self.versionLayout = QtWidgets.QHBoxLayout()
        self.versionLayout.setObjectName("versionLayout")
        self.versionLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.versionLabel.setTextFormat(QtCore.Qt.RichText)
        self.versionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.versionLabel.setObjectName("versionLabel")
        self.versionLayout.addWidget(self.versionLabel)
        self.varVersionLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.varVersionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.varVersionLabel.setObjectName("varVersionLabel")
        self.versionLayout.addWidget(self.varVersionLabel)
        self.aboutLayout.addLayout(self.versionLayout)
        self.gitHubLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.gitHubLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.gitHubLabel.setOpenExternalLinks(True)
        self.gitHubLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.gitHubLabel.setObjectName("gitHubLabel")
        self.aboutLayout.addWidget(self.gitHubLabel)
        self.tabWidget.addTab(self.aboutTab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.infoGroupBox.setTitle(_translate("MainWindow", "Informations"))
        self.titreGroupBox.setTitle(_translate("MainWindow", "Titre"))
        self.titreLineEdit.setPlaceholderText(_translate("MainWindow", "Les Lois de Newton"))
        self.soustitreGroupBox.setTitle(_translate("MainWindow", "Sous-Titre"))
        self.soustitreLineEdit.setPlaceholderText(_translate("MainWindow", "Newton, grand physicien"))
        self.matGroupBox.setTitle(_translate("MainWindow", "Matière"))
        self.matLineEdit.setPlaceholderText(_translate("MainWindow", "PHY"))
        self.numGroupBox.setTitle(_translate("MainWindow", "Numéro"))
        self.numLineEdit.setPlaceholderText(_translate("MainWindow", "0624"))
        self.sectionGroupBox.setTitle(_translate("MainWindow", "Première Section"))
        self.sectionNumLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; text-decoration: underline;\">1.</span></p></body></html>"))
        self.sectionLineEdit.setPlaceholderText(_translate("MainWindow", "La Loi de l\'Inertie"))
        self.pathPathLabel.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"none\"><span style=\" font-size:11pt; text-decoration: underline; color:#f0f0f0;\">Aucun chemin de sauvegarde</span></a></p></body></html>"))
        self.infoPersoGroupBox.setToolTip(_translate("MainWindow", "Pour modifier les informations, veuillez aller dans le Configurateur"))
        self.infoPersoGroupBox.setTitle(_translate("MainWindow", "Informations Personnelles"))
        self.auteurPersoGroupBox.setTitle(_translate("MainWindow", "Auteur"))
        self.auteurPersoLabel.setText(_translate("MainWindow", "Auteur"))
        self.niveauPersoGroupBox.setTitle(_translate("MainWindow", "Niveau"))
        self.niveauPersoLabel.setText(_translate("MainWindow", "Niveau"))
        self.genPushButton.setText(_translate("MainWindow", "Générer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.genTab), _translate("MainWindow", "Générateur"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.genTab), _translate("MainWindow", "Créer un document"))
        self.infoPerso.setTitle(_translate("MainWindow", "Informations Personnelles"))
        self.auteurConfig.setTitle(_translate("MainWindow", "Auteur"))
        self.auteurLineEdit.setPlaceholderText(_translate("MainWindow", "Laurent Bourgon"))
        self.niveauConfig.setTitle(_translate("MainWindow", "Niveau"))
        self.niveauLineEdit.setPlaceholderText(_translate("MainWindow", "Secondaire 5 - 2019-2020"))
        self.configSaveButton.setText(_translate("MainWindow", "Appliquer et Enregistrer"))
        self.matieresConfig.setTitle(_translate("MainWindow", "Matières Personnalisées"))
        item = self.matiereTableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.matiereTableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.matiereTableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.matiereTableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.matiereTableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.matiereTableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.matiereTableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.matiereTableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.matiereTableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.matiereTableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.matiereTableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.matiereTableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.matiereTableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.matiereTableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.matiereTableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.matiereTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Matière"))
        item = self.matiereTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nom Court"))
        item = self.matiereTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Chemin"))
        self.matiereTablePlus.setText(_translate("MainWindow", "+"))
        self.matiereTableMinus.setText(_translate("MainWindow", "-"))
        self.matiereTableReset.setText(_translate("MainWindow", "Réinitialiser"))
        self.matiereTableBrowse.setText(_translate("MainWindow", "Parcourir..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.configTab), _translate("MainWindow", "Configurateur"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.configTab), _translate("MainWindow", "Modifier les Informations"))
        self.titleLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">pyÉtude</span></p></body></html>"))
        self.versionLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Version: </span></p></body></html>"))
        self.varVersionLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic;\">[VERSION]</span></p></body></html>"))
        self.gitHubLabel.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://github.com/BourgonLaurent/pyEtude/blob/master/LICENSE\"><span style=\" text-decoration: underline; color:#f0f0f0;\">© Laurent Bourgon Sous la license MIT</span></a></p><p><span style=\" color:#f0f0f0;\"><br/></span></p><p><a href=\"https://github.com/BourgonLaurent/pyEtude\"><span style=\" text-decoration: underline; color:#f0f0f0;\">Projet GitHub</span></a></p><p><a href=\"https://github.com/BourgonLaurent/pyEtude#faq\"><span style=\" text-decoration: underline; color:#f0f0f0;\">Vous avez un problème?</span></a></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), _translate("MainWindow", "À Propos"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.aboutTab), _translate("MainWindow", "À Propos"))
