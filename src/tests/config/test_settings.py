## test_settings.py - tests.config
# Testing Settings Classes
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
from typing import Set
from damysos.config.matieres import Matiere
from damysos.config.models import ModelConfig, Model, ModelValues
from damysos.config.settings import Settings

# Default packages
import json
from unittest import TestCase
from dataclasses import asdict


class TestSettings(TestCase):
    auteur = "User"
    niveau = "Grade ÀÉÇ"
    matieres = {"Test": Matiere(alias="TEST", path="Tests ÀÉÇ")}

    model_name = "Test"
    model_exp_name = "Tests"
    model_values = ModelValues(
        auteur="Auteur",
        niveau="Niveau",
        titre="Titre",
        soustitre="Sous-Titre",
        matiere="Matière",
        numero="Numéro",
        section="Section",
    )

    model = Model(
        name=model_name,
        filepath="test.docx",
        export_name=model_exp_name,
        values=model_values,
    )
    modeles = ModelConfig(models=[model])

    settings = Settings(
        auteur=auteur, niveau=niveau, matieres=matieres, modeles=modeles
    )

    def test_values(self):
        """Test if values are saved correctly"""
        # Normal characters
        self.assertEqual(self.settings.auteur, self.auteur)
        # Accentuated characters
        self.assertEqual(self.settings.niveau, self.niveau)

    def test_dict(self):
        """Test if conversions to dict were successfully done"""
        # Normal characters
        self.assertEqual(asdict(self.settings)["auteur"], self.auteur)
        # Accentuated characters
        self.assertEqual(asdict(self.settings)["niveau"], self.niveau)

    def test_json_conversion(self):
        """Test if JSON conversions work correctly"""
        # Full conversion
        self.assertEqual(
            json.loads(json.dumps(asdict(self.settings)))["auteur"], self.auteur
        )
        # Children conversion: Matiere
        self.assertEqual(
            json.loads(json.dumps(asdict(self.settings)))["matieres"],
            {k: asdict(v) for k, v in self.matieres.items()},
        )
        # Children conversion: ModelConfig
        self.assertEqual(
            json.loads(json.dumps(asdict(self.settings)))["modeles"],
            asdict(self.modeles),
        )
        # Children conversion: Model
        self.assertEqual(
            json.loads(json.dumps(asdict(self.settings)))["modeles"]["models"][0],
            asdict(self.model),
        )
        # Children conversion: ModelValues
        self.assertEqual(
            json.loads(json.dumps(asdict(self.settings)))["modeles"]["models"][0][
                "values"
            ],
            asdict(self.model_values),
        )

    def test_rebuilding(self):
        """Test if the rebuild process works correctly"""
        # Full conversion
        self.assertEqual(
            Settings.rebuild_from_dict(json.loads(json.dumps(asdict(self.settings)))),
            self.settings,
        )
        # Children conversion: Matiere
        self.assertEqual(
            Settings.rebuild_from_dict(
                json.loads(json.dumps(asdict(self.settings)))
            ).matieres,
            self.matieres,
        )
        # Children conversion: ModelConfig
        self.assertEqual(
            Settings.rebuild_from_dict(
                json.loads(json.dumps(asdict(self.settings)))
            ).modeles,
            self.modeles,
        )
        # Children conversion: Model
        self.assertEqual(
            Settings()
            .rebuild_from_dict(json.loads(json.dumps(asdict(self.settings))))
            .modeles.models[0],
            self.model,
        )
        # Children conversion: ModelValues
        self.assertEqual(
            Settings()
            .rebuild_from_dict(json.loads(json.dumps(asdict(self.settings))))
            .modeles.models[0]
            .values,
            self.model_values,
        )
