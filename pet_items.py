class pet_items(pet_goods):
    def __init__(self, name, price, kind_item, expiration_date):
    pet_goods.__init__(self, name, price)
    self.kind_item = kind_item
    self.expiration_date = expiration_date
    pass
