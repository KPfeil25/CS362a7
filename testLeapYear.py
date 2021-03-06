import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyear.leapyear(400), True)
    def test2(self):
        self.assertEqual(leapyear.leapyear(4), True)
    def test3(self):
        self.assertEqual(leapyear.leapyear(100), False)

if __name__ == '__main__':
    unittest.main()