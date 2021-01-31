# 11-1 test

import unittest
from city_functions import get_city_coundtry


class CityCountreTest(unittest.TestCase):
    """Тест для 'city_functions.py'."""

    def test_city_country(self):
        """Вызов функции с такими значениями,
        как ‘santiago’ и ‘chile’, дает правильную строку. """
        formatted_city_country = get_city_coundtry('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """Работает ли вызов функции с 3 параметрами"""
        formatted_city_country_population = get_city_coundtry('santiago',
                                                              'chile',
                                                              '5000000')
        self.assertEqual(formatted_city_country_population, 'Santiago, '
                                                            'Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
