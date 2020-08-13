## model_config.py - Damysos.models
# Config classes for the config
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
from .model import Model

# Default packages
from dataclasses import dataclass
from typing import Dict, List, Optional, cast


@dataclass
class ModelConfig:
    default: Optional[Model]
    models: List[Model]

    @property
    def __dictionary__(self) -> Dict[str, str]:
        new_dict = self.__dict__.copy()
        new_dict["models"] = [
            model.__dictionary__ for model in cast(List[Model], new_dict["models"])
        ]

        return new_dict


## Example:
# model_config = ModelConfig(
#     default=None,
#     models=[
#         Model(
#             name="Documents de Révision",
#             filepath=os.path.join(os.getcwd(), "Documents de Révision.docx"),
#             exportpath="Documents de Révision",
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
