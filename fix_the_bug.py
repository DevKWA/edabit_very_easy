def find_the_bug(product):
    matches = {
        "Bread": "Bag",
        "Milk": "Bottle",
        "Beer": "Can",
        "Eggs": "Carton",
        "Cerial": "Box",
        "Candy": "Bar",
        "Cheese": "Wrapper"
    }
    return matches[product]


print(find_the_bug("Bread"))
print(find_the_bug("Milk"))
print(find_the_bug("Beer"))
print(find_the_bug("Eggs"))
print(find_the_bug("Cerial"))
print(find_the_bug("Candy"))
print(find_the_bug("Cheese"))
