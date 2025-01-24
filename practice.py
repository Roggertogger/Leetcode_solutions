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

    def method_1(self):
        print("this is the ", self.f_name)


s1 = student(213311035, "Bottle")
print(s1.id)
print(s1.f_name)
s1.method_1()

# practice qus (make a cons and pass the name of a student and his 3 sub marks and make another method to calculate the average of the marks)


class student:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def func(self):
        return (self.sub1 + self.sub2 + self.sub3) / 3


s1 = student("Leon mask", 5, 5, 5)
print(s1.sub1, s1.sub2, s1.sub3)
print(s1.func())

# practice qus for an account holder for credit and debit his balance using constructor and methods

class account:
    def __init__(self, bal, acc_nm):
        self.balance = bal
        self.account_num = acc_nm

    def credit(self, amount):
        self.balance += amount
        print("your balance is ", self.tot_balance())

    def debit(self, amount):
        self.balance -= amount
        print("your balance is ", self.tot_balance())

    def tot_balance(self):
        return self.balance


cus1 = account(10000, 1234)
cus1.credit(230)
cus1.debit(1000)
