import pytest

from src.individual_task_1 import Pair, make_Pair


class TestPair:
    def test_initialization_valid(self):
        pair = Pair(1, 5)
        assert pair.first == 1
        assert pair.second == 5

    def test_initialization_invalid(self):
        with pytest.raises(ValueError):
            Pair(5, 1)

        with pytest.raises(ValueError):
            Pair("a", 5)

        with pytest.raises(ValueError):
            Pair(1, "b")

    def test_read_valid(self):
        pass

    def test_display(self):
        pass

    def test_range_check(self):
        pair = Pair(1, 5)
        assert pair.range_check(3) is True
        assert pair.range_check(5) is False
        assert pair.range_check(0) is False

    def test_addition(self):
        pair1 = Pair(1, 5)
        pair2 = Pair(2, 6)
        pair3 = pair1 + pair2
        assert pair3.first == 3
        assert pair3.second == 11

    def test_subtraction(self):
        pair1 = Pair(5, 10)
        pair2 = Pair(2, 4)
        pair3 = pair1 - pair2
        assert pair3.first == 3
        assert pair3.second == 6

        with pytest.raises(ValueError):
            Pair(5, 10) - Pair(5, 10)

    def test_equality(self):
        pair1 = Pair(1, 5)
        pair2 = Pair(1, 5)
        pair3 = Pair(2, 6)
        assert pair1 == pair2
        assert pair1 != pair3

    def test_comparison(self):
        pair1 = Pair(1, 5)
        pair2 = Pair(2, 6)
        assert pair1 < pair2
        assert not pair2 < pair1

        with pytest.raises(ValueError):
            pair1 < 5  # Сравнение с несоответствующим типом

    def test_make_pair_valid(self):
        pair = make_Pair(1, 5)
        assert pair is not None
        assert pair.first == 1
        assert pair.second == 5

    def test_make_pair_invalid(self):
        with pytest.raises(ValueError):
            assert make_Pair(5, 1) is None
            assert make_Pair("a", 5) is None
            assert make_Pair(1, "b") is None
