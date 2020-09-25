import unittest
from city_functions import get_city_information

class CityTestCase(unittest.TestCase):
    """测试city_functions.py"""
    
    def test_city_country_info(self):
        """能够正确处理city， country字符串吗"""
        message=get_city_information('santiago', 'chile')
        self.assertEqual(message, 'Santiago, Chile')
    
    def test_city_country_population(self):
        """测试城市，国家，人口字符串"""
        message=get_city_information('santiago', 'chile', 5000000)
        self.assertEqual(message, "Santiago, Chile - population 5000000")
        
unittest.main()