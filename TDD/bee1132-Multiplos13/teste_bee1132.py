import unittest
from bee1132 import sum_multiplo13

class TesteSumMultiplos13(unittest.TestCase):

    def teste_sum_multiplos13(self):
        self.assertEqual(sum_multiplo13(100 , 200), 13954)
        self.assertEqual(sum_multiplo13(80 , 100), 1799)
        self.assertEqual(sum_multiplo13(17 , 176), 14270)
        self.assertEqual(sum_multiplo13(200 , 87), 15072)
        self.assertEqual(sum_multiplo13(500 , 550), 24669)

if __name__ == '__main__':
    unittest.main()