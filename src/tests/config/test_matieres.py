## test_matieres.py - tests.config
# Testing Matieres Classes
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
# Tested packages
from Damysos.config.matieres import Matiere

# Default packages
import json
from unittest import TestCase
from dataclasses import asdict


class TestModelConfig(TestCase):
    alias = "TEST"
    path = "Tests here AÉÇ"

    matiere = Matiere(alias=alias, path=path)

    def test_values(self):
        """Test if values are saved correctly"""
        # Normal characters
        self.assertEqual(self.matiere.alias, self.alias)
        # Accentuated characters
        self.assertEqual(self.matiere.path, self.path)

    def test_dict(self):
        """Test if conversions to dict were successfully done"""
        # Normal characters
        self.assertEqual(asdict(self.matiere)["alias"], self.alias)
        # Accentuated characters
        self.assertEqual(asdict(self.matiere)["path"], self.path)

    def test_json_conversion(self):
        """Test if JSON conversions work correctly"""
        # Full conversion
        self.assertEqual(
            json.loads(json.dumps(asdict(self.matiere)))["alias"], self.alias
        )

    def test_rebuilding(self):
        """Test if the rebuild process works correctly"""
        # Full conversion
        self.assertEqual(
            Matiere().rebuild_from_dict(json.loads(json.dumps(asdict(self.matiere)))),
            self.matiere,
        )
