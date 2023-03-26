def list_comprehension():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    pythonic_list = [elements for elements in a if elements % 2 == 0]
    print(pythonic_list)


list_comprehension()
