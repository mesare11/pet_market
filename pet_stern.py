from pet_goods import pet_goods
class pet_stern(pet_goods):
    def __init__(self, name, price, stern_for_kind_animal, weight):
        pet_goods.__init__(self, name, price)
        self.stern_for_kind_animal = stern_for_kind_animal
        self.weight = weight

    def display_stern(self):
        print(self.name, self.price, self.stern_for_kind_animal, self.weight)
