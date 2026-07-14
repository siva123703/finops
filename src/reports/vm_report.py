class VMReport:
    """
    Generates a FinOps report from analyzed VM data.
    """

    def generate(self, analysis):

        observations = []

        if analysis["running_vms"] == analysis["total_vms"]:
            observations.append(
                "All VM instances are currently running."
            )

        if analysis["stopped_vms"] > 0:
            observations.append(
                f"{analysis['stopped_vms']} VM(s) are stopped."
            )

        if len(analysis["machine_types"]) == 1:
            observations.append(
                "All VMs use the same machine type."
            )

        if len(analysis["zones"]) == 1:
            observations.append(
                "All VMs are deployed in a single zone."
            )

        report = {
            "summary": {
                "total_vms": analysis["total_vms"],
                "running_vms": analysis["running_vms"],
                "stopped_vms": analysis["stopped_vms"],
                "machine_types": analysis["machine_types"],
                "zones": analysis["zones"]
            },
            "observations": observations,
            "instances": analysis["instances"]
        }

        return report