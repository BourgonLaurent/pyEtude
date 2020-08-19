## Document.py - damysos
# Document exporter
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
from damysos import __version__

# Default packages
from typing import Dict

# External packages
from docxtpl import DocxTemplate


class Document:
    """
    Create a word document with specific values

    Parameters
    ----------
    values : Dict[str, str]
        Dictionnary containing the values to replace {"placeholder": "replaced"}
    
    model : str
        Path to the document model
    
    filepath : str
        Path to the export destination
    
    Methods
    ----------
    packWord : () -> ()
        Export the Word Document
    """

    def __init__(self, values: Dict[str, str], model: str, filepath: str):
        self.values = values
        self.model = model
        self.filepath = filepath

        self.document = DocxTemplate(self.model)

    def packWord(self):
        """Export the Word Document with the values given earlier"""
        self.document.render(self.values)
        self.document.save(self.filepath)
