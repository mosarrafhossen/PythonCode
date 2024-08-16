class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive!")


class boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Swim!")

class plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly!")
c = car("BMW", "BMW20")
b = boat("Eliza", "Eliza30")
p = plane("Boeing", "747")

for x in (c, b, p):
    x.move()