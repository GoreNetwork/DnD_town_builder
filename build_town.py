# from numpy import inner
from build_chars import *
from build_general_places import *
from build_stores import *
from pprint import pprint

def build_small_town():
    stores = {
        'combat_store':1,
        'general_store':1,
        'magic_store':0,
    }
    general_locations={
        'bakery':1,
        'inn':2,
        'temple':1,
        'wizard_services':0,
    }
    rare_items_count=1
    extra_chars = 5
    return build_town(extra_chars, stores, general_locations, rare_items_count)
def build_medium_town():
    stores = {
        'combat_store':2,
        'general_store':2,
        'magic_store':1,
    }
    general_locations={
        'bakery':2,
        'inn':3,
        'temple':2,
        'wizard_services':1,
    }
    rare_items_count=5
    extra_chars = 9
    return build_town(extra_chars, stores, general_locations, rare_items_count)
def build_large_town():
    stores = {
        'combat_store':5,
        'general_store':5,
        'magic_store':3,
    }
    general_locations={
        'bakery':2,
        'inn':5,
        'temple':4,
        'wizard_services':4,
    }
    rare_items_count=10
    extra_chars = 16
    return build_town(extra_chars, stores, general_locations, rare_items_count)





def build_town(extra_chars, stores, general_locations, rare_items_count):
    output = {} 
    output['stores']=[]
    output['general_locations']=[]
    output['extra_chars']=[]
    town_data_file  = "town_data/town_name_data.yml"
    town_data = read_in_yaml(town_data_file)
    output['town_name']= build_name(town_data)
    for store in stores:
        for each_store in range(0,stores[store]):
            output['stores'].append(build_store(store, store_data, rare_items_count ))
    for general_location in general_locations:
        for each in range(0,general_locations[general_location]):
            output['general_locations'].append(build_location(general_location, location_data))
    for each in range(0,extra_chars):
        output['extra_chars'].append(build_char(races, name_data, background_data, "extra_chars"))
    return output
    
pprint (build_large_town())