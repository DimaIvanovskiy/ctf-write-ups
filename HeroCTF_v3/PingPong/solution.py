str = ""

with open("output.txt", "r") as file:
    for line in file:
        if line == "PING\n":
            str += "1"
        elif line == "PONG\n":
            str += "0"
        else:
            print(line)
            raise Exception("sosi")

print(str)