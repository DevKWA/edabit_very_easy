def city_school_ids(string_1, string_2):
    return string_1[0].lower() + string_2[0].upper() + string_2[1:3].lower()


print(city_school_ids("mary", "lamb"))
print(city_school_ids("John", "SMITH"))
print(city_school_ids("mary", "smith"))
