from typing import List
from datetime import datetime

from src.models.Employee import Employee

class Schedule:
    def __init__(self, managerId: str, weekStart: datetime, weeksAheadCount: int, employees: List[Employee]):
        self.managerId = managerId
        self.weekStart = weekStart
        self.weeksAheadCount = weeksAheadCount
        self.employees = employees

    def toJson(self):
        result = '{'
        result += f'"ManagerId": "{self.managerId}",'
        result += '"Employees": ['

        employees_jsons = []
        for employee in self.employees:
            employees_jsons.append(employee.toJson())
        result += ','.join(employees_jsons)

        result += ']}'
            
        return result
