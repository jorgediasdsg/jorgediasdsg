import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


class ReadmePositioningTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = README.read_text(encoding="utf-8")
        cls.first_screen = "\n".join(cls.content.splitlines()[:18])

    def test_first_screen_has_searchable_positioning_and_required_stack(self):
        self.assertTrue(
            self.content.startswith(
                '<h1 align="center">Engenheiro de Software | Backend, Automação e DevOps</h1>'
            )
        )
        self.assertIn("integração com frontend", self.first_screen.casefold())

        for technology in (
            "Go",
            "Python",
            "Node.js",
            "React",
            "Docker",
            "Kubernetes",
            "Terraform",
            "Ansible",
            "CI/CD",
            "GitOps",
        ):
            with self.subTest(technology=technology):
                self.assertIn(technology, self.first_screen)

    def test_first_screen_starts_with_one_clear_heading(self):
        first_non_empty = next(line for line in self.content.splitlines() if line.strip())
        self.assertTrue(first_non_empty.startswith("<h1"))
        self.assertLess(self.content.find("</h1>"), self.content.find("\n---"))

    def test_profile_contains_no_identifiable_project_names_or_links(self):
        forbidden_project_names = (
            "poc-gke-lab",
            "fedora-bootstrap-ansible",
            "pdf-expert",
            "ultimate-ttt",
            "guesses",
        )
        for project_name in forbidden_project_names:
            with self.subTest(project_name=project_name):
                self.assertNotIn(project_name, self.content)

        self.assertNotIn("Projetos em destaque", self.content)
        self.assertNotRegex(self.content, r"github\.com/jorgediasdsg/[^\s)\"]+")


if __name__ == "__main__":
    unittest.main()
