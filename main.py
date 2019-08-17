print("Enter the height of the Tree!")
print("To exit type \"e\"")
while True:
    size = input("> ")
    if size == "e" or size == "exit":
        print("Bye Bye")
        break
    test = 3
    letzter = int(size) * 2 - 1
    u = int(size) - 1
    x = int(letzter / 2 - 0.5)
    lol = x + 1
    b = 5
    var = int(int(size) / 5)
    # ----------------------------------------
    # Blätter
    # ----------------------------------------
    for i in range(u):
        print(" ", end="")
    print("*")

    for i in range(u):
        for i in range(u - 1):
            print(" ", end="")
            if i == u - 2:
                u = u - 1

        for i in range(test):
            print("*", end="")
            if i == test - 1:
                print("")

            if i == test - 1:
                test = test + 2
    # ----------------------------------------
    # Stamm
    # ----------------------------------------
    for y in range(var):
        x = x - 1
    for y in range(b):
        print(" " * x, end="")
        print("*", end="")
        if int(size) % 5 == 0:
            for y in range(var):
                print("**", end="")
                if y == var - 1:
                    print("")
        else:
            for y in range(var):
                print("**", end="")
            print("")
    print("")

    if int(size) == 1:
        print("The russian stick!")