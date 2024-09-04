c
for i in range(100):
    if i < 99:
        print("{:02}".format(i), end=", ")
    else:
        print(f"{i} \n")
