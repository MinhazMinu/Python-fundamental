# class MyClass:
#     a = 5

#     def __init__(self, x):
#         self.x = x

#     def method1(self):
#         print(self.x)

#     @classmethod
#     def method2(cls):
#         print(cls.a)


# m1 = MyClass(10)

# m1.method2()
# MyClass.method2()


# class Person:
#     species = "Homo sapiens"
#     count = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Person.count += 1

#     def display(self):
#         print(f"{self.name} & {self.age}")

#     @classmethod
#     def show_count(cls):
#         print(f"there are {cls.count} {cls.species}")


# Person.show_count()

# p1 = Person("john", 20)
# p2 = Person("Jack", 34)
# Person.show_count()
# p1.show_count()

from datetime import datetime


class Employee:
    def __init__(self, first_name, last_name, birth_year, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.salary = salary

    def show(self):
        print(
            f" i am {self.first_name} {self.last_name} \
            born in {self.birth_year}"
        )


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} & {self.age}")

    @classmethod
    def from_str(cls, s):
        name, age = s.split(",")
        return cls(name, int(age))

    @classmethod
    def from_dict(cls, d):
        name = d["name"]
        age = d["age"]
        return cls(name, int(age))

    @classmethod
    def from_employee(cls, emp):
        name = emp.first_name + " " + emp.last_name
        age = datetime.today().year - emp.birth_year
        return cls(name, age)


s = "user,23"
d = {"name": "john", "age": 35}

p3 = Person.from_str(s)
p4 = Person.from_dict(d)

p3.display()
p4.display()

e1 = Employee("john", "doe", 1990, 50000)
p5 = Person.from_employee(e1)

p5.display()
