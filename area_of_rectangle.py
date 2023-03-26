def area_of_rect(length, width):
    if length * width == 0 or length * width != abs(length * width):
        return -1
    return length * width


print(area_of_rect(3, 4))
print(area_of_rect(10, 11))
print(area_of_rect(-1, 5))
print(area_of_rect(0, 2))
