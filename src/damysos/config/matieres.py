## matieres.py - damysos.config
# Matières Classes
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
from typing import Dict


@dataclass
class Matiere:
    """
    Matière Object that represents a Word document containing Jinja2 tags

    Parameters
    ----------
    alias: str
        (Optional) Short name of the matière
    
    path: str
        (Optional) Path of where the files for this matière are saved
    
    Static Methods
    ----------
    rebuild_from_dict: (rebuild_dict: Dict[str, str]) -> Matiere
        Create a new object from the dictionary (to be used with dataclasses.asdict)
    """

    alias: str = ""
    path: str = ""

    def __bool__(self):
        return bool([v for v in self.__dict__.values() if v])

    @staticmethod
    def rebuild_from_dict(rebuild_dict: Dict[str, str]):
        """
        Create a new object from the dictionary (to be used with dataclasses.asdict)

        Parameters
        ----------
        rebuild_dict : Dict[str, str]
            Dictionary that will be used to populate the dataclass

        Returns
        -------
        Matiere
            Returns the object created
        """
        matiere = Matiere()

        for key, value in rebuild_dict.items():
            matiere.__setattr__(key, value)

        return matiere