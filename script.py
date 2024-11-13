""" Create json file with routes from routes.txt """

import os
import json

current_folder = os.path.dirname(os.path.abspath(__file__))
routes_txt = os.path.join(current_folder, 'routes.txt')
names_fix_txt = os.path.join(current_folder, 'names_fix.txt')
routes_json = os.path.join(current_folder, 'routes.json')
routes_json_keys = os.path.join(current_folder, 'routes_keys.json')

extra_words = [
    'Autobús',
    'Bus + Ferry',
    'Tren',
]


data = {}

# read names fix
with open(names_fix_txt, 'r', encoding='utf-8') as f:
    names_fix = f.readlines()

with open(routes_txt, 'r', encoding='utf-8') as f:
    routes = f.readlines()
    for route in routes:
        
        # Skip empty lines
        if not route.strip():
            continue
        
        # Remove extra words
        for word in extra_words:
            route = route.replace(word, '')
            
        # Get route from and to
        route = route.strip()
        route_from, route_to = route.split(' - ')
        
        # Validate fix names
        for name_fix in names_fix:
            name_fix = name_fix.strip()
            if route_from in name_fix:
                route_from = name_fix
            if route_to in name_fix:
                route_to = name_fix
        
        if route_from not in data:
            data[route_from] = []
            
        # Append route to data
        data[route_from].append(route_to)
        print(route)

# Save data as json
with open(routes_json, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
    
# Save data as json (only keys)
data_keys = list(data.keys())
data_keys.sort()
with open(routes_json_keys, 'w', encoding='utf-8') as f:
    json.dump(data_keys, f, indent=4)
    
print('Data saved as json')