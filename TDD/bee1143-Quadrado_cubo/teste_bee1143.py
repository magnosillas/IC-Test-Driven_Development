import unittest
from bee1143 import quadrado_cubo

class TestQuadradoCubo(unittest.TestCase):

    def test_quadrado_cubo(self):
        self.assertEqual(quadrado_cubo(1), ['1 1 1'])
        self.assertEqual(quadrado_cubo(2), ['1 1 1','2 4 8'])
        self.assertEqual(quadrado_cubo(3), ['1 1 1','2 4 8','3 9 27'])
        self.assertEqual(quadrado_cubo(5), ['1 1 1','2 4 8','3 9 27', '4 16 64', '5 25 125'])
        self.assertEqual(quadrado_cubo(8), ['1 1 1','2 4 8','3 9 27', '4 16 64', '5 25 125',
                                            '6 36 216', '7 49 343', '8 64 512'])
        
if __name__ == '__main__':
    unittest.main()