# Day19_LRU_Cache.py
"""
Problem: Implement LRU Cache using OrderedDict
"""

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()  # Maintain insertion order
        self.size = capacity        # Max size of cache

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # Mark as recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)  # Remove LRU item

# Example usage
if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))  # Output: 1
    lru.put(3, 3)
    print(lru.get(2))  # Output: -1
    lru.put(4, 4)
    print(lru.get(1))  # Output: -1
    print(lru.get(3))  # Output: 3
    print(lru.get(4))  # Output: 4
