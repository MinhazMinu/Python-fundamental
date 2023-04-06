<!-- # Python-OOP
## Class: -->

-   To declare class object in python

```py
class Person:
    pass

# to fin id of the class object
print(id(Person()))
# Output : 1783208721472
```

-   We can instantiate a class by calling it with a pair of()

```py
p1 = Person()
p2 = Person()

# to find type of p1 & p2
print(type(p1))
#Output: <class '__main__.Person'>

# to find id / memory location of this two instances
print(id(p1))
print(id(p2))
#Output: 1671974599840
#        1671974599792

# we can see these two are in separate memory location
```

-   To create methods inside class

```py
class Person:
    def display(self):
        print("Hello")
        print(self)

    def greet(self):
        print("Hi, I am a person")

# to call these method we need to instantiate the class first
p1 = Person()
p2 = Person()
# now we can call his method
p1.display()
p2.greet()
# Output: Hello
#         Hi, I am a person
#         <__main__.Person object at 0x000001A08B12AEF0>

# though display method has a perimeter 'self', we do not need to pass it when we call this with instance variable p1 because python automatically send this as an a argument.
# To see what python automatically send in this argument
print(self)
#Output: <__main__.Person object at 0x000001A08B12AEF0>
# Python use this 'self' to identify the the instance object which call this method
```

-   How to add Data in the from of _instance variable_

```py
p1.name = 'Minhaz'
# this name variable is now attached to p1 instance
# this name variable only attached to only p1 instance not p2
# so, if we attached a variable from outside of class, all instance doesn't have same variable.
# to achieve this , we can attached variable from inside of a class

class Person:
    def display(self):
        # we attach name variable using self.
        self.name = "John"
        print(f"Hello {self.name}")


p1 = Person()
p1.display()
print(p1.name)
#Output: Jhon
```

-   Changing one instance variable dose not affect other instance variable

```py
class Person:
    def display(self):
        self.name = "John"


p1 = Person()
p2 = Person()
p1.display()
p2.display()

#changing name variable in p1 instance
p1.name = "Minhaz"


print(p1.name)
# Output : Minhaz
print(p2.name)
# Output : Jhon
# No change in p2 instance
```

-   To set variable in more flexible way, we can pass variable as an argument when we using the method of a class

```py
class Person:
    def display(self, name):
        self.name = name
        print(f"Hello {self.name}")


p1 = Person()
p2 = Person()

p1.display("Minhaz")
p2.display("Jhon")

print(p1.name)
print(p2.name)
# Output: Hello Minhaz
# Hello Jhon
# Minhaz
# Jhon
```
