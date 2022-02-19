import yaml
from pprint import pprint
import random 
from os import listdir
from os.path import isfile, join



name_folder = 'names'
backgrounds_folder = "backgrounds"


def pull_races(name_folder):
    files = [f for f in listdir(f"./{name_folder}") if isfile(join(f"./{name_folder}", f))]
    races = []
    for file in files:
        races.append(file.split('.')[0])
    return races

races = pull_races(name_folder)

def read_in_yaml(file):
    with open(file, 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    return data_loaded

def build_dwarf_name(dwarf_name_data):
    sex = random.choice(['male', 'female'])
    first_name = random.choice(dwarf_name_data['first'][sex])
    last_name_first_part=random.choice(dwarf_name_data['last']['adgitive'])
    last_name_second_part=random.choice(dwarf_name_data['last']['noun'])
    name = f"{first_name} {last_name_first_part}{last_name_second_part}"
    data = [sex, name]
    return data

def name_builder(name_data):
    sex = random.choice(['male', 'female'])
    first_name = random.choice(name_data['first'][sex])
    last_name=random.choice(name_data['last'])
    name = f"{first_name} {last_name}"
    data = [sex, name] 
    return data   

def run_name_builder(race, name_data ):
    if race == "dwarf":
        return build_dwarf_name(name_data[race])
    else:
        return name_builder(name_data[race])

name_data = {}

for race in races:
    file_name = f"{name_folder}/{race}.yml"
    tmp_name_data = read_in_yaml(file_name)
    name_data[race]=tmp_name_data

background_data = read_in_yaml(f"{backgrounds_folder}/backgrounds.yml")

def build_char(races, name_data, background_data, profession):
    char_data = {}
    char_data['race'] = random.choice(races)
    tmp_data = run_name_builder(char_data['race'], name_data )
    char_data['sex']=tmp_data[0]
    char_data['name']=tmp_data[1]
    # pprint (background_data)
    char_data['background'] = random.choice(background_data[profession])
    char_data['flaw']=random.choice(background_data['flaws'])
    return char_data

# pprint (build_char(races, name_data, background_data, "store_worker")      )


