from build_chars import *
from pprint import pprint
locations_folder = 'general_locations'
from build_stores import build_name



def pull_types(folder):
    files = [f for f in listdir(f"./{folder}") if isfile(join(f"./{folder}", f))]
    types = []
    for file in files:
        types.append(file.split('.')[0])
    return types

def build_types(folder, types):
    data = {}
    for type in types:
        file_name = f"{folder}/{type}.yml"
        tmp_name_data = read_in_yaml(file_name)
        data[type]=tmp_name_data
    return data

types = pull_types(locations_folder)
location_data = build_types(locations_folder, types)

def build_location(location_type, location_data):
    tmp_location = {}
    tmp_location['name'] =build_name(location_data[location_type])
    tmp_location['type']= location_type
    tmp_location['person running store']= build_char(races, name_data, background_data, "store_worker")
    tmp_location['services']={}
    for service in location_data[location_type]['services']:
        low, high = location_data[location_type]['services'][service]
        high = high+1
        price = str(random.choice(range(low, high)))+" sp"
        tmp_location['services'][service]= price
    return tmp_location

# pprint (build_location('inn', location_data))
# pprint (build_location('temple', location_data))
# pprint (build_location('wizard_services', location_data))
# pprint (build_location('bakery', location_data))