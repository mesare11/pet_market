from pet_goods import pet_goods
from pet_items import pet_items
class pet_feeders(pet_items):
    def __init__(self, name, price, kind_item, expiration_date, feeder_for_kind_animal, feeder_size):
        pet_items.__init__(self, name, price, kind_item, expiration_date)
        self.feeder_for_kind_animal = feeder_for_kind_animal
        self.feeder_size = feeder_size

    def display_feeders(self):
        print(self.name, self.price, self.kind_item, self.expiration_date, self.feeder_for_kind_animal, self.feeder_size)

    def add_feeder():
        goods_array=[]
        name=input("Please input name goods: ")
        price=int(input("Please input price goods: "))
        kind_item=input("Please input kind item: ")
        expiration_date=input("Please input expiration date: ")
        feeder_for_kind_animal=input("Please input feeder for kind animal: ")
        feeder_size=input("Please input feeder size: ")
        goods_array.append(name)
        goods_array.append(price)
        goods_array.append(kind_item)
        goods_array.append(expiration_date)
        goods_array.append(feeder_for_kind_animal)
        goods_array.append(feeder_size)
