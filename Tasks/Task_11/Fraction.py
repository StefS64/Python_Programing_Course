import math

class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        assert denominator != 0, "Denominator cannot be zero"
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def fractionFromFile(self, file_name):
        with open(file_name, 'r') as file:
            data = file.read()
            numerator, denominator = map(int, data.split('/'))
            return Fraction(numerator, denominator)

    def fractionSaveFile(self, file_name):
        with open(file_name, 'w') as file:
            file.write(f"{self.numerator}/{self.denominator}")

    def __add__(self, other: 'Fraction') -> 'Fraction':
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other: 'Fraction') -> bool:
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other: 'Fraction') -> bool:
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other: 'Fraction') -> bool:
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other: 'Fraction') -> bool:
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self) -> str:
        return f"Fraction({self.numerator}, {self.denominator})"