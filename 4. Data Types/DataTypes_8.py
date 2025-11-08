class SimpleMap:
    def __init__(self):
        self._items = []

    def set(self, key, value):
        for i, (k, v) in enumerate(self._items):
            if k == key:
                self._items[i] = (key, value)
                return
        self._items.append((key, value))

    def get(self, key, default=None):
        for k, v in self._items:
            if k == key:
                return v
        return default

    def remove(self, key):
        for i, (k, v) in enumerate(self._items):
            if k == key:
                del self._items[i]
                return

    def keys(self):
        return [k for k, v in self._items]

    def values(self):
        return [v for k, v in self._items]

    def items(self):
        return self._items.copy()



# Пример использования
my_map = SimpleMap()

my_map.set("name", "John")
my_map.set("age", 25)
my_map.set("city", "Example City")

print("Keys:", my_map.keys())
print("Values:", my_map.values())
print("Items:", my_map.items())

# Accessing values by key
print("Name:", my_map.get("name"))
print("Gender:", my_map.get("gender", "Not specified"))

# Removing a key-value pair
my_map.remove("age")

print("Keys after removing 'age':", my_map.keys())
