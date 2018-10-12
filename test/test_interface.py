import unittest
import context
from src import interface

class testInterface(unittest.TestCase):

    def test_get_user_input(self):
        result = interface.get_user_input()
        self.assertNotTrue("", result)

if __name__ == '__main__':
    unittest.main()
