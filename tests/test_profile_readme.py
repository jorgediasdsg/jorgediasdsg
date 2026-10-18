import re
import unittest
from pathlib import Path


README = (Path(__file__).parents[1] / "README.md").read_text(encoding="utf-8")


class ProfileReadmeContractTests(unittest.TestCase):
    def test_evolution_stages_are_ordered_and_complete(self):
        stages = [
            "Redes e sistemas",
            "Desenvolvimento",
            "Arquitetura",
            "Automação",
            "DevOps",
            "Operação",
        ]
        positions = [README.index(f"| {stage} |") for stage in stages]

        self.assertEqual(positions, sorted(positions))
        self.assertIn("## Linha de evolução técnica", README)

    def test_each_stage_relates_to_technologies_or_practices(self):
        expected_terms = {
            "Redes e sistemas": ("Linux", "redes"),
            "Desenvolvimento": ("Go", "APIs", "testes"),
            "Arquitetura": ("serviços", "separação de responsabilidades"),
            "Automação": ("scripts", "Ansible", "Terraform"),
            "DevOps": ("Docker", "Kubernetes", "CI/CD"),
            "Operação": ("logs", "recuperação", "observabilidade"),
        }

        for stage, terms in expected_terms.items():
            row = next(line for line in README.splitlines() if f"| {stage} |" in line)
            self.assertTrue(
                any(term.lower() in row.lower() for term in terms),
                msg=f"{stage} não relaciona tecnologia ou prática verificável",
            )

    def test_readme_does_not_expose_identifiable_project_names(self):
        forbidden_identifiers = (
            "poc-gke-lab",
            "fedora-bootstrap-ansible",
            "pdf-expert",
            "ultimate-ttt",
            "guesses",
            "linkedin.com",
        )

        for identifier in forbidden_identifiers:
            self.assertNotIn(identifier.lower(), README.lower())

    def test_readme_does_not_invent_metrics_or_job_titles(self):
        self.assertIsNone(re.search(r"\b\d+\s*%", README))
        self.assertNotRegex(
            README.lower(),
            r"\b(ceo|cto|diretor|gerente|head|tech lead)\b",
        )


if __name__ == "__main__":
    unittest.main()
