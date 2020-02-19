from pet_goods import pet_goods
from pet_animals import pet_animals
class pet_cats(pet_animals):
    def __init__(self, name, price, kind_pet, age, cats_breed):
        pet_animals.__init__(self, name, price, kind_pet, age)
        self.cats_breed = cats_breed

    def display_cats(self):
        print(self.name, self.price, self.kind_pet, self.age, self.cats_breed)
