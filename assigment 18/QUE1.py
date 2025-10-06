class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
        print(f"Complex number created: {self}")

    def __del__(self):
        print(f"Complex number {self} destroyed.")

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"

print("=== Complex Number Operations ===")
c1 = ComplexNumber(4, 5)
c2 = ComplexNumber(2, -3)

print("\nFirst Complex Number :", c1)
print("Second Complex Number:", c2)

c3 = c1 + c2
print("\nAddition Result      :", c3)

c4 = c1 - c2
print("Subtraction Result   :", c4)

