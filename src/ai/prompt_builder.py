class PromptBuilder:
    """
    Builds prompts for Gemini AI.
    """

    def build(self, report):

        summary = report["summary"]

        prompt = f"""
You are an experienced Google Cloud FinOps Engineer.

Analyze the following Compute Engine environment.

Summary

Total VMs: {summary['total_vms']}
Running VMs: {summary['running_vms']}
Stopped VMs: {summary['stopped_vms']}

Machine Types:
{summary['machine_types']}

Zones:
{summary['zones']}

Current Observations:
{report['observations']}

Provide:

1. Cost optimization recommendations
2. Rightsizing suggestions
3. Idle VM detection advice
4. Best practices
5. Estimated monthly savings if applicable

Respond in a professional report format.
"""

        return prompt