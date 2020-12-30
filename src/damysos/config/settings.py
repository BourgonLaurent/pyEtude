## settings.py - damysos.config
# Settings classes
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
# Project packages
from damysos import CONFIG_FILE
from .matieres import Matiere
from .models import Model, ModelConfig, ModelValues

# Default packages
import json
import os
from dataclasses import asdict, dataclass, field
from typing import Any, Dict

# External packages
from damysos.ui.widgets.advanced_tab_widget import AdvancedTabWidget

DEFAULT_MATIERES: Dict[str, Matiere] = {
    "Anglais": Matiere("ANG", ""),
    "Arts": Matiere("ART", ""),
    "Chimie": Matiere("CHM", ""),
    "Éducation Financière": Matiere("EFI", ""),
    "Éducation Physique": Matiere("EDP", ""),
    "Éthique et Culture Religieuse": Matiere("ECR", ""),
    "Français": Matiere("FRA", ""),
    "Mathématiques": Matiere("MAT", ""),
    "Monde Contemporain": Matiere("MDC", ""),
    "Physique": Matiere("PHY", ""),
}

_doc_de_rev = Model(
    "Documents de Révision",
    filepath=os.path.join(os.getcwd(), "Documents de Révision.docx"),
    export_name="",
    values=ModelValues(
        auteur="Auteur",
        niveau="Niveau",
        titre="Titre",
        soustitre="Sous-Titre",
        matiere="Matière",
        numero="Numéro",
        section="Section",
    ),
)

DEFAULT_MODELS = ModelConfig(models=[_doc_de_rev], default=_doc_de_rev.name)


@dataclass
class Settings:
    """
    Configuration Object that holds all settings

    Parameters
    ----------
    auteur : str
        Name of the user

    niveau : str
        Level of the user

    matieres: Dict[str, Matiere]
        Dictionary containing the matière, the key is its name
    
    modeles: ModelConfig
        Models that are available to the user
    
    Methods
    ----------
    load_config_file () -> Settings
        Populate the parameters from damysos.CONFIG_FILE    
    
    rebuild_from_dict: (rebuild_dict: Dict[str, Any]) -> Settings
        Create a new object from the dictionary (to be used with dataclasses.asdict)
    """

    auteur: str = ""
    niveau: str = ""
    custom_matieres: bool = False
    matieres: Dict[str, Matiere] = field(default_factory=lambda: {})
    modeles: ModelConfig = ModelConfig()

    def __bool__(self):
        return bool([v for v in self.__dict__.values() if v])

    def dump_config_file(self):
        with open(CONFIG_FILE, mode="w", encoding="utf-8") as config_file:
            json.dump(
                asdict(self), config_file, sort_keys=True, indent=4, ensure_ascii=False
            )

    def reset_matieres(self):
        self.matieres = DEFAULT_MATIERES

    @staticmethod
    def load_config_file(tab_widget: AdvancedTabWidget = None):
        try:
            with open(CONFIG_FILE, mode="r", encoding="utf-8") as config_file:
                config: Dict[str, Any] = json.load(config_file)

            if tab_widget:
                tab_widget.setConfigurationMode(in_configuration_mode=False)
            return Settings.rebuild_from_dict(config)

        except FileNotFoundError:
            if tab_widget:
                tab_widget.setConfigurationMode(in_configuration_mode=True)
            return Settings(matieres=DEFAULT_MATIERES, modeles=DEFAULT_MODELS)

    @staticmethod
    def rebuild_from_dict(rebuild_dict: Dict[str, Any]):
        """
        Create a new object from the dictionary (to be used with dataclasses.asdict)

        Parameters
        ----------
        rebuild_dict : Dict[str, Any]
            Dictionary that will be used to populate the dataclass

        Returns
        -------
        Settings
            Returns the object created
        """
        settings = Settings()

        for key, value in rebuild_dict.items():
            try:
                if key == "matieres":
                    value = {
                        name: Matiere.rebuild_from_dict(matiere)
                        for name, matiere in value.items()
                    }
                elif key == "modeles":
                    value = ModelConfig.rebuild_from_dict(value)

                settings.__setattr__(key, value)
            except:
                assert KeyError

        return settings
