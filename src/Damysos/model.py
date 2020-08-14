## model.py - Damysos.models
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
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ModelValues:
    """
    Values for the models

    Parameters
    ----------
    The parameter correspond to the Jinja tags
    """

    auteur: str
    niveau: str
    titre: str
    soustitre: str
    matiere: str
    numero: str
    section: str


@dataclass
class Model:
    """
    Model Object that represents a Word document containing Jinja2 tags

    Parameters
    ----------
    name: str
        Name of the model
    
    filepath: str
        Filepath of the Word document
    
    export_name: str
        Name of the folder that will contain the exported documents

    values: ModelValues
        ModelValues object containing the Jinja tags that will be replaced
    """

    name: str
    filepath: str
    export_name: str
    values: ModelValues


@dataclass
class ModelConfig:
    """
    Configuration Object that holds all available models

    Parameters
    ----------
    models: List[Model]
        List containing Model objects that can be selected
    
    default: Model | None
        (Optional) The default model that is set, (must also be part of the models)
    """

    models: List[Model]
    default: Optional[Model] = None


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
