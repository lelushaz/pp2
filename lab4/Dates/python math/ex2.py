def trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, first value: "))

area = trapezoid_area(base1, base2, height)
print(f"Excpected Output: {area}")