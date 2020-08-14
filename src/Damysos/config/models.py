## model.py - damysos.config
# Model Classes
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
# Default packages
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ModelValues:
    """
    Values for the models

    Parameters
    ----------
    The parameter correspond to the Jinja tags

    Methods
    ----------
    rebuild_from_dict: (rebuild_dict: Dict[str, str]) -> ModelValues
        Populate the parameters from a dictionary (to be used with dataclasses.asdict)
    """

    auteur: str = ""
    niveau: str = ""
    titre: str = ""
    soustitre: str = ""
    matiere: str = ""
    numero: str = ""
    section: str = ""

    def rebuild_from_dict(self, rebuild_dict: Dict[str, str]):
        """
        Populate the parameters from a dictionary (to be used with dataclasses.asdict)

        Parameters
        ----------
        rebuild_dict : Dict[str, str]
            Dictionary that will be used to populate the dataclass

        Returns
        -------
        ModelValues
            Returns itself
        """
        for key, value in rebuild_dict.items():
            self.__setattr__(key, value)

        return self


@dataclass
class Model:
    """
    Model Object that represents a Word document containing Jinja2 tags

    Parameters
    ----------
    name: str
        (Optional) Name of the model
    
    filepath: str
        (Optional) Filepath of the Word document
    
    export_name: str
        (Optional) Name of the folder that will contain the exported documents

    values: ModelValues
        (Optional) ModelValues object containing the Jinja tags that will be replaced

    Methods
    ----------
    rebuild_from_dict: (rebuild_dict: Dict[str, Any]) -> Model
        Populate the parameters from a dictionary (to be used with dataclasses.asdict)
    """

    name: str = ""
    filepath: str = ""
    export_name: str = ""
    values: ModelValues = ModelValues()

    def rebuild_from_dict(self, rebuild_dict: Dict[str, Any]):
        """
        Populate the parameters from a dictionary (to be used with dataclasses.asdict)

        Parameters
        ----------
        rebuild_dict : Dict[str, Any]
            Dictionary that will be used to populate the dataclass

        Returns
        -------
        Model
            Returns itself
        """
        for key, value in rebuild_dict.items():
            if key == "values":
                value = ModelValues().rebuild_from_dict(value)

            self.__setattr__(key, value)

        return self


@dataclass
class ModelConfig:
    """
    Configuration Object that holds all available models

    Parameters
    ----------
    models: List[Model] | None
        (Optional) List containing Model objects that can be selected
    
    default: Model | None
        (Optional) The default model that is set, (must also be part of the models)

    Methods
    ----------
    rebuild_from_dict: (rebuild_dict: Dict[str, Any]) -> ModelConfig
        Populate the parameters from a dictionary (to be used with dataclasses.asdict)
    """

    models: List[Model] = field(default=List[Model])  # type: ignore
    default: Optional[Model] = None

    def rebuild_from_dict(self, rebuild_dict: Dict[str, Any]):
        """
        Populate the parameters from a dictionary (to be used with dataclasses.asdict)

        Parameters
        ----------
        rebuild_dict : Dict[str, Any]
            Dictionary that will be used to populate the dataclass

        Returns
        -------
        ModelConfig
            Returns itself
        """

        for key, value in rebuild_dict.items():
            if key == "models":
                value = [Model().rebuild_from_dict(m) for m in value]

            self.__setattr__(key, value)

        return self


## Example:
# model_config = ModelConfig(
#     models=[
#         Model(
#             name="Documents de Révision",
#             filepath="Documents de Révision.docx",
#             export_name="Documents de Révision",
#             values=ModelValues(
#                 auteur="Auteur",
#                 niveau="Niveau",
#                 titre="Titre",
#                 soustitre="Sous-Titre",
#                 matiere="Matière",
#                 numero="Numéro",
#                 section="Section",
#             ),
#         )
#     ],
# )
# model_config_dict = {
#     "models": {
#         "name": "Documents de Révision",
#         "filepath": "Documents de Révision.docx",
#         "export_name": "Documents de Révision",
#         "values": {
#             "auteur": "Auteur",
#             "niveau": "Niveau",
#             "titre": "Titre",
#             "soustitre": "Sous-Titre",
#             "matiere": "Matière",
#             "numero": "Numéro",
#             "section": "Section",
#         },
#     },
#     "default": None,
# }
