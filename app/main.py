from __future__ import annotations
from typing import Hashable, Any


class SuperPuperNode:
    def __init__(
            self,
            key: Hashable,
            value: Any,
            next_node: SuperPuperNode = None,
            hash_value: Hashable = None
    ) -> None:
        self.key = key
        self.value = value
        self.hash_value = hash_value
        self.next_node = next_node


class Dictionary:
    def __init__(self) -> None:
        self.temp_table = None
        self.size = 8
        self.load = 0
        self.hash_table = self.create_buckets()

    def create_buckets(self) -> list:
        return [None] * self.size

    def resize_table(self) -> None:
        self.load = 0
        self.size = self.size * 2
        self.temp_table = self.hash_table
        self.hash_table = self.create_buckets()
        for bucket in self.temp_table:
            if bucket:
                current = bucket
                while current:
                    self.__setitem__(current.key, current.value)
                    current = current.next_node
        self.temp_table = None

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.load >= self.size * (2 / 3):
            self.resize_table()

        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        if bucket is not None:
            current = bucket
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next_node

        new_node = SuperPuperNode(
            key,
            value,
            self.hash_table[hashed_key],
            hash(key)
        )
        self.hash_table[hashed_key] = new_node
        self.load += 1

    def __getitem__(self, key: Hashable) -> Any:
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        if bucket is not None:
            current = bucket
            while current:
                if current.key == key:
                    return current.value
                current = current.next_node

        raise KeyError("There is no such key in KostiaDict")

    def __len__(self) -> int:
        return self.load

    def __str__(self) -> str:
        return "".join(str(item) for item in self.hash_table)
