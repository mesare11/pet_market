class pet_animals(pet_goods):
    def __init__(self, name, price, kind_pet, age):
    pet_goods.__init__(self, name, price)
    self.kind_pet = kind_pet
    self.age = age
