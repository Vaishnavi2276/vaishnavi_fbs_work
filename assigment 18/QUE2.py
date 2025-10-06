class Distance:
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
        print(f"Constructor called: Distance created ({self.km} km, {self.m} m, {self.cm} cm)")

    def __del__(self):
        print(f"Destructor called: Distance ({self.km} km, {self.m} m, {self.cm} cm) deleted")

    def normalize(self):
        if self.cm >= 100:
            self.m += self.cm // 100
            self.cm = self.cm % 100

        if self.m >= 1000:
            self.km += self.m // 1000
            self.m = self.m % 1000

        if self.cm < 0:
            self.m -= 1
            self.cm += 100
        if self.m < 0:
            self.km -= 1
            self.m += 1000

    def __add__(self, other):
        new_km = self.km + other.km
        new_m = self.m + other.m
        new_cm = self.cm + other.cm
        result = Distance(new_km, new_m, new_cm)
        result.normalize()
        return result

    def __sub__(self, other):
        new_km = self.km - other.km
        new_m = self.m - other.m
        new_cm = self.cm - other.cm
        result = Distance(new_km, new_m, new_cm)
        result.normalize()
        return result

    def __str__(self):
        return f"{self.km} km, {self.m} m, {self.cm} cm"

print("=== Distance Operations ===")

d1 = Distance(2, 800, 75)
d2 = Distance(1, 500, 50)

print("\nDistances:")
print("d1 =", d1)
print("d2 =", d2)

d3 = d1 + d2
print("\nAddition (d1 + d2):", d3)

d4 = d1 - d2
print("Subtraction (d1 - d2):", d4)
