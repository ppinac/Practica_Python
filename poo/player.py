class Player:
    vocation= "no vocation"
    spell = "Puff"
    movement_speed = "50"
    #metodos init
    def __init__(self,**kwargs):
        self.name = input("Elige tu nombre: ")
        self.hit_points = kwargs.get("hit_points", 50)
        self.mana = kwargs.get("mana", 50)
    def __str__(self):
        return "{} es un {} tiene: {} puntos de ataque y {}  puntos de mana, puede lanzar {} y se mueve a una velocida de {} puntos \n".format(
                                                                                                                        self.name,
                                                                                                                        self.vocation,
                                                                                                                        self.hit_points,
                                                                                                                        self.mana,
                                                                                                                        self.cast_spell(),
                                                                                                                        self.movement_speed
                                                                                                                        )

    def cast_spell(self):
        return self.spell

class Sorcerer(Player):
    vocation = "Sorcerer"
    spell= "utevo lux"
    movement_speed = "20"
    def cast_spell(self): #sobre escritura del metodo cast_spell de la clase Player
        return "{} y exura". format(self.spell)
        
class Knight(Player):
    vocation = "knight"
    spell= "exori"
    movement_speed = "60"
    def cast_spell(self):
        return " {} y exura". format(self.spell)

class Paladin(Player):
    vocation = "paladin"
    spell= "exana "
    movement_speed = "80"
class Druid(Player):
    vocation = "druid"
    spell= "exura siu"
    movement_speed = "20"