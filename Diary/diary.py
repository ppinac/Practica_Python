from peewee import *
import datetime
import sys
from collections import OrderedDict





db= SqliteDatabase("diary.db")


class Entry(Model):
    #contenido
    #timestamp
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database= db

def create_and_connect():
    """Connect to the database"""
    db.connect()
    db.create_tables([Entry],safe=True)

def menu_loop():
    """ Show menu """
    choice =None
    while choice != 'q':
        print("press 'q' to quit")
        for key,value in menu.items():
            print("{}) {}".format(key,value.__doc__))
        choice = input("Action: ").lower().strip()
        if choice in menu:
            menu[choice]()


def add_entry():
    """Adds Entry"""
    print("Enter your thoughts. Press ctr + D to finish")
    data = sys.stdin.read().strip()
    
    if data:
        if input("Do you want to save entry? [Y/N]").lower().strip() != 'n':
           Entry.create(content=data)
           print("your entry was saved successfully ")

def view_entry(search_query=None):
    """View all entries"""
    entries =Entry.select().order_by(Entry.timestamp.desc())

    if search_query:
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp= entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        print('\n')
        print(timestamp)
        print('-'*len(timestamp))
        print(entry.content)
        print('\n')
        print('-'*len(entry.content))
        print('n) next entry')
        print('e) edit entry')
        print('d) delete entry')
        print('q) return to menu')

        next_action= input("Action: ").lower().strip()
        if next_action == 'q':
            break
        elif next_action =='e':
            edit_entry()
        elif next_action == 'd':
            delete_entry(entry)
def edit_entry():
    """Edit Entries"""
    entradas = sys.stdin.read().strip()
    Entry.content = entradas
    entradas.save()
def search_entries():
    """Search Entries"""
    search_query= input("Search query: ").strip()
    view_entry(search_query)

def delete_entry(entry):
    """Delete entries"""
    action= input("are you sure? [Y/N]: ").lower().strip()
    if action == 'y':
        entry.delete_instance()


menu= OrderedDict([
                    ('a',add_entry),
                    ('v',view_entry),
                    ('s',search_entries),
                    ('d',delete_entry)
                   ])


if __name__ == '__main__': # se usa para cuando pones from diary import solo importe las funciones
    create_and_connect()
    menu_loop()
