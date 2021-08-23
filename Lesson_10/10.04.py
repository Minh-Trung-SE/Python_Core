class Pets:
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

class Dog:
    species = 'mammal'
    is_hungry = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'

    def eat(self):
        self.is_hungry = False

    def walk(self, type = 'walking'):
        return f"{self.name} is {type}"


class RussellTerrier(Dog):
    def run(self,speed):
        return f'{self.name} runs {speed}'
    # def walk(self, type = 'running'):
    #     return f"{self.name} is {type}"

class Bulldog(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'
    # def walk(self, type = 'fly'):
    #     return f"{self.name} is {type}"



if __name__ == '__main__':
    dogs = [
        Dog("Tom", 6),
        Bulldog("Jerry", 9),
        RussellTerrier("Butt", 3)
        ]
    pets = Pets(dogs)
    pets.walk()


