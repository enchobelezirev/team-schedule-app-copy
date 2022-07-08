import unittest
import pytest
import json
from app import app
ONE_EMPLOYEE_SCHEDULE_PATH = "test/data/sample_files/manager_single_employee.json"

class TestGenerateEndpoint(unittest.TestCase):

    def create_client(self):
        app.config.update({'TESTING': True})
        self.client = app.test_client()
        with app.test_client() as self.client:
            yield self.client

    def test_generate_endpoint(self):
        app.config.update({'TESTING': True})
        self.client = app.test_client()
        with open(ONE_EMPLOYEE_SCHEDULE_PATH, "r", encoding="utf-8") as file:
            sample_json = json.load(file)
        resp = self.client.post('/generate',  json=sample_json)

        assert resp.status_code == 200
        data = json.loads(resp.json)
        assert "manager_id" in data
        assert "employees" in data
        assert 1 == len(data["employees"])
        assert 0 < len(data["employees"][0]["next_week_shifts"])