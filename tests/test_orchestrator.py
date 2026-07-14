import unittest
from unittest.mock import patch

from src.orchestrator.orchestrator import FinOpsOrchestrator


class FinOpsOrchestratorTests(unittest.TestCase):
    def test_run_includes_ai_recommendations(self):
        report = {
            "summary": {"total_vms": 1, "running_vms": 1, "stopped_vms": 0},
            "observations": ["All VM instances are currently running."],
            "instances": [{"name": "vm-1", "status": "RUNNING"}],
        }

        with patch("src.orchestrator.orchestrator.VMCollector") as collector_cls, patch(
            "src.orchestrator.orchestrator.VMAnalyzer"
        ) as analyzer_cls, patch("src.orchestrator.orchestrator.VMReport") as report_cls, patch(
            "src.orchestrator.orchestrator.PromptBuilder"
        ) as prompt_builder_cls, patch("src.orchestrator.orchestrator.GeminiService") as gemini_service_cls:
            collector_cls.return_value.collect.return_value = [{"name": "vm-1", "status": "RUNNING"}]
            analyzer_cls.return_value.analyze.return_value = {
                "total_vms": 1,
                "running_vms": 1,
                "stopped_vms": 0,
                "machine_types": {"e2-medium": 1},
                "zones": {"us-central1-a": 1},
                "instances": [{"name": "vm-1", "status": "RUNNING"}],
            }
            report_cls.return_value.generate.return_value = report
            prompt_builder_cls.return_value.build.return_value = "prompt"
            gemini_service_cls.return_value.generate.return_value = "AI recommendations"

            orchestrator = FinOpsOrchestrator()
            result = orchestrator.run()

        self.assertEqual(result["ai_recommendations"], "AI recommendations")
        prompt_builder_cls.return_value.build.assert_called_once_with(report)


if __name__ == "__main__":
    unittest.main()
