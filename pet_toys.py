from pet_goods import pet_goods
from pet_items import pet_items
class pet_toys(pet_items):
    def __init__(self, name, price, kind_item, expiration_date, toy_for_kind_animal, kind_of_toy):
        pet_items.__init__(self, name, price, kind_item, expiration_date)
        self.toy_for_kind_animal = toy_for_kind_animal
        self.kind_of_toy = kind_of_toy

    def display_toys(self):
        print(self.name, self.price, self.kind_item, self.expiration_date, self.toy_for_kind_animal, self.kind_of_toy)

    def add_toy():
        goods_array=[]
        name=input("Please input name goods: ")
        price=int(input("Please input price goods: "))
        kind_item=input("Please input kind item: ")
        expiration_date=input("Please input expiration date: ")
        toy_for_kind_animal=input("Please input toy for kind animal: ")
        kind_of_toy=input("Please input kind of toy: ")
        goods_array.append(name)
        goods_array.append(price)
        goods_array.append(kind_item)
        goods_array.append(expiration_date)
        goods_array.append(toy_for_kind_animal)
        goods_array.append(kind_of_toy)
