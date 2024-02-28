## test_value_return.py

import unittest
from homework.e_functions.value_return import get_hour, get_minutes, get_seconds

class TestValueReturnFunctions(unittest.TestCase):

    def test_get_hour(self):
        # Test cases for get_hour function
        self.assertEqual(get_hour(3600), 1)  # 1 hour
        self.assertEqual(get_hour(7200), 2)  # 2 hours
        self.assertEqual(get_hour(86400), 0)  # 0 hours (24 hours)
        self.assertEqual(get_hour(90000), 1)  # 1 hour after 24 hours

    def test_get_minutes(self):
        # Test cases for get_minutes function
        self.assertEqual(get_minutes(60), 1)  # 1 minute
        self.assertEqual(get_minutes(3660), 1)  # 1 minute after 1 hour
        self.assertEqual(get_minutes(3600), 0)  # 0 minutes
        self.assertEqual(get_minutes(3661), 1)  # 1 minute after 1 hour 1 second

    def test_get_seconds(self):
        # Test cases for get_seconds function
        self.assertEqual(get_seconds(1), 1)  # 1 second
        self.assertEqual(get_seconds(61), 1)  # 1 second after 1 minute
        self.assertEqual(get_seconds(3601), 1)  # 1 second after 1 hour
        self.assertEqual(get_seconds(3600), 0)  # 0 seconds

if __name__ == '__main__':
    unittest.main()
