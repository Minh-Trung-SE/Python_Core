class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


def get_biggest_number(*args):
    oldest_age = max(Dog.age for Dog in list_dog)
    print(f"The oldest dog is {oldest_age} years old")


list_dog = [Dog('Fake', 2),
            Dog('Mickey', 7),
            Dog('Fuk', 5)]

get_biggest_number(*(dog for dog in list_dog))
