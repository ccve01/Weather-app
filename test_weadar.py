import unittest
import __main__
from weadar import get_location

class test_get_location(unittest.TestCase):
        def findLocation(self):
                self.assertEqual(get_location('92223', 'us'), 'Beaumont')

if __name__ == '__main__':
        unittest.main()
