import unittest
from proiectFinal import Proiect
class Test1(unittest.TestCase):
    def setUp(self):
        self.__proiect = Proiect()
        self.result = self.__proiect.count("test2.txt")
        self.result2 = self.__proiect.average_run_time_excluding_system("test2.txt")
        self.result3 = self.__proiect.count_app_failures3("test2.txt")
        self.result41, self.result42  = self.__proiect.count_app_failures("test2.txt")
        self.result51, self.result52  = self.__proiect.app_with_most_successful_runs("test2.txt")
        self.result61, self.result62 = self.__proiect.third_of_day_with_most_failures("test2.txt")
        self.result7= self.__proiect.run_times_per_app("test2.txt")
        self.result8= self.__proiect.busiest_hour_per_app("test2.txt")
        self.result9= self.__proiect.calculate_failure_rates("test2.txt")
        self.result10= self.__proiect.run_times_per_app("test2.txt")


    def test_(self):
        print(self.result[('INFO', 'BackendApp')])
        self.assertEqual(self.result[('ERROR', 'BackendApp')],1)
        self.assertEqual(self.result[('INFO', 'BackendApp')],4.5)
        self.assertEqual(self.result[('INFO', 'API')],3)
        self.assertEqual(self.result[('DEBUG', 'SYSTEM')],1)
        self.assertEqual(self.result[('ERROR', 'API')],1)
        self.assertEqual(self.result[('DEBUG', 'API')],1)
        self.assertEqual(self.result[('DEBUG', 'FrontendApp')],2)
    
    def test_2(self):
        self.assertEqual(self.result2[('BackendApp')],13.4)
        self.assertEqual(self.result2[('API')],18.67)

    def test_3(self):
        self.assertEqual(self.result3.get('FrontendApp'), 0)
        self.assertEqual(self.result3.get('BackendApp'),1)
        self.assertEqual(self.result3.get('API'),1)
        self.assertEqual(self.result3.get('SYSTEM'),0)

    def test_4(self):
        self.assertEqual(self.result41,"BackendApp")
        self.assertEqual(self.result42,1)

    def test_5(self):
        self.assertEqual(self.result51,"BackendApp")
        self.assertEqual(self.result52,5)

    def test_6(self):
        self.assertEqual(self.result61,'00:00:00 - 07:59:59')
        self.assertEqual(self.result62,1)
    
    def test_7(self):
        self.assertEqual(self.result7[0].get('BackendApp'),('12:26:42', 18))
        self.assertEqual(self.result7[0].get('API'), ('03:42:50', 22))
        self.assertEqual(self.result7[1].get('BackendApp'),('13:08:50', 5))
        self.assertEqual(self.result7[1].get('API'),('17:23:35', 14))

    def test_8(self):
        self.assertEqual(self.result8.get('BackendApp'),('12', 3))
        self.assertEqual(self.result8.get('API'), ('17', 4))
        self.assertEqual(self.result8.get('FrontendApp'),('13', 1))

    
    def test_9(self):    
        self.assertEqual(self.result9.get('BackendApp'), 10.0)
        self.assertEqual(self.result9.get('API'), 12.50)
        self.assertEqual(self.result9.get('SYSTEM'), 0.0)
        self.assertEqual(self.result9.get('FrontendApp'), 0.0)
    
    def test_10(self):
        self.assertEqual(self.result10[0].get('BackendApp'),('12:26:42', 18))
        self.assertEqual(self.result10[0].get('API'), ('03:42:50', 22))
        self.assertEqual(self.result10[1].get('BackendApp'),('13:08:50', 5))
        self.assertEqual(self.result10[1].get('API'),('17:23:35', 14))

        

if __name__ == '__main__':
    unittest.main()
