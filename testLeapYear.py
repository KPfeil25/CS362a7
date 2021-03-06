import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertAlmostEqual(leapyear.leapyear(400), True)
            
if __name__ == '__main__':
    unittest.main()