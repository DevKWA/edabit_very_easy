def list_overlap():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    a_remove_duplicates = set(a)
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    b_remove_duplicates = set(b)
    for elements in a_remove_duplicates:
        for numbers in b_remove_duplicates:
            if elements == numbers:
                print(elements & numbers)


list_overlap()


def list_overlap_oneline():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    a_remove_duplicates = set(a)
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    b_remove_duplicates = set(b)
    one_liner = [elements & numbers for elements in a_remove_duplicates for numbers in b_remove_duplicates if
                 elements == numbers]
    print(one_liner)


list_overlap_oneline()
