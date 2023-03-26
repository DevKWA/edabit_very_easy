def list_ends():
    a = [1, 2, 3, 4, 5, 6]
    b = list(a[0:1] + a[-1:-2:-1])
    print(b)


list_ends()
