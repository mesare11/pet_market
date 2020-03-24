from pet_goods import pet_goods
from pet_animals import pet_animals
from pet_items import pet_items
from pet_cage import pet_cage
from pet_cats import pet_cats
from pet_feeders import pet_feeders
from pet_rodents import pet_rodents
from pet_stern import pet_stern
from pet_toys import pet_toys
from goods_creator import goods_creator
from array import array
def sum_goods(all_goods:array) ->None:
    """
    This function sums all goods from array
    param all_goods array of ints of goods
    """
    numberObject=-1
    lenArray=len(all_goods)-1
    prices=[]
    while (lenArray>numberObject):
        numberObject=numberObject+1
        prices.append(all_goods[numberObject].display_prices())
    summa=sum(prices)
    print("The total value of all goods "+format(summa)+"$")
    
cat1=pet_cats("Tom", 20, "Cat", "3 month", "Siamese")
cat2=pet_cats("Joe", 15, "Cat", "4 month", "Scottish fold")
cat3=pet_cats("Jim", 20, "Cat", "3 month", "Siamese")
cat4=pet_cats("Fiona", 25, "Cat", "4 month", "Scottish fold")
cat5=pet_cats("Jeremy", 30, "Cat", "2 month", "British cat")
rat1=pet_rodents("Sam", 2, "Rodent", "1 month", "White rat")
rat2=pet_rodents("Chloe", 3, "Rodent", "2 month", "White rat")
rat3=pet_rodents("Pit", 3, "Rodent", "2 month", "Black rat")
hamster1=pet_rodents("Ti", 5, "Rodent", "1 month", "Decorative hamster")
hamster2=pet_rodents("Li", 5, "Rodent", "1 month", "Decorative hamster")
cage1=pet_cage("Rodenta", 14, "For Rodents", "25x25x50")
cage2=pet_cage("Rodenta", 19, "For Rodents", "40x40x50")
cage3=pet_cage("Rodenta", 25, "For Rodents", "70x70x70")
cage4=pet_cage("Vendy", 55, "For Birds", "70x55x150")
cage5=pet_cage("Vendy", 70, "For Cats", "100x700x80")
stern1=pet_stern("Vendy", 5, "For Cats", 5)
stern2=pet_stern("Vendy", 10, "For Cats", 9)
stern3=pet_stern("Rodenta", 4, "For Cats", 5)
stern4=pet_stern("Rodenta", 1, "For Rodents", 1)
stern5=pet_stern("Vendy", 2, "For Rodents", 1)
toy1=pet_toys("Rodenta", 10, "For play", "5 years", "For Cats", "Ball")
toy2=pet_toys("Vendy", 15, "For play", "6 years", "For Cats", "Ball")
toy3=pet_toys("Vendy", 20, "For Run", "3 years", "For Rodents", "Hamster wheel")
toy4=pet_toys("Rodenta", 22, "For Run", "4 years", "For Rodents", "Hamster wheel")
toy5=pet_toys("Rodenta", 10, "For Claw", "1 year", "For Cats", "claw-point")
feeder1=pet_feeders("Vendy", 2, "For eat", "2 years", "For Cats", "20x20x20")
feeder2=pet_feeders("Vendy", 2, "For water", "2 years", "For Cats", "20x20x20")
feeder3=pet_feeders("Rodenta", 3, "For water", "3 years", "For Cats", "25x25x25")
feeder4=pet_feeders("Rodenta", 3, "For eat", "3 years", "For Cats", "25x25x25")
feeder5=pet_feeders("Rodenta", 1, "For eat", "1 year", "For Rodents", "5x5x5")

all_goods=[cat1,cat2,cat3,cat4,cat5,rat1,rat2,rat3,hamster1,hamster2,cage1,cage2,cage3,cage4,cage5,stern1,stern2,stern3,stern4,stern5,toy1,toy2,toy3,toy4,toy5,feeder1,feeder2,feeder3,feeder4,feeder5]
sum_goods(all_goods)   


goods_creator.input_goods()

toy1.display_toys(),toy2.display_toys(),toy3.display_toys(),toy4.display_toys(),toy5.display_toys()
stern1.display_stern(),stern2.display_stern(),stern3.display_stern(),stern4.display_stern(),stern5.display_stern()
rat1.display_rodents(), rat2.display_rodents(),rat3.display_rodents(), hamster1.display_rodents(), hamster2.display_rodents()
feeder1.display_feeders(), feeder2.display_feeders(), feeder3.display_feeders(), feeder4.display_feeders(), feeder5.display_feeders()  
cat1.display_cats(),cat2.display_cats(),cat3.display_cats(),cat4.display_cats(),cat5.display_cats()
cage1.display_cage(),cage2.display_cage(),cage3.display_cage(),cage4.display_cage(),cage5.display_cage()
