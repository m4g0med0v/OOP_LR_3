import pytest

from src.individual_task_2 import Money


class TestMoney:
    def test_initialization_from_string(self):
        money = Money("10:5, 50:2, 100:1", max_size=5)
        assert len(money) == 3
        assert money[0] == {"denomination": "10", "count": 5}
        assert money[1] == {"denomination": "50", "count": 2}
        assert money[2] == {"denomination": "100", "count": 1}

    def test_initialization_from_list(self):
        data = [
            {"denomination": "10", "count": 5},
            {"denomination": "50", "count": 2},
        ]
        money = Money(data, max_size=5)
        assert len(money) == 2
        assert money[0] == {"denomination": "10", "count": 5}
        assert money[1] == {"denomination": "50", "count": 2}

    def test_addition(self):
        money = Money(max_size=5)
        money.add("10", 5)
        money.add("20", 3)
        assert len(money) == 2
        assert money[0] == {"denomination": "10", "count": 5}
        assert money[1] == {"denomination": "20", "count": 3}

        # Добавление к существующему номиналу
        money.add("10", 2)
        assert money[0] == {"denomination": "10", "count": 7}

    def test_max_size_limit(self):
        money = Money(max_size=2)
        money.add("10", 1)
        money.add("20", 2)
        money.add("50", 1)  # Этот элемент не должен добавиться

        assert len(money) == 2
        assert money[0] == {"denomination": "10", "count": 1}
        assert money[1] == {"denomination": "20", "count": 2}

    def test_size_method(self):
        money = Money(max_size=5)
        assert money.size == 5

    def test_indexing(self):
        money = Money("10:1, 20:2", max_size=5)
        assert money[0] == {"denomination": "10", "count": 1}
        assert money[1] == {"denomination": "20", "count": 2}

        with pytest.raises(IndexError):
            money[2]

    def test_string_representation(self):
        money = Money("10:5, 50:2, 100:1", max_size=5)
        assert str(money) == "10: 5, 50: 2, 100: 1"

    def test_len_method(self):
        money = Money("10:5, 50:2", max_size=5)
        assert len(money) == 2

        money.add("20", 3)
        assert len(money) == 3
