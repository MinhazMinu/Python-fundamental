###### Python class method

-   until now we only learn about instance method. Instance method always have a perimeter _self_. There are other two method

    -   class method
    -   static method

-   Class method is a method that are associated with the class it self. Not with any particular instance of the class.

-   To make a class method wee need to add _@classmethod_ before the method. _@classmethod_ is function decorator

*   Like instance method, class method also have a special perimeter. By strong convention it is _cls_

```py
class MyClass:
    a = 5

    def __init__(self, x):
        self.x = x

    def method1(self):
        print(self.x)

    @classmethod
    def method2(cls):
        print(cls.a)
```

-   Class method can be invoked by class name or by instance variable. But strong convention is to invoked by class name

```py
class MyClass:
    a = 5

    def __init__(self, x):
        self.x = x

    def method1(self):
        print(self.x)

    @classmethod
    def method2(cls):
        print(cls.a)

# we are not create any instance till now, but still we can call class method.
MyClass.method2() # Output : 5

# now we are creating an instance
m1 = MyClass(10)
# and call the class method
m1.method2()      # Output : 5

```

-   A class method can only work with a class variable. it can not work with instance variable as it dose not have _self_

*   So, when we have to process some information that is associated with class it self, not with any instance object, then we will turn out method into a class method by writing the _@classmethod_ decorator & specifying the _cls_ as the first perimeter.

*   The most common use of a class method is defining the factory method.
    For example, there might be a need to create Person instance from different type of data
    Let assume we need to create two type of person object from a string and another is from dictionary.

```py
temp_string = "user","age"
temp_dict = {"name": "john", "age":35}
```

-   As python dose not support method overloading, so there can be one type of initializer

```py
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


s = "user,23"
d = {"name": "john", "age": 35}

p3 = Person.from_str(s)
p4 = Person.from_dict(d)

p3.display()
p4.display()
```

-   Now create a Person object From an Employee object

```py
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
```

now lets create an person object from this employee object

```py
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
```
