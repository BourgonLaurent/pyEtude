## settings.py - Damysos.config
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
from .matieres import Matiere
from .models import ModelConfig

# Default packages
from dataclasses import dataclass, field
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
    rebuild_from_dict: (rebuild_dict: Dict[str, Any]) -> Settings
        Populate the parameters from a dictionary (to be used with dataclasses.asdict)
    """

    auteur: str = ""
    niveau: str = ""
    matieres: Dict[str, Matiere] = field(default=Dict[str, Matiere])  # type: ignore
    modeles: ModelConfig = ModelConfig()

    def rebuild_from_dict(self, rebuild_dict: Dict[str, Any]):
        """
        Populate the parameters from a dictionary (to be used with dataclasses.asdict)

        Parameters
        ----------
        rebuild_dict : Dict[str, Any]
            Dictionary that will be used to populate the dataclass

        Returns
        -------
        Settings
            Returns itself
        """

        for key, value in rebuild_dict.items():
            if key == "matieres":
                value = {
                    name: Matiere().rebuild_from_dict(matiere)
                    for name, matiere in value.items()
                }
            elif key == "modeles":
                value = ModelConfig().rebuild_from_dict(value)

            self.__setattr__(key, value)

        return self
