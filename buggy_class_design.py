# buggy_class_design.py
# Contains intentional OOP bugs for AI code testing

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width + self.height  # Bug: should be multiplication

    def perimeter(self):
        return 2 * self.width + self.height  # Bug: should be 2 * (width + height)

    def is_square(self):
        return self.width == self.height


class Circle:
    PI = 3.14  # Bug: imprecise PI, should use math.pi

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * self.radius ** 2

    def circumference(self):
        return self.PI * self.radius  # Bug: should be 2 * PI * radius


class Temperature:
    def __init__(self, celsius=0):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 9/5  # Bug: should be * 5/9


class ShoppingCart:
    items = []  # Bug: mutable class variable shared across ALL instances

    def __init__(self):
        pass  # should be self.items = []

    def add_item(self, name, price, quantity=1):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def total(self):
        return sum(item["price"] for item in self.items)
        # Bug: doesn't multiply by quantity

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                # Bug: modifying list during iteration, may skip items

    def item_count(self):
        return len(self.items)  # Bug: returns distinct items, not total quantity


class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.friends = []

    def add_friend(self, other):
        self.friends.append(other)
        # Bug: doesn't add reciprocal friendship — one-directional
        # Bug: allows duplicate friends
        # Bug: allows self-friending

    def __eq__(self, other):
        return self.name == other.name  # Bug: only compares name, two "John"s are equal

    def __repr__(self):
        return f"User({self.name})"


class Matrix:
    def __init__(self, data):
        self.data = data  # Bug: stores reference, not copy — external mutations affect internal state
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match")
        result = self.data  # Bug: modifies self.data instead of creating new matrix
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] += other.data[i][j]
        return Matrix(result)

    def transpose(self):
        result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        self.data = result  # Bug: mutates in place AND returns — confusing API
        return Matrix(result)


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        return -1
        # Bug: doesn't update access order, so LRU eviction is broken

    def put(self, key, value):
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Bug: removes arbitrary key (dict ordering not guaranteed in older Python)
            first_key = next(iter(self.cache))
            del self.cache[first_key]
            # Bug: should remove LEAST recently used, not first inserted


if __name__ == "__main__":
    r = Rectangle(5, 3)
    print(f"Area: {r.area()}")  # Expect 15, get 8

    cart1 = ShoppingCart()
    cart1.add_item("Apple", 1.0, 3)
    cart2 = ShoppingCart()
    print(f"Cart2 items: {cart2.item_count()}")  # Expect 0, get 1 (shared class var)
