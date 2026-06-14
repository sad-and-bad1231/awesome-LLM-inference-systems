import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MONITOR = ROOT / "scripts" / "ai_infra_monitor" / "monitor.py"


class CliTests(unittest.TestCase):
    def test_help_lists_core_commands(self):
        result = subprocess.run(
            [sys.executable, str(MONITOR), "--help"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        for command in ("discover", "validate", "finalize", "status"):
            self.assertIn(command, result.stdout)


if __name__ == "__main__":
    unittest.main()
