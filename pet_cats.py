from pet_goods import pet_goods
from pet_animals import pet_animals
class pet_cats(pet_animals):
    def __init__(self, name, price, kind_pet, age, cats_breed):
        pet_animals.__init__(self, name, price, kind_pet, age)
        self.cats_breed = cats_breed

    def display_cats(self):
        print(self.name, self.price, self.kind_pet, self.age, self.cats_breed)

    def add_cat():
        goods_array=[]
        name=input("Please input name goods: ")
        price=int(input("Please input price goods: "))
        kind_pet=input("Please input kind of pet: ")
        age=input("Please input age pet: ")
        cats_breed=input("Please input cats breed: ")
        goods_array.append(name)
        goods_array.append(price)
        goods_array.append(kind_pet)
        goods_array.append(age)
        goods_array.append(cats_breed)
