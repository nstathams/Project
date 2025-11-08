class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def _hash(self, key):
        if isinstance(key, str):
            hash_value = sum(ord(char) for char in key)
        else:
            hash_value = hash(key)
        return hash_value % self.size

    def put(self, key, value):
        hash_value = self._hash(key)
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        elif self.slots[hash_value] == key:
            self.data[hash_value] = value
        else:
            next_slot = (hash_value + 1) % self.size
            while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                next_slot = (next_slot + 1) % self.size

            if self.slots[next_slot] is None:
                self.slots[next_slot] = key
                self.data[next_slot] = value
            else:
                self.data[next_slot] = value

    def get(self, key, default=None):
        start_hash = self._hash(key)
        position = start_hash

        while self.slots[position] is not None:
            if self.slots[position] == key:
                return self.data[position]
            position = (position + 1) % self.size
            if position == start_hash:
                break
        return default

    def remove(self, key):
        start_hash = self._hash(key)
        position = start_hash

        while self.slots[position] is not None:
            if self.slots[position] == key:
                self.slots[position] = None
                self.data[position] = None
                self._rehash_after_remove(position)
                return
            position = (position + 1) % self.size
            if position == start_hash:
                break

    def _rehash_after_remove(self, removed_index):
        current = (removed_index + 1) % self.size
        while self.slots[current] is not None:
            key_to_reinsert = self.slots[current]
            value_to_reinsert = self.data[current]
            self.slots[current] = None
            self.data[current] = None
            self.put(key_to_reinsert, value_to_reinsert)

            current = (current + 1) % self.size

    def keys(self):
        return [key for key in self.slots if key is not None]

    def values(self):
        return [value for value in self.data if value is not None]

    def items(self):
        items_list = []
        for i in range(self.size):
            if self.slots[i] is not None:
                items_list.append((self.slots[i], self.data[i]))
        return items_list


my_hashmap = HashMap()
my_hashmap.put("name", "John")
my_hashmap.put("age", 25)
my_hashmap.put("city", "Example City")

print("Keys:", my_hashmap.keys())  # Keys: ['name', 'age', 'city']
print("Values:", my_hashmap.values())  # Values: ['John', 25, 'Example City']
print("Items:", my_hashmap.items())  # Items: [('name', 'John'), ('age', 25), ('city', 'Example City')]

print("Name:", my_hashmap.get("name"))  # Name: John
print("Gender:", my_hashmap.get("gender", "Not specified"))  # Gender: Not specified

my_hashmap.remove("age")
print("Keys after removing 'age':", my_hashmap.keys())  # Keys after removing 'age': ['name', 'city']
