

# * To combine a list of stings we use join method, which is demonstrated below
# arr = ["ab", "bc", "cd"]
# print(" ".join(arr))

# *List Comprehension
# *Comprehensions means to create a type of data using for loops inside it.

# myArr = [i*i for i in range(4)]
# print(myArr)

# * Now we shall learn about hashmaps
# newSet = set()
# newSet.add(1)
# newSet.add(2)

# * There exists a thing in python where you can check whether some value is in a set or not
# print(3 in newSet)

# * List to set conversion

# list_to_set = [1, 2, 3, 4, 1, 2]
# print(set(list_to_set))

# * Set comprehension

# set_comprehension = {i for i in range(5)}
# print(set_comprehension)

# ?                                                                HASHMAPS
# *These are denoted by flower brackets.
# *They are also known as dictionaries.
# *They come in key value pairs.

# myMap = {}
# myMap["Prathik"] = 90
# myMap["Navdeep"] = 120

# *Also another way to initialize is by actually writing it entirely
# mynewMap = {"Pk": 30, "kp": 60}
# print(mynewMap)

# print(myMap)
# //{'Prathik': 90, 'Navdeep': 120}

# print(len(myMap))
# //2


# * Again we can check if a key exists in hashmap like we did it for a set
# print("Prathik" in myMap)  # *This will be true
# print(90 in myMap)
# * This will be false as this method only checks for keys and not values
# print(120 in myMap)

# *There is also dict comprehension
# myoldMap = {i: i+50 for i in range(6)}
# print(myoldMap)

# * Looping through maps:

# myMapp = {"prathik": 25, "mahesh": 50, "suresh": 40}

# *This is to print just values in the dict
# for val in myMapp.values():
#     print(val)

# *Now if you want to classify both keys and values:
# for keys, values in myMapp.items():
#     print(keys.capitalize(), "has scored", values)

# !                                                         TUPLES
# ? These are like arrays but are immutable - i.e they cannot be modified.
# ? Not very common, but is used as keys in dict or something like that
