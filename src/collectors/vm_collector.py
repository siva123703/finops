from src.services.compute_service import ComputeService


class VMCollector:
    """
    Collects VM inventory from Compute Engine.
    """

    def __init__(self):
        self.compute_service = ComputeService()

    def collect(self):
        """
        Returns all VM instances.
        """
        return self.compute_service.list_instances()