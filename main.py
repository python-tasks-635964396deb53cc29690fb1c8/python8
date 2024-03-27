from overpy import Overpass

api = Overpass()

result = api.parse_xml(open('12.osm', 'r').read())

groups_opening_hours = {}

for node in result.nodes:
    if 'amenity' in node.tags and node.tags['amenity'] == 'restaurant':
        opening_hours = node.tags['opening_hours'] if 'opening_hours' in node.tags else '«Не задано»'
        name = node.tags['name'] if 'name' in node.tags else '«Нет названия»'
        if opening_hours in groups_opening_hours:
            groups_opening_hours[opening_hours].append((name, node.lat, node.lon))
        else:
            groups_opening_hours[opening_hours] = [(name, node.lat, node.lon)]

for time, attrs in groups_opening_hours.items():
    print(f'Время работы {time}:')
    for attr in attrs:
        print(f'\t{attr[0]} [{attr[1]}; {attr[2]}]')
    print()
