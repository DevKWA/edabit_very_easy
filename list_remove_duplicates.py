def list_remove_duplicates_set():
    a = [11, 11, 22, 3, 34, 5, 5, 7, 8, 1, 2, ]
    b = set(a)
    c = sorted(b)
    print(c)


list_remove_duplicates_set()


def list_remove_duplicates_for_loop():
    a = [11, 22, 3, 4, 5, 5, 6, 7, 88, 88, 9, 12, 3, 4]
    b = []
    for numbers in a:
        if numbers not in b:
            b.append(numbers)
    print(b)


list_remove_duplicates_for_loop()
