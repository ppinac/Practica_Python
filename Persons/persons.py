from peewee import *
from datetime import date

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database

def create_family_menbers():
    uncle_tommy= Person(name= "Tommy", birthday=date(2000,11,11), is_relative=True)
    uncle_tommy.save()

    grandma_laura = Person.create(name= "Laura", birthday=date(1864,12,12), is_relative=False)

    tommys_dog = Pet.create(owner=uncle_tommy,name= "Pretty", animal_type= "Dog")
    lauras_cat = Pet.create(owner=grandma_laura,name= "Gato", animal_type= "Cat")

    #actualizando registros
    tommys_dog.name = "Leopoldo"
    tommys_dog.save()

def create_and_conect():
    db.connect()
    db.create_tables([Person, Pet])

def get_family_menbers():
    for person in Person.select():
        print("Nombre: {} Fecha de Nacimiento: {}".format(person.name,person.birthday))

def get_family_menber_birthday(name):
    #family_menber = Person.select().where(Person.name == name).get()
    family_menber = Person.get(Person.name==name)  #forma simple de mostrar un registro
    print("{} Cumple el: {}".format(name,family_menber.birthday))

def delete_pet(name):
    #query = Pet.delete().where(Pet.name == name) borrar varios archivos
    #delete_entries = query.execute()
    query = Pet.get(Pet.name == name)  #borrar solo un archivo
    delete_entries = query.delete_instance()
    print("{} Registros Borrados".format(delete_entries))

def delete_persons(name):
    query = Person.delete().where(Person.name ==name)
    delete_entries= query.execute()
    print("{} Registros borrados".format(delete_entries))

create_and_conect()
#delete_pet("Leopoldo")
delete_persons("Laura")
#get_family_menbers()
#get_family_menber_birthday("Laura")
#create_family_menbers()