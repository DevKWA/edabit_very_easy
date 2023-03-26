def return_negative(num):
    if num == abs(num):
        return -num
    return num


print(return_negative(4))
print(return_negative(15))
print(return_negative(-4))
print(return_negative(0))
