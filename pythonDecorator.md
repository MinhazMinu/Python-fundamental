-   A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.
-   There are a lots of decorator in python. [Some of theme...](https://github.com/lord63/awesome-python-decorator)
-   Here wil will learn how to use python decorator for using getter and setter method of a class

```py
class Person:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def display(self):
        print(self._x, self._y)

    # we declare method value as property. So we can access value just like a property oof a class. Ex: p1.value
    # this is now working as getter method
    @property
    def value(self):
        return self._x
    # this is now working as a setter method
    @value.setter
    def value(self, val):
        self._x = val


p1 = Person(1, 2)

# getting the value of _x
print(p1.value)
# Output : 1

# set new value of _x
p1.value = 10
print(p1.value)
# Output : 10
```

###### why we will use property?

-   There id no hard and first rule that we should use property.
-   Having said that, property help us to write code in _pythonic_ way. Lets see an example.

-   Let assume we a Person class like this.

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)
```

it takes two perimeters in its constructor method _name_,_age_.

-   Let assume this code has been used in client code just like below.

```py
# client code
p1 = Person("John", 20)
p1.age = 40
```

-   Now the new requirement is that, before set the age, it must validate that if a age is _20 < age < 100_

    One solution could be, we change age as a private variable and use a method to assign the age & before assigning, we validate.

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        # change to a private variable
        self._age = age

    def display(self):
        print(self.name, self.age)

    # validate the new age and set the age
    def set_age(self, new_age):
        if 20 < new_age < 80:
            self._age = new_age
        else:
            raise ValueError("Age must be between 20 and 80")
```

    As age variable is now a private property of a class, Client is not supposed to access it directly.<br>
    so we need to set a getter method also.

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def display(self):
        print(self.name, self.age)

    def set_age(self, new_age):
        if 20 < new_age < 80:
            self._age = new_age
        else:
            raise ValueError("Age must be between 20 and 80")

    def get_age(self):
        return self._age
```

    Now client code can use this *set_age* & *get_age* method to set and get the age property.

```py
p1 = Person("John", 20)
p1.set_age(40)

# or to get the age & increase by 1
p1.set_age(p1.get_age() + 1)
```

Though this code is working, it has two problem.

1. There is no validation during instantiation of the object.

```py
p1 = Person("John", 20)
# this wont provide any error
```

so we need to put the validation code in constructor also.

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        if 20 < age < 80:
            self._age = age
        else:
            raise ValueError("Age must be between 20 and 80")

    def display(self):
        print(self.name, self.age)

    def set_age(self, new_age):
        if 20 < new_age < 80:
            self._age = new_age
        else:
            raise ValueError("Age must be between 20 and 80")

    def get_age(self):
        return self._age
```

2. <span style="color:red">It will break the client Code!!</span> So, this update code is not backward compatible. but why?..
   Remember the client code before ? code was...

```py
p1 = Person("John", 20)
p1.set_age(40)
print(p1.age)
```

This code will generate this error.
<span style="color:red">AttributeError: 'Person' object has no attribute 'age'. Did you mean: '\_age'?</span>
Because we change the age variable to \_age.

###### Using property

-   Now let achieve the new requirement using property.

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if 20 < new_age < 80:
            self._age = new_age
        else:
            raise ValueError("Age must be between 20 and 80")
```

-   Now client code dose not need to change anything, because client code can access age as an property

```py
# get age
print(p1.age)
# set new age with validation
p1.age = 50
# increment age
p1.age += 2
```

-   So, when we need to run data validation of an existing class property we can use _property decorator_.
-   We can also use _property decorator_ to make an instance variable as a read only or write only. Ex: if we remove @age.setter method this age will turn into only read only property.

###### If we change an instance variable, any other variable that is calculated from the instance variable will not changed

-   Below is a rectangular class

```py
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.diagonal = (width ** 2 + height ** 2) ** 0.5

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
```

```py
r1 = Rectangle(10, 20)
print(r1.diagonal, r1.get_area(), r1.get_perimeter())
# Output: 22.360679774997898 200 60
r1.width = 30
r1.height = 40
print(r1.diagonal, r1.get_area(), r1.get_perimeter())
# Output : 22.360679774997898 1200 140
# Here though we change width & height, diagonal did not change because it is calculate from instance variable width & hight.
# are * perimeter is change because it is calculated in a function
```

-   In this type of scenario we can use property decorator.

```py
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
```

This wont brake client code, hance it was backward compatible
