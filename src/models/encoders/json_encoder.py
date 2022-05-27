"""JSON-Encoder for module data-model."""
import json

from src.models.employee import Employee
from models.schedule1 import Schedule
from src.models.shift import Shift


class JSONEncoder(json.JSONEncoder):
    """JSON-Encoder class for data-model."""

    def default(self, o):
        """
        Return JSON-encoded dictionary for object o.

        Parameters
        ----------
        o : object to be JSON-encoded
        """
        if isinstance(o, Employee):
            json_struct = {
                "user_id": o.uid,
                "next_week_shifts": o.nextWeekShifts,
            }
            return json_struct

        elif isinstance(o, Shift):
            json_struct = {
                "start_time": str(o.startTime),
                "end_time": str(o.endTime),
                "duration": o.duration,
            }

            return json_struct

        elif isinstance(o, Schedule):
            json_struct = {
                "manager_id": o.managerId,
                "employees": o.employees,
            }

            return json_struct
