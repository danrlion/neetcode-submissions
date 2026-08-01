from typing import Dict, List


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[int, int] = {}
        self.order_used: List[int] = []

    def update_lru(self, key):
        if key not in self.order_used:
            self.order_used.append(key)
        else:
            ind = self.order_used.index(key)
            for i in range(ind, len(self.order_used) - 1):
                self.order_used[i] = self.order_used[i+1]
            self.order_used[-1] = key

    def get(self, key: int) -> int:
        if key in self.cache:
            self.update_lru(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity and key not in self.cache:
            key_least_used = self.order_used[0]
            del self.cache[key_least_used]
            self.order_used = self.order_used[1:]
        self.update_lru(key)
        self.cache[key] = value
