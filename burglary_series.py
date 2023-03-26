def angry_words(*insults_dictionary):
    for key in insults_dictionary:
        print(key)
        return len(key)


print(angry_words({"a": "dumb", "b": "idiot", "c": "scumbag"}))
print(angry_words({"a": "dumb", "b": "idiot", "c": "scumbag", "d": "asshole", "e": "bitch"}))

