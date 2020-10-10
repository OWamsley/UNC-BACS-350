from .models import Superhero

def add_hero(hero_name, hero_id, hero_info):
    return Superhero.objects.create(name = hero_name, identity =hero_id)

def list_heroes():
    return Superhero.objects.all()

def get_hero(pk):
    return Superhero.objects.get(pk=pk)

def get_identity(id):
    return Superhero.objects.get(identity=id)

def get_hero_name(supername):
    return Superhero.objects.get(name=supername)

def set_hero_id(pk, id):
    w = get_hero(pk)
    w.identity=id
    w.save()
    
def set_hero_name(pk, name):
    w = get_hero(pk)
    w.name=name
    w.save()
    
def delete_hero(pk):
    Superhero.objects.get(pk=pk).delete() 