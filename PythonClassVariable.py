# class Person:
#     species = "Homo sapiens"
#     count = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Person.count += 1

#     def display(self):
#         print(f"{self.name} & {self.age}")


# p1 = Person("jhon", 20)
# p2 = Person("jhon", 20)


# print(f"Total instance {Person.count}")


# class BankAccount:
#     rate_of_interest = 5
#     minimum_balance = 100
#     minimum_balance_fees = 10

#     def __init__(self, account_number, owner_name, balance):
#         self.account_number = account_number
#         self.owner_name = owner_name
#         self.balance = balance

#     def withdraw(self, amount):
#         self.balance -= amount

#     def deposit(self, amount):
#         self.balance += amount


# acc1 = BankAccount("1234", "minu", 10000)
# acc2 = BankAccount("4567", "minhaz", 20000)


# class Book:
#     x = 5

#     def __init__(self):
#         self.x = 100


# b = Book()

# print(b.x)
# print(Book.x)


# class Account:
#     rate = 5


# a1 = Account()
# a2 = Account()

# Account.rate = 10

# print(Account.rate)
# print(a1.rate)


class Account:
    rate = 5


a1 = Account()
a2 = Account()

a1.rate = 10

print(Account.rate)
print(a1.rate)
print(a2.rate)
