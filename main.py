from src import main as src_main


def finops_agent(request=None):
    return src_main.finops_agent(request)


__all__ = ["finops_agent"]
