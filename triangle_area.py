def triangle_area(base, height, shape):
    triangle = 0.5 * base * height
    parallelogram = base * height
    return triangle if shape == "triangle" else parallelogram


print(triangle_area(2, 3, "triangle"))
print(triangle_area(8, 6, "parallelogram"))
print(triangle_area(2.9, 1.3, "parallelogram"))
