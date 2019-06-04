import player
import troll


#instancias u objetos
sorcerer = player.Sorcerer(hit_points=40,mana=80)
knight =player.Knight(hit_points=80,mana=20)
paladin = player.Paladin(hit_points=60,mana=40)
druid = player.Druid(hit_points=70,mana=80)

frost = troll.Frost(hit_points =55, mana=300)
island= troll.Island(hit_points=50, mana=290)
swamp = troll.Swamp(hit_points=55,mana=320)
champions = troll.Champions(hit_points=75,mana=350)

print(sorcerer)
print(knight)
print(paladin)
print(druid)

print("--------------------Troll----------------------")
print(frost)
print(island)
print(swamp)
print(champions)


