class Grandparend:
    height = 170
    eyes = "green"
    age = 63
class Parent(Grandparend):
    age = 39

class Child(Parent):
    age = 12
    height = 165
    def __init__(self):
        print(self.height)
        print(self.eyes)
        print(self.age)

max = Child()

class Human:
    height = 170

class Student(Human):
    pass

class Worker(Human):
    pass

nick = Student()
kate = Worker()
print(nick.height, kate.height)

class Hello:
    def __init__(self):
        print("Hello")
class Hello_world(Hello):
    def __init__(self):
        super().__init__()
        print("World")

obj = Hello_world()
