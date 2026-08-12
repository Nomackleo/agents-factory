import unittest
import os
import json

class TestSpecKitIntegration(unittest.TestCase):

    def setUp(self):
        self.base_path = r"c:\Users\Nomack\Documents\workspace\agents\antigravity\dev\prompt-generator\agents-factory\minimal-coding-ecosystem"

    def test_spec_driven_developer_skill_exists(self):
        """Verifica que el skill spec-driven-developer exista y cumpla Neo-CRISPE."""
        skill_file = os.path.join(self.base_path, ".agents", "skills", "minimal-coding-guild", "spec-driven-developer", "SKILL.md")
        self.assertTrue(os.path.exists(skill_file), "Falta SKILL.md para spec-driven-developer")
        with open(skill_file, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("---", content)
            self.assertIn("name: spec-driven-developer", content)
            self.assertIn("<role>", content)
            self.assertIn("<task>", content)
            self.assertIn("<sdd_lifecycle>", content)

    def test_routing_matrix_includes_sdd(self):
        """Verifica que la matriz de enrutamiento incluya la regla spec_driven_development."""
        matrix_path = os.path.join(self.base_path, "brain", "routing-matrix.json")
        with open(matrix_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            rules = data.get("routing_rules", [])
            assigned_agents = [r.get("assigned_agent") for r in rules]
            self.assertIn("spec-driven-developer", assigned_agents)

    def test_models_yml_includes_sdd_agent(self):
        """Verifica que models.yml defina el modelo para spec-driven-developer."""
        models_path = os.path.join(self.base_path, "brain", "models.yml")
        with open(models_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("spec-driven-developer:", content)
            self.assertIn("gemini-3.6-flash", content)

if __name__ == "__main__":
    unittest.main()
