#!/usr/bin/env python3
#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if new_size == "Small" or new_size == "Medium" or new_size == "Large":
            self._size = new_size
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price = self.price + 1.0