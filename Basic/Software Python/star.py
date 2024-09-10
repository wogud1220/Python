i = 0
while (i <11):
    for j in range(11):
        if (j<=i):
            print("*", end="")
        else:
            print(".", end="")
    i = i+1
    if (j>=1):
        print("")
