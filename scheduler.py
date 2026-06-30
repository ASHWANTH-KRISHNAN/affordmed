def optimize_vehicle_tasks(vehicles, max_hours):
    """
    0/1 Knapsack.
    Duration = weight, Impact = value.
    Returns selected tasks with maximum impact within mechanic-hour limit.
    """
    n = len(vehicles)
    dp = [[0] * (max_hours + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        duration = int(vehicles[i - 1].get("Duration", 0))
        impact = int(vehicles[i - 1].get("Impact", 0))

        for hours in range(max_hours + 1):
            dp[i][hours] = dp[i - 1][hours]
            if duration <= hours:
                dp[i][hours] = max(dp[i][hours], impact + dp[i - 1][hours - duration])

    selected_tasks = []
    hours = max_hours

    for i in range(n, 0, -1):
        if dp[i][hours] != dp[i - 1][hours]:
            task = vehicles[i - 1]
            selected_tasks.append(task)
            hours -= int(task.get("Duration", 0))

    selected_tasks.reverse()

    return {
        "maxImpact": dp[n][max_hours],
        "totalDuration": sum(int(task.get("Duration", 0)) for task in selected_tasks),
        "selectedTaskIDs": [task.get("TaskID") for task in selected_tasks],
        "selectedTasks": selected_tasks,
    }
