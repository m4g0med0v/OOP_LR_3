#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дополнительно к требуемым в заданиях операциям перегрузить операцию индексирования [].
# Максимально возможный размер списка задать константой. В отдельном поле size должно
# храниться максимальное для данного объекта количество элементов списка; реализовать метод
# size(), возвращающий установленную длину. Если количество элементов списка изменяется во
# время работы, определить в классе поле count. Первоначальные значения size и count
# устанавливаются конструктором.
# В тех задачах, где возможно, реализовать конструктор инициализации строкой.

# Реализовать класс Money, используя для представления суммы денег список словарей.
# Словарь имеет два ключа: номинал купюры и количество купюр данного достоинства.
# Номиналы представить как строку. Элемент списка словарей с меньшим индексом
# содержит меньший номинал.


from typing import Dict, List, Optional


class Money:
    def __init__(
        self, initial_data: Optional[str] = None, max_size: int = 10
    ) -> None:
        # Максимальное количество элементов
        self._size: int = max_size
        # Список словарей для представления купюр
        self.data: List[Dict] = []
        # Текущее количество элементов
        self.count: int = 0

        # Инициализация через строку или список словарей
        if isinstance(initial_data, str):
            self._initialize_from_string(initial_data)
        elif isinstance(initial_data, list):
            self._initialize_from_list(initial_data)

    def _initialize_from_string(self, data_string: str) -> None:
        pairs = data_string.split(", ")
        for pair in pairs:
            denom, count = pair.split(":")
            self.add(denom.strip(), int(count.strip()))
        self.count = len(self.data)

    def _initialize_from_list(self, data_list: List[Dict]) -> None:
        for item in data_list:
            if "denomination" in item and "count" in item:
                self.add(item["denomination"], item["count"])
        self.count = len(self.data)

    def add(self, denomination: str, count: int) -> None:
        if self.count < self.size:
            # Проверяем, есть ли уже такой номинал в списке
            for item in self.data:
                if item["denomination"] == denomination:
                    item["count"] += count
                    return

            # Если номинал не найден, добавляем новый
            self.data.append({"denomination": denomination, "count": count})
            self.count += 1
            # Сортируем список по номиналу
            self.data.sort(key=lambda x: int(x["denomination"]))
        else:
            print(
                "Максимальный размер достигнут. Невозможно добавить больше элементов."
            )

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int) -> None:
        self._size = value

    def __getitem__(self, index: int) -> Dict:
        if 0 <= index < self.count:
            return self.data[index]
        else:
            raise IndexError("Индекс вне диапазона.")

    def __str__(self) -> str:
        return ", ".join(
            [f"{item['denomination']}: {item['count']}" for item in self.data]
        )

    def __len__(self) -> int:
        return self.count


if __name__ == "__main__":
    money = Money("10:5, 50:2, 100:1", max_size=5)
    print(money)

    money.add("20", 3)
    print(money)

    print(money.size)
    print(len(money))
    print(money[3])
