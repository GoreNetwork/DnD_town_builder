Town Builder runs mainly on yml files.
For example if you want to add new races just add a new file and base it off one of the existing files **not dward, as dwarf is odd**.  Same for general locations (genernerally service driven locations), or stores.

you build the town with `python build_town.py` 

Inside build_town.py there are town definations, lets look at build_large_town for example

```
def build_large_town():
    stores = {
        'combat_store':5, # Number of combat stores
        'general_store':5,
        'magic_store':3,
    }
    general_locations={
        'bakery':2, # Number of combat bakeries
        'inn':5,
        'temple':4,
        'wizard_services':4,
    }
    rare_items_count=10 # In the stores how many rare items
    extra_chars = 16  # How many extra chars are built out
```
As more locations/stores are added more things will need to be added to the template.  Honestly you probably don't need more than 1 of most of the general_locations (inns are nice to have multiple of)

Currently each store/general location builds with a name, an NPC running the place, services they offer with price.  

Stores can also have rare items

NPCs are generated with a name, race, general background, and something that drivces their char.