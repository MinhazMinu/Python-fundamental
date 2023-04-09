###### Static method

-   Static method dose not have any special perimeter
-   Static method can not access class variable & and class variable
-   when we need to create some utility function or helper method that constrains some login related to the class
    turn it intu static method

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

    @staticmethod
    def method3(m, n):
        return m + n
```
