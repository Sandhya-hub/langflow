# tests/test_agent.py

import unittest
from langflow.agent import ProjectEstimationAgent

class TestProjectEstimationAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ProjectEstimationAgent()

    def test_estimate_duration(self):
        request = {
            'type': 'duration',
            'tasks': [{'duration': 5}, {'duration': 3}]
        }
        response = self.agent.handle_request(request)
        self.assertEqual(response, 8)

    def test_estimate_cost(self):
        request = {
            'type': 'cost',
            'tasks': [{'duration': 5}, {'duration': 3}],
            'hourly_rate': 50
        }
        response = self.agent.handle_request(request)
        self.assertEqual(response, 400)

if __name__ == '__main__':
    unittest.main()
