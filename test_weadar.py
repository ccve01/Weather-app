import unittest
from weadar import get_location

class test_get_location(unittest.TestCase):
        def test_findLocation(self):
                self.assertEqual(get_location('60632','us'), [41.8093, -87.7052])

if __name__ == '__main__':
        unittest.main()