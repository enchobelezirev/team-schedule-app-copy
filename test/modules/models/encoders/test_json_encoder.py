import unittest

from src.models.encoders.json_encoder import JSONEncoder
from src.models.shift import Shift


class TestJSONEncoder(unittest.TestCase):
    def test_default_shouldEncodeCorrectly_whenGivenShiftObject(self):
        # Arrange
        encoder = JSONEncoder()
        shift = Shift(1111111, 222222, 1000)
        
        # Act
        shift_json = encoder.default(shift)
        
        # Assert
        self.assertEqual(shift_json["start_time"], str(1111111))
        self.assertEqual(shift_json["end_time"], str(222222))
        self.assertEqual(shift_json["duration"], 1000)
