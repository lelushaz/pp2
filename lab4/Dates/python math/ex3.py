import math
def regular_polygon_area(num, length):
    area = (num * length ** 2) / (4 * math.tan(math.pi / num))
    return area
num= int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))

area = regular_polygon_area(num, length)
print(f"The area of the polygon is: {area}")