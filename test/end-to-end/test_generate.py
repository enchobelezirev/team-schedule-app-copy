import unittest
import pytest
import json
from app import app
ONE_EMPLOYEE_SCHEDULE_PATH = "test/data/sample_files/manager_single_employee.json"

class TestGenerateEndpoint(unittest.TestCase):

    def test_generate_shouldReturnEmployeesWithNextWeeksShiftsGenerated_whenEndpointIsCalledWithEmployeesPreviousShifts(self):
        # Arrange
        app.config.update({'TESTING': True})
        self.client = app.test_client()
        with open(ONE_EMPLOYEE_SCHEDULE_PATH, "r", encoding="utf-8") as file:
            sample_json = json.load(file)

        # Act
        resp = self.client.post('/generate',  json=sample_json)

        # Assert
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.json)
        self.assertTrue("manager_id" in data)
        self.assertTrue("employees" in data)
        self.assertEqual(len(data["employees"]), 1)
        self.assertTrue(len(data["employees"][0]["next_week_shifts"]) > 0)

    def test_generate_shouldReturnBadRequestError_whenSheduleNotSend(self):
        # Arrange
        app.config.update({'TESTING': True})
        self.client = app.test_client()
        
        # Act
        resp = self.client.post('/generate')

        # Assert
        assert resp.status_code == 400
        data = json.loads(resp.data)
        assert "error" in data
        assert data["error"] == "Schedule is missing or ca not be mapped"
