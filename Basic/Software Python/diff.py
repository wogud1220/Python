class Animal:
    def __init__(self, name):
        self.name = name
        print(self.name, "has heart")
    def live(self):
        print(self.name, "is alive")
class Mamal:
    def __init__(self, name):
        self.name = name
        print(self.name, "has spine")
    def live(self):
        print(self.name, "can move")
class Dog:
    def __init__(self, name):
        self.name = name
        print(self.name, "has fur")
    def live(self):
        print(self.name, "can bark")


dog = Dog("pydog")
mamal = Mamal("pydog")
animal = Animal("pydog")
animal.live()
mamal.live()
dog.live()
###aaaaa




