def calculate_total_sum(*arguments):
    totalSum = []
    for number in arguments:
        totalSum.append(number)
        first_element = totalSum[0]
        return first_element


print(calculate_total_sum(5, 4, 3, 2, 1))
print(calculate_total_sum(11, 33, 22, 99, 100))
print(calculate_total_sum(111, 0, 2, 90, 8))