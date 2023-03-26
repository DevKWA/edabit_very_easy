def calc_using_string(num1, num2, operator):
    return eval(f"{num1}{operator}{num2}")


print(calc_using_string(4, 9, "+"))
print(calc_using_string(12, 5, "-"))
print(calc_using_string(6, 3, "*"))
print(calc_using_string(25, 5, "//"))
print(calc_using_string(14, 3, "%"))
print(calc_using_string(7, 2, "/"))
