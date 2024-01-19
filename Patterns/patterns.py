
# ? This is for printing 4 stars in 4 rows
# def nForest(n):
#     for i in range(n):
#         for j in range(n):
#             print("*", end=" ")
#     print()
#     pass


# nForest(3)

# ? Now we move on to 2nd pattern i.e printing equal number of stars as their line number

# def pattern2(n):
#     for i in range(n):
#         for j in range(i+1):
#             print("*", end="")
#         print()


# pattern2(4)

# *Another pattern

def pattern3(n):
    for i in range(n):
        for j in range(1, i+2):
            print(j, end=' ')
        print()


pattern3(4)
