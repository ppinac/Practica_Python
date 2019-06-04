class Troll:
    vocation = "Troll"
    exp = 0
    items = " meat "

    def __init__(self,**kwargs):
        self.hit_points = kwargs.get("hit_points", 50)
        self.mana= kwargs.get("mana", 290)
    
    def __str__(self):
        return "El {} troll tiene {} puntos de ataque y {} mana, al matarlo nos da {} de experiencia y dropea {}\n ".format(
                                                                                                                            self.vocation,
                                                                                                                            self.hit_points,
                                                                                                                            self.mana,
                                                                                                                            self.exp,
                                                                                                                            self.drop_items())
        
    def drop_items (self):
        return self.items
class Frost(Troll):
    vocation = "Frost"
    exp = 23
    items ="spears"
    
    def drop_items(self):
        return "{} con otros articulos".format(self.items)
    
class Island (Troll):
    vocation = "Island"
    exp = 20
    items = "wood"
    def drop_items(self):
        return "{} con otros articulos".format(self.items)

class Swamp(Troll):
    vocation ="Swamp"
    exp = 25
    items = "fish"
    def drop_items(self):
        return "{} con otros articulos".format(self.items)

class Champions(Troll):
    vocation ="Champions"
    exp = 40
    items ="gold coins"
    def drop_items(self):
        return "{} con otros articulos".format(self.items)