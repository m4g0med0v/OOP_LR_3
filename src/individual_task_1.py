#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Выполнить индивидуальное задание 1 лабораторной работы 4.1,
# максимально задействовав имеющиеся в Python средства перегрузки
# операторов.


class Pair:
    def __init__(self, firts: int, second: int) -> None:
        # Проверка корректности диапазона
        if not (isinstance(firts, int) and isinstance(second, int)):
            raise ValueError("Оба значения должны быть целыми числами.")

        if firts >= second:
            raise ValueError("Значение first должно быть меньше значения second.")

        self.first = firts
        self.second = second

    # Ввод данных с клавиатуры
    def read(self) -> bool:
        try:
            self.first = int(input("Введите значение для first: "))
            self.second = int(input("Введите значение для second: "))
            if self.first >= self.second:
                raise ValueError("Значение first должно быть меньше значения second.")
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
            return False
        return True

    # Вывод
    def display(self) -> None:
        print(f"[{self.first}, {self.second}]")

    # Проверка, принадлежит ли число заданному интервалу
    def range_check(self, number: int) -> bool:
        return self.first <= number < self.second

    # Перегрузка оператора сложения
    def __add__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first + other.first, self.second + other.second)
        raise ValueError("Операция сложения возможна только с объектами типа Pair.")

    # Перегрузка оператора вычитания
    def __sub__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first - other.first, self.second - other.second)
        raise ValueError("Операция вычитания возможна только с объектами типа Pair.")

    # Перегрузка оператора равенства
    def __eq__(self, other):
        if isinstance(other, Pair):
            return (self.first == other.first) and (self.second == other.second)
        return False

    # Перегрузка оператора сравнения
    def __lt__(self, other):
        if isinstance(other, Pair):
            return self.first < other.first and self.second < other.second
        raise ValueError("Операция сравнения возможна только с объектами типа Pair.")

    # Перегрузка оператора строкового предстваления
    def __str__(self):
        return f"[{self.first}, {self.second})"


def make_Pair(first: int, second: int):
    try:
        return Pair(first, second)
    except ValueError as e:
        print(f"Ошибка при создании пары: {e}")
        return None


if __name__ == "__main__":
    pair1 = make_Pair(1, 5)
    pair2 = make_Pair(2, 4)

    pair1.display()
    pair2.display()

    pair3 = pair1 + pair2
    pair3.display()

    pair4 = pair1 - pair2
    pair4.display()

    print(pair1 == pair2)
    print(pair1 < pair2)
