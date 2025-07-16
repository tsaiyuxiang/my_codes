# jar.py
class Jar:

    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError("capacity must be greater than 0")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n <= 0 or self.size + n > self.capacity:
            raise ValueError("can not deposit")
        else :
            self.size += n

    def withdraw(self, n):
        if n <= 0 or self.size < n :
            raise ValueError("can not deposit")
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("capacity must be greater than 0")
        else:
            self._capacity = value

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("size must can't be negative")
        else:
            self._size = value




