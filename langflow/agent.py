# langflow/agent.py

from langflow.core.agent import Agent
from langflow.estimation_logic import estimate_project_duration, estimate_project_cost

class ProjectEstimationAgent(Agent):
    def __init__(self):
        super().__init__()

    def handle_request(self, request):
        if request['type'] == 'duration':
            return estimate_project_duration(request['tasks'])
        elif request['type'] == 'cost':
            return estimate_project_cost(request['tasks'], request['hourly_rate'])
        else:
            return "Invalid request type"
