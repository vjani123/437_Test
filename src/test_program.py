import unittest

from program import add 
from program import divide

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1,2),3)
    def test_bad_add(self): 
        self.assertNotEqual(add(1,2),2)
    def divide(self):
        self.asserEqual(divide(4,2),2)
if __name__  == '__main__':
     unittest.main()    

