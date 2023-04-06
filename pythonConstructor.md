-   '\__init _\_' method in python is a magic method which automatically called when a python class has been instantiate
-   A class could have only

```py
class Person:
    def __init__(self):
        print("Constructor called")


p1 = Person()
# Output : Constructor called

# So if we nned any code that should be executed just after the object creation, we can write in __init__ method
```

-   Set _instance variable_ using constructor

```py
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Hello {self.name}")


p1 = Person("Minhaz")
# Output: Hello Minhaz
# we pass the value of 'name' as an argument when object is initialized
```
