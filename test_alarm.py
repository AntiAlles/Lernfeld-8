import unittest 
import json
import os
from alarm import Alarm

class TestAlarm(unittest.TestCase):

    def test_alarm_CPU_over_threshold(self):     
        os.environ["IS_TEST_ENV"] = "true"
        test_mock_data_file = open('test_mock_data.json')        
        data = json.load(test_mock_data_file)
        test_mock_data_file.close()

        response = Alarm.is_CPU_over_threshold(data, 0)
        self.assertEqual(response, True)

    def test_alarm_CPU_under_threshold(self):
        os.environ["IS_TEST_ENV"] = "true"
        test_mock_data_file = open('test_mock_data.json')        
        data = json.load(test_mock_data_file)
        test_mock_data_file.close()

        response = Alarm.is_CPU_over_threshold(data, 100)
        self.assertEqual(response, False)

    def test_alarm_IO_over_threshold(self):     
        os.environ["IS_TEST_ENV"] = "true"
        test_mock_data_file = open('test_mock_data.json')        
        data = json.load(test_mock_data_file)
        test_mock_data_file.close()

        response = Alarm.is_IO_over_threshold(data, 0)
        self.assertEqual(response, True)

    def test_alarm_IO_under_threshold(self):
        os.environ["IS_TEST_ENV"] = "true"
        test_mock_data_file = open('test_mock_data.json')        
        data = json.load(test_mock_data_file)
        test_mock_data_file.close()

        response = Alarm.is_IO_over_threshold(data, 6)
        self.assertEqual(response, False)

if __name__ == '__main__':
    unittest.main()