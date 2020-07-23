from pet_goods import pet_goods
from pet_animals import pet_animals
class pet_rodents(pet_animals):
    def __init__(self, name, price, kind_pet, age, rodent_breed):
        pet_animals.__init__(self, name, price, kind_pet, age)
        self.rodent_breed = rodent_breed

    def display_rodents(self):
        print(self.name, self.price, self.kind_pet, self.age, self.rodent_breed)

    def add_rodent():
        goods_array=[]
        name=input("Please input name goods: ")
        price=int(input("Please input price goods: "))
        kind_pet=input("Please input kind of pet: ")
        age=input("Please input age pet: ")
        rodent_breed=input("Please input rodent breed: ")
        goods_array.append(name)
        goods_array.append(price)
        goods_array.append(kind_pet)
        goods_array.append(age)
        goods_array.append(rodent_breed)
