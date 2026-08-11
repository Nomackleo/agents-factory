import unittest
import os
import json

class TestMinimalCodingEcosystem(unittest.TestCase):

    def setUp(self):
        self.base_path = r"c:\Users\Nomack\Documents\workspace\agents\antigravity\dev\prompt-generator\agents-factory\minimal-coding-ecosystem"

    def test_ecosystem_structure(self):
        """Verifica que el ecosistema contenga todas las carpetas y configuraciones obligatorias."""
        self.assertTrue(os.path.exists(self.base_path))
        self.assertTrue(os.path.exists(os.path.join(self.base_path, "README.md")))
        self.assertTrue(os.path.exists(os.path.join(self.base_path, "brain", "routing-matrix.json")))
        self.assertTrue(os.path.exists(os.path.join(self.base_path, "brain", "models.yml")))

    def test_skills_crispe_compliance(self):
        """Verifica que los skills del Minimal Coding Guild cumplan con la sintaxis Neo-CRISPE."""
        skills_path = os.path.join(self.base_path, ".agents", "skills", "minimal-coding-guild")
        expected_skills = ["minimal-code-refactorer", "minimal-architect-checker", "minimal-qa-gatekeeper"]
        
        for skill in expected_skills:
            skill_file = os.path.join(skills_path, skill, "SKILL.md")
            self.assertTrue(os.path.exists(skill_file), f"Falta SKILL.md para {skill}")
            with open(skill_file, "r", encoding="utf-8") as f:
                content = f.read()
                self.assertIn("---", content)
                self.assertIn("name:", content)
                self.assertIn("description:", content)
                self.assertIn("<role>", content)
                self.assertIn("<task>", content)

    def test_routing_matrix_valid_json(self):
        """Verifica que la matriz de enrutamiento sea un JSON válido."""
        matrix_path = os.path.join(self.base_path, "brain", "routing-matrix.json")
        with open(matrix_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertEqual(data.get("ecosystem"), "minimal-coding-ecosystem")
            self.assertTrue(len(data.get("routing_rules", [])) >= 3)

if __name__ == "__main__":
    unittest.main()
