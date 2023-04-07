# class Person:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y

#     def display(self):
#         print(self._x, self._y)

#     @property
#     def value(self):
#         return self._x

#     @value.setter
#     def value(self, val):
#         self._x = val


# p1 = Person(1, 2)
# print(p1.value)


# base code
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         if 20 < age < 80:
#             self._age = age
#         else:
#             raise ValueError("Age must be between 20 and 80")

#     def display(self):
#         print(self.name, self.age)

#     def set_age(self, new_age):
#         if 20 < new_age < 80:
#             self._age = new_age
#         else:
#             raise ValueError("Age must be between 20 and 80")

#     def get_age(self):
#         return self._age


# # client code
# p1 = Person("John", 20)
# p1.set_age(40)
# print(p1.age)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(self.name, self.age)

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, new_age):
#         if 20 < new_age < 80:
#             self._age = new_age
#         else:
#             raise ValueError("Age must be between 20 and 80")


# p1 = Person("John", 25)

# p1.age = 70
# p1.age += 40


# print(p1.age)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def diagonal(self, width, height):
        return (width**2 + height**2) ** 0.5

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height


r1 = Rectangle(10, 20)
print(r1.diagonal, r1.get_area(), r1.get_perimeter())

r1.width = 30
r1.height = 40
print(r1.diagonal, r1.get_area(), r1.get_perimeter())
