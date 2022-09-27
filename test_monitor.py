import unittest 
import json
import os
from monitor import Monitor

class TestMonitor(unittest.TestCase):

    def test_monitor_log_update(self):     
        os.environ["IS_TEST_ENV"] = "true"
        test_mock_data_file = open('test_mock_data.json')        
        data = json.load(test_mock_data_file)
        test_mock_data_file.close()
        
        #clear content of status.log 
        open('status.log', 'w').close()
        Monitor.update_log(data)

        #read log content as string into var
        log_content_file = open('status.log', 'r')
        log_content = log_content_file.read()
        log_content_file.close()
        target_string = "2022-09-26 22:10:00; CPU:1.1%; io:1.08B/s; IPv4: 3088.88Bits/s; IPv6: 51.52Bits/s\n"
        
        self.assertEqual(log_content, target_string)
        

if __name__ == '__main__':
    unittest.main()