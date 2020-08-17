## advanced_tab_widget.py - damysos.ui.widgets
# Modified QTabWidget with additional functionalities
#
# MIT (c) 2020 Laurent Bourgon
#    Permission is hereby granted, free of charge, to any person obtaining a copy
#    of this software and associated documentation files (the "Software"), to deal
#    in the Software without restriction, including without limitation the rights
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#    copies of the Software, and to permit persons to whom the Software is
#    furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be included in all
#    copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#    SOFTWARE.

## Imports
# External packages
from PySide2.QtWidgets import QWidget, QTabWidget


class AdvancedTabWidget(QTabWidget):
    def __init__(self, parent: QWidget) -> None:
        """
        Creates the QTabWidget and sets its text

        Parameters
        ----------
        parent : QWidget
            Any Widget that will be parent of the QLineEdit
        """

        super().__init__(parent=parent)

        self.tabGenIndex = 0
        self.tabGenTooltip = "Créer un document"
        self.tabConfigIndex = 1
        self.tabModelIndex = 2
        self.tabModelTooltip = "Créer et gérer les modèles"
        self.tabAboutIndex = 3

        self.tabDisabledTooltip = "Veuillez utiliser le Configurateur"

    def setConfigurationMode(self, in_configuration_mode: bool):
        """
        Set the mode of the TabWidget

        Parameters
        ----------
        in_configuration_mode : bool
            True if the user is in configuration
        """
        # Générateur
        self.setTabEnabled(self.tabGenIndex, not in_configuration_mode)
        self.setTabToolTip(
            self.tabGenIndex,
            self.tabDisabledTooltip if in_configuration_mode else self.tabGenTooltip,
        )
        # Modèles
        self.setTabEnabled(self.tabModelIndex, not in_configuration_mode)
        self.setTabToolTip(
            self.tabModelIndex,
            self.tabDisabledTooltip if in_configuration_mode else self.tabModelTooltip,
        )
        # Set position
        self.setCurrentIndex(
            self.tabConfigIndex if in_configuration_mode else self.tabGenIndex
        )
