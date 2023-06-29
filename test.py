import unittest
from unittest.mock import patch
from unittest import TestCase
from weadar import get_location

class test_get_location(unittest.TestCase):
        @patch('builtins.input', side_effect=['92223', 'us'])
        def TestLocation(self, mock_inputs):
                self.assertEqual(get_location(), 'Beaumont')

if __name__ == '__main__':
        unittest.main()
