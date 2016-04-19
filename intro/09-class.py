class Animal(object):
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, kind):
        super(self.__class__, self).__init__(name)
        self.kind = kind

    def bark(self):
        return "Hong hong"


pet = Dog("Pytz", "Shih Tzu")
print pet.name
print pet.kind
print pet.bark()
