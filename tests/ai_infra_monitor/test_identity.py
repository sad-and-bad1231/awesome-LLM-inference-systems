import unittest

from scripts.ai_infra_monitor.ai_infra_monitor.identity import (
    candidate_identity,
    normalize_title,
)
from scripts.ai_infra_monitor.ai_infra_monitor.models import Candidate


class IdentityTests(unittest.TestCase):
    def test_normalize_title_removes_formatting_noise(self):
        self.assertEqual(
            normalize_title("The KV-Cache: An Efficient System!"),
            "kv cache efficient system",
        )

    def test_arxiv_identity_ignores_version_and_pdf_form(self):
        first = Candidate(title="A", url="https://arxiv.org/abs/2606.12345v2")
        second = Candidate(title="A revised", url="https://arxiv.org/pdf/2606.12345")
        self.assertEqual(candidate_identity(first), candidate_identity(second))
        self.assertEqual(candidate_identity(first), "arxiv:2606.12345")

    def test_doi_has_priority_over_title(self):
        item = Candidate(
            title="Unrelated title",
            url="https://doi.org/10.1145/1234.5678",
        )
        self.assertEqual(candidate_identity(item), "doi:10.1145/1234.5678")

    def test_program_anchors_are_distinct_identities(self):
        first = Candidate(title="First", url="https://example.org/program/#event-one")
        second = Candidate(title="Second", url="https://example.org/program/#event-two")
        self.assertNotEqual(candidate_identity(first), candidate_identity(second))


if __name__ == "__main__":
    unittest.main()
