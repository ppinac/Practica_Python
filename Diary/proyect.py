#listar entradas por bloques de paginacion
#borrar entrada de diario
#buscar entrada por fecha
#opcion para editar entrada
#registrar entrada de diario
from peewee import *
from collections  import OrderedDict
import datetime
import sys
db =SqliteDatabase("diario.db")

#Database
class Entry(Model):
    timestamp = TimestampField(default=datetime.datetime.now())
    content = TextField()
    class Meta:
        database = db
#fin Database


def add_entry():
    """Add New Entry"""
    print("Entry your thought")
    print("Press Ctrl + D to finish")
    data = sys.stdin.read().strip()
    if data:
        if input("do you want to save? [Y/N]").lower().strip() != 'n':
            Entry.create(content=data)
            print("Your entry save successfull!")

def edit_entry():
    """"Edit Entry"""

def search_entry():
    """Search Entry"""
    search_query =input("ingrese dato de busqueda: ").strip()
    list_entry(search_query)

def list_entry(search_query=None):
    """List Entry"""
    entries = Entry.select().order_by(Entry.timestamp.desc())
        
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp= entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        print(timestamp)
        print('-'*len(timestamp))
        print(entry.content)
        print('+'*len(entry.content))
        print('\n')

def delete_entry():
    """Delete Entry"""

def create_and_connect():
    db.connect()
    db.create_tables([Entry],safe=True)


#menu to the diary

def menu_loop():
    """show Menu"""
    choice = None
    while choice != 'q':
        print("-"*8)
        print("Press 'q' to quit")
        for key,value in menu.items():
            print("{}) {}".format(key,value.__doc__))
        choice = input("Action: ").lower().strip()
        if choice in menu:
            menu[choice]()

menu = OrderedDict([
                    ("a",add_entry),
                    ("l",list_entry),
                    ("d",delete_entry),
                    ("s",search_entry)
                    ])
#Fin menu to diary
create_and_connect()
menu_loop()
