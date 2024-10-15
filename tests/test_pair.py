import unittest

from ..src.individual_task_1 import Pair, make_Pair


class TestPair(unittest.TestCase):
    def test_initialization_valid(self):
        # Проверка корректной инициализации
        pair = Pair(1, 5)
        self.assertEqual(pair.first, 1)
        self.assertEqual(pair.second, 5)

    def test_initialization_invalid(self):
        # Проверка некорректной инициализации
        with self.assertRaises(ValueError):
            Pair(5, 1)

        with self.assertRaises(ValueError):
            Pair("a", 5)

        with self.assertRaises(ValueError):
            Pair(1, "b")

    def test_read_valid(self):
        pass

    def test_display(self):
        pass

    def test_range_check(self):
        # Проверка принадлежности числа интервалу.
        pair = Pair(1, 5)
        self.assertTrue(pair.range_check(3))
        self.assertFalse(pair.range_check(5))
        self.assertFalse(pair.range_check(0))

    def test_addition(self):
        # Проверка перегрузки оператора сложения.
        pair1 = Pair(1, 5)
        pair2 = Pair(2, 6)
        pair3 = pair1 + pair2
        self.assertEqual(pair3.first, 3)
        self.assertEqual(pair3.second, 11)

    def test_subtraction(self):
        # Проверка перегрузки оператора вычитания.
        pair1 = Pair(5, 10)
        pair2 = Pair(2, 4)
        pair3 = pair1 - pair2
        self.assertEqual(pair3.first, 3)
        self.assertEqual(pair3.second, 6)

        # Проверка некорректного результата (first >= second).
        with self.assertRaises(ValueError):
            Pair(5, 10) - Pair(5, 10)

    def test_equality(self):
        # Проверка перегрузки оператора равенства.
        pair1 = Pair(1, 5)
        pair2 = Pair(1, 5)
        pair3 = Pair(2, 6)
        self.assertTrue(pair1 == pair2)
        self.assertFalse(pair1 == pair3)

    def test_comparison(self):
        # Проверка перегрузки оператора сравнения.
        pair1 = Pair(1, 5)
        pair2 = Pair(2, 6)
        self.assertTrue(pair1 < pair2)
        self.assertFalse(pair2 < pair1)

        # Проверка некорректного сравнения.
        with self.assertRaises(ValueError):
            pair1 < 5  # Сравнение с несоответствующим типом

    def test_make_pair_valid(self):
        # Проверка создания пары с помощью make_Pair.
        pair = make_Pair(1, 5)
        self.assertIsNotNone(pair)
        self.assertEqual(pair.first, 1)
        self.assertEqual(pair.second, 5)

    def test_make_pair_invalid(self):
        # Проверка создания пары с некорректными значениями.
        pair = make_Pair(5, 1)
        self.assertIsNone(pair)

        pair = make_Pair("a", 5)
        self.assertIsNone(pair)

        pair = make_Pair(1, "b")
        self.assertIsNone(pair)


if __name__ == "__main__":
    unittest.main()
