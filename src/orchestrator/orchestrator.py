from src.ai.gemini_service import GeminiService
from src.ai.prompt_builder import PromptBuilder
from src.collectors.vm_collector import VMCollector
from src.analyzers.vm_analyzer import VMAnalyzer
from src.reports.vm_report import VMReport


class FinOpsOrchestrator:

    def __init__(self):
        self.collector = VMCollector()
        self.analyzer = VMAnalyzer()
        self.report = VMReport()
        self.prompt_builder = PromptBuilder()
        self.gemini_service = GeminiService()

    def run(self, user_message=None):

        instances = self.collector.collect()

        analysis = self.analyzer.analyze(instances)

        report = self.report.generate(analysis)

        prompt = self.prompt_builder.build(report)
        if user_message:
            prompt = f"User question: {user_message}\n\n{prompt}"

        ai_recommendations = self.gemini_service.generate(prompt)

        report["ai_recommendations"] = ai_recommendations
        report["user_message"] = user_message

        return report