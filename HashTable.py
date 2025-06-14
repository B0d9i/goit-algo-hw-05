class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash_function(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])
    
    def get(self, key):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        raise KeyError(f"Key {key} not found")
    
    def delete(self, key):
        index = self._hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                self.table[index].pop(i)
                return
        raise KeyError(f"Key {key} not found")

# Тестування
if __name__ == "__main__":
    ht = HashTable()
    ht.put("key1", "value1")
    ht.put("key2", "value2")
    print(ht.get("key1"))  #
    ht.delete("key1")
    try:
        ht.get("key1")
    except KeyError as e:
        print(e)  # key1 нема'