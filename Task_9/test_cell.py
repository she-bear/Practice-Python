import unittest
from cell import Cell, SubError


class TestCell(unittest.TestCase):
    def setUp(self):
        self.cell_1 = Cell(5)

    def test_init(self):
        self.assertEqual(self.cell_1.quantity, 5)

    def test_str(self):
        self.assertEqual(str(self.cell_1), '5')

    def test_add(self):
        cell_2 = Cell(2)
        ret = self.cell_1 + cell_2
        self.assertEqual(ret.quantity, 7)

    def test_add_3(self):
        cell_2 = Cell(2)
        cell_3 = Cell(10)
        ret_2 = self.cell_1 + cell_2 + cell_3
        self.assertEqual(ret_2.quantity, 17)

    def test_iadd(self):
        self.cell_1 += 5
        self.assertIsInstance(self.cell_1, Cell)
        self.assertEqual(self.cell_1.quantity, 10)

    def test_sub(self):
        cell_2 = Cell(10)
        ret = cell_2 - self.cell_1
        self.assertEqual(ret.quantity, 5)

    def test_raise(self):
        cell_2 = Cell(10)
        with self.assertRaises(SubError):
            ret_2 = self.cell_1 - cell_2

    def test_mul(self):
        cell_2 = Cell(60)
        ret = self.cell_1 * cell_2
        self.assertEqual(ret.quantity, 300)

    def test_truediv(self):
        ret = Cell(5) / Cell(3)
        self.assertEqual(ret.quantity, 1)


if __name__ == '__main__':
    unittest.main()
