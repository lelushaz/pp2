def parallelogram_area(base_length, height):
    area = base_length * height
    return area

base_length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = parallelogram_area(base_length, height)
print("Expected Output:", area)