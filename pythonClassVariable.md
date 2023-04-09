#### Python Class variable

-   Python variables which are define inside the class but outside of the method are _class variable_.
-   Class variable are shared by all the instance of the class, its belongs to the class.

```py
class Person:
    # Class variable
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} & {self.age}")

```

-   Class variable can be accessed by _class_ name or by instance object. But it is a hard convention to access class variable by _class name_

```py
class Person:
    # Class variable
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} & {self.age}")


p1 = Person("jhon", 20)
# Class variable *species* is accessed by instance variable.
print(p1.species) # Output : Homo sapiens
# Class variable *species* is accessed by Class Name.
print(Person.species) # Output : Homo sapiens
```

-   If there is a same class variable as _instance variable_, _instance variable_ hides the _class variable_ when access by _instance variable_

```py
class Book:
    # class variable x
    x = 5

    def __init__(self):
        # instance variable x
        self.x = 100


b = Book()

print(b.x) # Output : 100
print(Book.x) #output : 5
```

so , when we access a variable by instance, python first checks weather the instance contains that variable, if its contains then use that, otherwise it looks in class variable with same name.

-   Example : Use class variable to count how many instance a class have.

```py
class Person:
    species = "Homo sapiens"
    # declare a class variable count and set to 0
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # increment count every time an instance is created
        Person.count += 1

    def display(self):
        print(f"{self.name} & {self.age}")


p1 = Person("jhon", 20)
p2 = Person("jhon", 20)
# two instance have been created

print(f"Total instance {Person.count}")
# Output : Total instance 2
```

-   So, if you have some information that is applicable to a class, not to instance variable - thant we should declare that information as a class variable

*   Another Example: Lets say we have a BankAccount class. Every bank account have some information
    -   rate_of_interest
    -   minimum_balance
    -   minimum_balance_fees

this information's are same for all the instance, so we should declare all these as class variable.

```py
class BankAccount:
    rate_of_interest = 5
    minimum_balance = 100
    minimum_balance_fees = 10

    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


acc1 = BankAccount("1234", "minu", 10000)
acc2 = BankAccount("4567", "minhaz", 20000)
```

-   we see we can access a _class variable_ by class name & by instance variable. But if we change a class variable by instance we will find some unexpected behaver
    -   change by class name

```py
class Account:
    # class variable
    rate = 5

a1 = Account()
a2 = Account()

# change class variable by class name
Account.rate = 10

print(Account.rate) # output : 10
print(a1.rate)      # output : 10
print(a2.rate)      # output : 10

# so, changing by class name also change the value if instance variable
```

    - Change by instance variable

```py
class Account:
    rate = 5


a1 = Account()
a2 = Account()

a1.rate = 10

print(Account.rate) # output : 5
print(a1.rate)      # output : 10
print(a2.rate)      # output : 5

# so changing by instance variable only change the value for that instance
```
