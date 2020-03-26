class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.data = {}
        self.log = []

    def get(self, key: int) -> int:
        ret = self.data.get(key, -1)
        if ret != -1:
            self.log.remove(key)
            self.log.append(key)
        return ret

    def put(self, key: int, value: int) -> None:
        if self.data.get(key, ''):
            self.data[key] = value
            self.log.remove(key)
            self.log.append(key)  
        else:
            if self.size == self.capacity:
                lru = self.log.pop(0)
                print('LRU:', lru)
                del self.data[lru]
                self.size -= 1

            self.data[key] = value
            self.log.append(key)
            self.size += 1

# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2);

cache.put(2, 1);
print(cache.data)
cache.put(1, 1);
print(cache.data)
cache.put(2, 3);
print(cache.data)
cache.put(4, 1);
print(cache.data)
print(cache.get(1))
print(cache.data)
print(cache.get(2))
print(cache.data)
