from pet_goods import pet_goods
class pet_cage(pet_goods):
    def __init__(self, name, price, cage_for_kind_animal, size):
        pet_goods.__init__(self, name, price)
        self.cage_for_kind_animal = cage_for_kind_animal
        self.size = size

    def display_cage(self):
        print(self.name, self.price, self.cage_for_kind_animal, self.size)

    def add_cage():
        goods_array=[]
        name=input("Please input name goods: ")
        price=int(input("Please input price goods: "))
        cage_for_kind_animal=input("Please input cage for kind animal: ")
        size=input("Please input size: ")
        goods_array.append(name)
        goods_array.append(price)
        goods_array.append(cage_for_kind_animal)
        goods_array.append(size)
