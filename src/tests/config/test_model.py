## test_model.py - tests.config
# Testing Model Classes
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
from damysos.config.models import ModelValues, Model, ModelConfig

# Default packages
import json
from unittest import TestCase
from dataclasses import asdict


class TestModelValues(TestCase):
    auteur = "Auteur"
    matiere = "Matière"
    values = ModelValues(
        auteur=auteur,
        niveau="Niveau",
        titre="Titre",
        soustitre="Sous-Titre",
        matiere=matiere,
        numero="Numéro",
        section="Section",
    )

    def test_values(self):
        """Test if values are saved correctly"""
        # Normal characters
        self.assertEqual(self.values.auteur, self.auteur)
        # Accentuated characters
        self.assertEqual(self.values.matiere, self.matiere)

    def test_dict(self):
        """Test if conversions to dict were successfully done"""
        # Normal characters
        self.assertEqual(asdict(self.values)["auteur"], self.auteur)
        # Accentuated characters
        self.assertEqual(asdict(self.values)["matiere"], self.matiere)

    def test_json_conversion(self):
        """Test if JSON conversions work correctly"""
        # Full conversion
        self.assertEqual(
            json.loads(json.dumps(asdict(self.values)))["auteur"], self.auteur
        )
        # Accentuated characters
        self.assertEqual(
            json.loads(json.dumps(asdict(self.values)))["matiere"], self.matiere
        )

    def test_rebuilding(self):
        """Test if the rebuild process works correctly"""
        # Full conversion
        self.assertEqual(
            ModelValues.rebuild_from_dict(json.loads(json.dumps(asdict(self.values)))),
            self.values,
        )


class TestModel(TestCase):
    name = "test"
    exp_name = "ÀÉÇ"

    values = ModelValues(
        auteur="Auteur",
        niveau="Niveau",
        titre="Titre",
        soustitre="Sous-Titre",
        matiere="Matière",
        numero="Numéro",
        section="Section",
    )
    model = Model(name=name, filepath="test.docx", export_name=exp_name, values=values)

    def test_values(self):
        """Test if values are saved correctly"""
        # Normal characters
        self.assertEqual(self.model.name, self.name)
        # Accentuated characters
        self.assertEqual(self.model.export_name, self.exp_name)

    def test_dict(self):
        """Test if conversions to dict were successfully done"""
        # Check if both are equals
        self.assertEqual(asdict(self.model)["name"], self.name)
        # Check if values are the same
        self.assertEqual(asdict(self.model)["values"], asdict(self.values))

    def test_modelvalues(self):
        """Test if ModelValues changes"""
        # Check if both are equals
        self.assertEqual(self.model.values, self.values)

    def test_json_conversion(self):
        """Test if JSON conversions work correctly"""
        # Full conversion
        self.assertEqual(json.loads(json.dumps(asdict(self.model)))["name"], self.name)
        # Children conversion: ModelValues
        self.assertEqual(
            json.loads(json.dumps(asdict(self.model)))["values"], asdict(self.values)
        )

    def test_rebuilding(self):
        """Test if the rebuild process works correctly"""
        # Full conversion
        self.assertEqual(
            Model.rebuild_from_dict(json.loads(json.dumps(asdict(self.model)))),
            self.model,
        )
        # Children conversion: ModelValues
        self.assertEqual(
            Model()
            .rebuild_from_dict(json.loads(json.dumps(asdict(self.model))))
            .values,
            self.values,
        )


class TestModelConfig(TestCase):
    name = "test"
    exp_name = "Tests"

    values = ModelValues(
        auteur="Auteur",
        niveau="Niveau",
        titre="Titre",
        soustitre="Sous-Titre",
        matiere="Matière",
        numero="Numéro",
        section="Section",
    )

    model = Model(name=name, filepath="test.docx", export_name=exp_name, values=values)
    model2 = Model(name="ÀÉÇ", filepath="ÀÉÇ.docx", export_name="ÀÉÇ", values=values)

    model_config = ModelConfig(models=[model, model2])

    def test_values(self):
        """Test if values are saved correctly"""
        # Normal characters
        self.assertEqual(self.model_config.models, [self.model, self.model2])
        # None values
        self.assertEqual(self.model_config.default, None)

    def test_none_values(self):
        """Test if values are saved correctly"""
        # Setting values
        self.model_config.default = self.model
        self.assertEqual(self.model_config.default, self.model)
        # Resetting to None
        self.model_config.default = None
        self.assertEqual(self.model_config.default, None)

    def test_dict(self):
        """Test if conversions to dict were successfully done"""
        # Check if both are equals
        self.assertEqual(asdict(self.model_config)["default"], None)
        # Check if values are the same
        self.assertEqual(asdict(self.model_config)["models"][0], asdict(self.model))

    def test_json_conversion(self):
        """Test if JSON conversions work correctly"""
        # Full conversion
        self.assertEqual(
            json.loads(json.dumps(asdict(self.model_config)))["default"], None
        )
        # Children conversion: Model
        self.assertEqual(
            json.loads(json.dumps(asdict(self.model_config)))["models"][0],
            asdict(self.model),
        )
        # Children conversion: ModelValues
        self.assertEqual(
            json.loads(json.dumps(asdict(self.model_config)))["models"][0]["values"],
            asdict(self.model.values),
        )

    def test_rebuilding(self):
        """Test if the rebuild process works correctly"""
        # Full conversion
        self.assertEqual(
            ModelConfig.rebuild_from_dict(
                json.loads(json.dumps(asdict(self.model_config)))
            ),
            self.model_config,
        )
        # Children conversion: Model
        self.assertEqual(
            ModelConfig.rebuild_from_dict(
                json.loads(json.dumps(asdict(self.model_config)))
            ).models[0],
            self.model,
        )
        # Children conversion: ModelValues
        self.assertEqual(
            ModelConfig.rebuild_from_dict(
                json.loads(json.dumps(asdict(self.model_config)))
            )
            .models[0]
            .values,
            self.values,
        )
