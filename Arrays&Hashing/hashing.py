
# todo:                                                 Hashing!!
# def numHashing():
#     n = int(input("Enter the size of the array:\t"))
#     newList = []

#     # *Here you are accepting the array elements
#     print("Now enter the array elements")
#     for i in range(0, n):
#         ele = int(input())
#         newList.append(ele)

#     max_size = 13
#     # * Now you create a hash array with a max size of max_size
#     # ? So this is how you create a hash array : array_name = [0] * some size
#     hash_table = [0] * max_size  # ! Remember this syntax :)
#     for i in range(n):
#         hash_table[newList[i]] += 1

#     # * This is where we start execution of the queries

#     q = int(input("How many times do you want to execute the query:\n"))

#     for i in range(q):
#         number = int(
#             input("Enter the number you want to know how many times it has repeated:\t"))
#         if number > max_size:
#             print("Please enter a number below ", max_size)
#         print(number, " has repeated ", hash_table[number], "times")


#  todo:                                                                        Character Hashing

newString = input("Enter the string:\n")

hashArray = [0] * 256  # ! Another reminder about the syntax of hashing
# ? This for loop means, for every single value(i) in the string, count it's appearance and add it inside hash array, converting it into ascii
for i in newString:
    # ! While working with ascii values in python, to convert any character into it's ascii values, there is a method called ord()
    hashArray[ord(i)] += 1

query = int(
    input("Enter the number of times you want to execute the query:\n"))

for i in range(query):
    c = input("Enter the element you want to search for:\t")
    print(c, "has been repeated for", hashArray[ord(c)], "times")
