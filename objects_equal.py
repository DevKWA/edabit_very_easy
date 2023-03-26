def object_equals(obj_one, obj_two):
    if obj_one == obj_two:
        return True
    else:
        return False


print(object_equals(obj_one=3, obj_two=4))
print(object_equals(obj_one=4, obj_two=4))
print(object_equals(obj_one={"phone": "3325558745",
                             "email": "benny@edabit.com"
                             }, obj_two={"name": "Jason",
                                         "phone": "9853759720",
                                         "email": "jason@edabit.com"}))
