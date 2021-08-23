class Dog:
    # =================================Class attribute=============================
    species = 'mammal'
    is_hungry = True
    # =================================Initializer=================================
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # =================================Instance method=============================
    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'

    def eat(self):
        self.is_hungry = False
# =================================Child (inherits from Dog class)=================
class RussellTerrier(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'

class Bulldog(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


# =================================Parent class =====================================
class Pets:
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs


if __name__ == '__main__':
    dogs = [
        Dog("Tom", 6),
        Bulldog("Jerry", 9),
        RussellTerrier("Butt", 3),
        Bulldog("Wine", 1)
    ]
    # Instantiate the Pets class
    check_is_hungry = 0
    pets = Pets(dogs)
    print(f'I have {len(pets.dogs)} dogs.')
    for dog in pets.dogs:
        print(f'{dog.name} is {dog.age}')
        if dog.is_hungry:
            check_is_hungry += 1
    print(f'And they\'re all {dog.species}s, of course.')
    if check_is_hungry == len(pets.dogs):
        print(f"My dogs are hungry")
    elif check_is_hungry == 0:
        print(f"My dogs are not hungry")
    else:
        print(f"Exception!")









