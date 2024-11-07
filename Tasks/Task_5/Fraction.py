import math

class Fraction:
    def __init__(self, numerator, denominator):
        assert denominator != 0, "Denominator cannot be zero"
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

# Testowanie klasy Fraction

u1 = Fraction(1, 2)
u2 = Fraction(3, 4)
u3 = Fraction(-1, 2)

print(f"u1: {u1}")
print(f"u2: {u2}")
print(f"u3: {u3}")
print(f"u4: {u4}")

print(f"u1 + u2: {u1 + u2}")
print(f"u1 - u2: {u1 - u2}")
print(f"u1 * u2: {u1 * u2}")
print(f"u1 / u2: {u1 / u2}")

print(f"u1 == u2: {u1 == u2}")
print(f"u1 != u2: {u1 != u2}")
print(f"u1 < u2: {u1 < u2}")
print(f"u1 <= u2: {u1 <= u2}")
print(f"u1 > u2: {u1 > u2}")
print(f"u1 >= u2: {u1 >= u2}")

print(f"u1 + u3: {u1 + u3}")
print(f"u1 - u3: {u1 - u3}")
print(f"u1 * u3: {u1 * u3}")
print(f"u1 / u3: {u1 / u3}")

print(f"u1 == u3: {u1 == u3}")
print(f"u1 != u3: {u1 != u3}")
print(f"u1 < u3: {u1 < u3}")
print(f"u1 <= u3: {u1 <= u3}")
print(f"u1 > u3: {u1 > u3}")
print(f"u1 >= u3: {u1 >= u3}")