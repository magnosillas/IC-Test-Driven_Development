import unittest
from bee1117 import notas_validas

class TesteNotasValidas(unittest.TestCase):

    def teste_notas_validas(self):
        self.assertEqual(notas_validas(-3.5 , 3.5), "nota invalida")
        self.assertEqual(notas_validas(3.5 , 10.0), 6.75)
        self.assertEqual(notas_validas(8.0 , 5.0), 6.5)
        self.assertEqual(notas_validas(4.0 , 65.0), "nota invalida")

if __name__ == '__main__':
    unittest.main()