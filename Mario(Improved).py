print("\n")
name = input("Enter a name: ")
print("___________________________________")
print(name.upper(), "                WORLD    TIME")
print("004250    coins X 01   1-1      283")
print("\n")
print("                       |?|             ")


def doublePyramid(mario):
    for i in range(mario):
        for k in range(mario - i):
            print(" ", end = "")
        for k in range(i):
            print("#", end = "")
        for i in range(i, 0):
            print(i, end = "")
        for k in range(4):
            print("", end = " ")
        for k in range(i):
            print("#", end = "")
        for i in range(i, 0):
            print(i, end = "")
        print("\n")
        
doublePyramid(5)
print("_____    ______________________")
print("     |  |")
print("___________________________________")
print("\n")
