from collections import Counter


class VMAnalyzer:
    """
    Analyzes VM inventory and produces FinOps insights.
    """

    def analyze(self, instances):

        total_vms = len(instances)

        running_vms = [
            vm for vm in instances
            if vm["status"] == "RUNNING"
        ]

        stopped_vms = [
            vm for vm in instances
            if vm["status"] == "TERMINATED"
        ]

        machine_types = Counter(
            vm["machine_type"] for vm in instances
        )

        zones = Counter(
            vm["zone"] for vm in instances
        )

        return {
            "total_vms": total_vms,
            "running_vms": len(running_vms),
            "stopped_vms": len(stopped_vms),
            "machine_types": dict(machine_types),
            "zones": dict(zones),
            "instances": instances
        }