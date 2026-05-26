def classify_growth(
    observed_mutation_rate: float,
    division_rate: float,
    abnormal_marker: bool
) -> tuple[str, str]:
    if observed_mutation_rate >= 0.15 and division_rate >= 6 and abnormal_marker:
        return (
            "Cancer-like Growth Detected",
            "High mutation load, rapid division, and abnormal marker are all present."
        )

    if observed_mutation_rate >= 0.08 or division_rate >= 4 or abnormal_marker:
        return (
            "Warning",
            "One or more abnormal indicators are present. Monitoring is recommended."
        )

    return (
        "Normal",
        "Mutation and growth indicators are within safe simulated limits."
    )


def recommended_response(status: str) -> str:
    if status == "Cancer-like Growth Detected":
        return "Simulated response: activate stop-growth signal / apoptosis-like safety pathway."
    if status == "Warning":
        return "Simulated response: increase monitoring and run additional checks."
    return "Simulated response: continue normal replication."
