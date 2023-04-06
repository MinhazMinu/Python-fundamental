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
