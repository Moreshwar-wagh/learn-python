with open("files/learning_python.txt") as file_object:
    contents = file_object.readlines()

for line in contents:
    line = line.strip()
    print(line.replace("Python", "Java"))
