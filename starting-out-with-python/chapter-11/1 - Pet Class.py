class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

name = input('What is the name of the pet? ')
animal_type = input('What kind of pet is it? ')
age = input('How old is the pet? ')

petobject = Pet(name, animal_type, age)

print("Here is the pet's name:", petobject.get_name())
print("Here is the animal type:", petobject.get_type())
print("Here is the pet's age:", petobject.get_age())
