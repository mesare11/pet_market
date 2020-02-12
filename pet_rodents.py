class pet_rodents(pet_animals):
    def __init__(self, name, price, kind_pet, age, rodent_breed):
    pet_goods.__init__(self, name, price)
    pet_animals.__init__(self, kind_pet, age)
    self.rodent_breed = rodent_breed
