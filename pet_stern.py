from pet_goods import pet_goods
class pet_stern(pet_goods):
    def __init__(self, name, price, stern_for_kind_animal, weight):
        pet_goods.__init__(self, name, price)
        self.stern_for_kind_animal = stern_for_kind_animal
        self.weight = weight

    def display_stern(self):
        print(self.name, self.price, self.stern_for_kind_animal, self.weight)

    def add_stern():
        goods_array=[]
        name=input("Please input name goods: ")
        price=int(input("Please input price goods: "))
        stern_for_kind_animal=input("Please input stern for kind animal: ")
        weight=input("Please input weight: ")
        goods_array.append(name)
        goods_array.append(price)
        goods_array.append(stern_for_kind_animal)
        goods_array.append(weight)
