import unittest
from project import x_plus_y

class MyReturnNameFunc(unittest.TestCase):
   def test_that_x_plus_y(self):
       self.assertEqual(x_plus_y(2, 3), (5))

if __name__ == "__main__":
   unittest.main()