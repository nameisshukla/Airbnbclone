
with open("file1.txt", "r") as file:
    lines = file.read()
    lines = lines.split()
    print(lines)
    for i in lines:
        if i.isdigit():
            print(i)
        