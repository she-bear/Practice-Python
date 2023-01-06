import unittest
import tasks_def


class TestCell(unittest.TestCase):
    def test_division(self):
        self.assertNotEqual(tasks_def.func_division(10, 2), 6)

    def test_division_raise(self):
        with self.assertRaises(ZeroDivisionError):
            tasks_def.func_division(10, 0)

    def test_classes(self):
        self.assertNotIsInstance(tasks_def.TrafficLight, tasks_def.Stationery)


if __name__ == '__main__':
    unittest.main()
