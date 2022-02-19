from build_chars import *
from pprint import pprint
store_folder = 'store_items'



def pull_store_types(store_folder):
    files = [f for f in listdir(f"./{store_folder}") if isfile(join(f"./{store_folder}", f))]
    stores = []
    for file in files:
        stores.append(file.split('.')[0])
    return stores

store_types = pull_store_types(store_folder)

store_data = {}

for store_type in store_types:
    file_name = f"{store_folder}/{store_type}.yml"
    tmp_name_data = read_in_yaml(file_name)
    store_data[store_type]=tmp_name_data

def build_name(individual_store_data):
    # pprint (individual_store_data)
    first_name = random.choice(individual_store_data['names']['first'])
    second_name = random.choice(individual_store_data['names']['second'])
    name = f"{first_name} {second_name}"
    return name


def build_store(store_type, store_data, rare_item_count):
    tmp_store_data={}
    tmp_store_data['name']=build_name(store_data[store_type])
    tmp_store_data['type']=store_type
    tmp_store_data['common']= store_data[store_type]['common']
    rare_items = {}
    for each in range (1, rare_item_count+1):
        entry_list = list(store_data[store_type]['rare'].items())
        item = random.choice(entry_list)
        rare_items[item[0]]=item[1]
        # rare_item = random.choice(store_data[store_type]['rare'])
    tmp_store_data['rare']= rare_items
    tmp_store_data['person running store']= build_char(races, name_data, background_data, "store_worker")
    return tmp_store_data




# pprint (build_store('combat_store', store_data, 5))
# print ('\n\n\n\n')
# pprint (build_store('general_store', store_data, 5))
# print ('\n\n\n\n')
# pprint (build_store('magic_store', store_data, 5))