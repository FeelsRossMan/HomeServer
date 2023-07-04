def get_number_from_txt():
    with open("count.txt", "r") as f:
        return f.readline()