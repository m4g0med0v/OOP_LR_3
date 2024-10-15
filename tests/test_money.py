import unittest
from ..src.individual_task_2 import Money


class TestMoney(unittest.TestCase):
    def test_initialization_from_string(self):
        # Проверка корректной инициализации из строки
        money = Money("10:5, 50:2, 100:1", max_size=5)
        self.assertEqual(len(money), 3)
        self.assertEqual(money[0], {"denomination": "10", "count": 5})
        self.assertEqual(money[1], {"denomination": "50", "count": 2})
        self.assertEqual(money[2], {"denomination": "100", "count": 1})

    def test_initialization_from_list(self):
        # Проверка корректной инициализации из списка словарей
        data = [
            {"denomination": "10", "count": 5},
            {"denomination": "50", "count": 2},
        ]
        money = Money(data, max_size=5)
        self.assertEqual(len(money), 2)
        self.assertEqual(money[0], {"denomination": "10", "count": 5})
        self.assertEqual(money[1], {"denomination": "50", "count": 2})

    def test_addition(self):
        # Проверка добавления новых купюр
        money = Money(max_size=5)
        money.add("10", 5)
        money.add("20", 3)
        self.assertEqual(len(money), 2)
        self.assertEqual(money[0], {"denomination": "10", "count": 5})
        self.assertEqual(money[1], {"denomination": "20", "count": 3})

        # Добавление к существующему номиналу
        money.add("10", 2)
        self.assertEqual(money[0], {"denomination": "10", "count": 7})

    def test_max_size_limit(self):
        # Проверка ограничения по максимальному размеру
        money = Money(max_size=2)
        money.add("10", 1)
        money.add("20", 2)
        money.add("50", 1)  # Этот элемент не должен добавиться

        self.assertEqual(len(money), 2)
        self.assertEqual(money[0], {"denomination": "10", "count": 1})
        self.assertEqual(money[1], {"denomination": "20", "count": 2})

    def test_size_method(self):
        # Проверка метода _size()
        money = Money(max_size=5)
        self.assertEqual(money._size(), 5)

    def test_indexing(self):
        # Проверка перегрузки оператора индексирования
        money = Money("10:1, 20:2", max_size=5)
        self.assertEqual(money[0], {"denomination": "10", "count": 1})
        self.assertEqual(money[1], {"denomination": "20", "count": 2})

        # Проверка на ошибку при выходе за границы индекса
        with self.assertRaises(IndexError):
            money[2]

    def test_string_representation(self):
        # Проверка строкового представления объекта
        money = Money("10:5, 50:2, 100:1", max_size=5)
        self.assertEqual(str(money), "10: 5, 50: 2, 100: 1")

    def test_len_method(self):
        # Проверка метода __len__()
        money = Money("10:5, 50:2", max_size=5)
        self.assertEqual(len(money), 2)

        money.add("20", 3)
        self.assertEqual(len(money), 3)


if __name__ == "__main__":
    unittest.main()
