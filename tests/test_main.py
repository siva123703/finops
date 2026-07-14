import unittest
from unittest.mock import patch

import main


class MainEntryPointTests(unittest.TestCase):
    def test_root_main_reexports_finops_agent(self):
        with patch("src.main.finops_agent") as mocked_finops_agent:
            mocked_finops_agent.return_value = "ok"
            self.assertEqual(main.finops_agent(None), "ok")
            mocked_finops_agent.assert_called_once_with(None)


if __name__ == "__main__":
    unittest.main()
