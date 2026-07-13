from google.cloud import compute_v1
from src.config import PROJECT_ID


class ComputeService:
    """
    Handles all Compute Engine API interactions.
    """

    def __init__(self):
        self.client = compute_v1.InstancesClient()

    def list_instances(self):
        """
        Returns all VM instances in the project.
        """

        request = compute_v1.AggregatedListInstancesRequest(
            project=PROJECT_ID
        )

        instances = []

        for zone, response in self.client.aggregated_list(request=request):

            if not response.instances:
                continue

            for instance in response.instances:

                instances.append({
                    "name": instance.name,
                    "status": instance.status,
                    "machine_type": instance.machine_type.split("/")[-1],
                    "zone": instance.zone.split("/")[-1],
                })

        return instances