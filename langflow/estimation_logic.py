# langflow/estimation_logic.py

def estimate_project_duration(tasks):
    total_duration = sum(task['duration'] for task in tasks)
    return total_duration

def estimate_project_cost(tasks, hourly_rate):
    total_cost = sum(task['duration'] * hourly_rate for task in tasks)
    return total_cost
