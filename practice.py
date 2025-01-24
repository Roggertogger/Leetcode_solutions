# while loop
i = 1
while i <= 5:
    print(i)
    i = i + 1


# for loop

for i in range(2):
    print("hello world")

# append and insert

mark = [21, 23, 35, 36]

mark.append(32)
mark.insert(2, 43)
print(mark)

# class and object with constructor


class student:
    name = "Apple"

    def __init__(self, id, f_name):
        self.id = id
        self.f_name = f_name
        print("constructor always work first")


s1 = student(213311035, "Bottle")
print(s1.id)
print(s1.f_name)
