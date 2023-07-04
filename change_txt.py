
def change_txt():
    current = ""

    #reading
    file = open("count.txt", "r")
    current = file.readline()
    print(current)

    #writing
    file = open("count.txt", "w")
    if current == "":
        file.write("1")
    else:
        file.write(str(int(current) + 1))
