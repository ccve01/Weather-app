import unittest
from weadar import get_location, get_zipcode, get_countrycode,print_header, get_weather
from unittest import mock 
from io import StringIO
import sys


class test_get_location(unittest.TestCase):
        def test_findLocation(self):
                self.assertEqual(get_location('60632','us'), [41.8093, -87.7052])
        def test_get_zipcode(self):
                hat = mock.builtins.input
                mock.builtins.input = lambda _: '60632'
                self.assertEqual(get_zipcode('60632'), '60632')
        def test_countrycode(self):
                hat = mock.builtins.input
                mock.builtins.input = lambda _: 'us'
                self.assertEqual(get_zipcode('us'), 'us')
        def test_print_header(self):
                ben = StringIO()
                sys.stdout = ben
                print_header('Ben 10')
                sys.stdout = sys.__stdout__
                self.assertEqual(ben.getvalue(),'\nBen 10\n------\n')
        # def test_get_weather(self):
        #         with mock.patch('__main__.get_location') as MockClass:
        #             MockClass.return_value = [41.8093, -87.7052]
        #             self.assertEqual(get_weather(''),80)
        # impossible to test since it calls another function and live data is always changing 
if __name__ == '__main__':
        unittest.main()