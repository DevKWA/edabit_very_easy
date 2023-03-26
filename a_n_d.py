def a_n_d(num1, num2):
    return num1 and num2


print(a_n_d(1, 1))
print(a_n_d(0, 0))


def o_r(num1, num2):
    return num1 or num2


print(o_r(1, 0))
print(o_r(1, 1))


def n_o_t(num1):
    return 0 if num1 == 1 else 1


print(n_o_t(0))
print(n_o_t(1))
