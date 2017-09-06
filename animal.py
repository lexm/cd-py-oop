class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "Health is:", self.health
        return self

bear1 = Animal("Bear",270)
bear1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)
    def pet(self):
        self.health += 5
        return self

fido = Dog("Fido")
fido.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon."
        return self

animal2 = Animal("Freddie", 137)
#animal2.pet()
#animal2.fly()
animal2.display_health()

spot = Dog("Fido")
#spot.fly()
dragon1 = Dragon("Viserion")
dragon1.fly().display_health()
