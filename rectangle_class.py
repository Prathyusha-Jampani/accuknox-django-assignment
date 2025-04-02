class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._data = [{'length': self.length}, {'width': self.width}]
        self._index = 0  # For iteration
    def __iter__(self):
        self._index = 0  # Reset iteration state
        return self
    def __next__(self):
        if self._index < len(self._data):
            result = self._data[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration
# Example usage
rect = Rectangle(10, 5)
for value in rect:
    print(value)
