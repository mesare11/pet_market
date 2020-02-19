from pet_goods import pet_goods
from pet_animals import pet_animals
class pet_rodents(pet_animals):
    def __init__(self, name, price, kind_pet, age, rodent_breed):
        pet_animals.__init__(self, name, price, kind_pet, age)
        self.rodent_breed = rodent_breed

    def display_rodents(self):
        print(self.name, self.price, self.kind_pet, self.age, self.rodent_breed)
