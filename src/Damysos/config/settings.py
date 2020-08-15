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
from .. import CONFIG_FILE
from .matieres import Matiere
from .models import ModelConfig

# Default packages
import json
from dataclasses import asdict, dataclass, field
from typing import Any, Dict


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
    matieres: Dict[str, Matiere] = field(default_factory=lambda: {})
    modeles: ModelConfig = ModelConfig()

    def __bool__(self):
        return bool([v for v in self.__dict__.values() if v])

    def dump_config_file(self):
        with open(CONFIG_FILE, mode="w", encoding="utf-8") as config_file:
            json.dump(
                asdict(self), config_file, sort_keys=True, indent=4, ensure_ascii=False
            )

    @staticmethod
    def load_config_file():
        try:
            with open(CONFIG_FILE, mode="r", encoding="utf-8") as config_file:
                config: Dict[str, Any] = json.load(config_file)

            return Settings.rebuild_from_dict(config)
        except FileNotFoundError:
            return Settings()

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
            if key == "matieres":
                value = {
                    name: Matiere.rebuild_from_dict(matiere)
                    for name, matiere in value.items()
                }
            elif key == "modeles":
                value = ModelConfig.rebuild_from_dict(value)

            settings.__setattr__(key, value)

        return settings
