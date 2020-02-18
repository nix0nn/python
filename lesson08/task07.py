class ComplexDigit:
    def __init__(self, nums):
        self.nums = nums

    def __add__(self, other):
        return self.nums + other.nums

    def __mul__(self, other):
        return self.nums * other.nums


a = ComplexDigit(complex(1, 5))
b = ComplexDigit(complex(2, 6))

print(a + b)
print(a * b)