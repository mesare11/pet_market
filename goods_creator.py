from pet_cats import pet_cats
class goods_creator:
    def input_goods():
        #goods_array=[]
        print("Type of goods: 1 - Cats /n 2- Rodents /n 3 - Cage /n 4 - Feeders /n 5 - Stern /n 6 - Toys")
        new_goods=int(input("Please input type goods: "))
        id_goods=input("Please input id goods: ")
        if new_goods==1:
            pet_cats.add_cat()
        elif new_goods==2:
            pet_cats.add_rodent()
        elif new_goods==3:
            pet_cats.add_cage()
        elif new_goods==4:
            pet_cats.add_feeder()
        elif new_goods==5:
            pet_cats.add_stern()
        elif new_goods==6:
            pet_cats.add_toy()
        else:
            pass
        print(id_goods,goods_array)
            
