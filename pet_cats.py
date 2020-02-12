class pet_cats(pet_animals):
    def __init__(self, name, price, kind_pet, age, cats_breed):
    pet_goods.__init__(self, name, price)
    pet_animals.__init__(self, kind_pet, age)
    self.cats_breed = cats_breed
