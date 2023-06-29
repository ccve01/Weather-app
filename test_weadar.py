import unittest
import __main__
from weadar import get_location


class testFile(unittest.TestCase):
    def test_findLocation(self):
        self.assertEqual(get_location('92223', 'us'), [33.9504, -116.9701])


if __name__ == '__main__':
    unittest.main()
