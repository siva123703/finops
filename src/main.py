import functions_framework
from src.orchestrator.finops import run_finops_analysis


@functions_framework.http
def finops_agent(request):

    result = run_finops_analysis()

    return result