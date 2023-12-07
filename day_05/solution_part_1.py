# solution to Advent of Code day 5 part 1

import pprint

def find_lowest_location_number(buffer):

    map_dict, seed_location_dict = parse(buffer)
    seed_location_dict = find_soil_type(map_dict, seed_location_dict)
    seed_list = [seed for seed in seed_location_dict]
    seed_location_dict = find_fertilizer_type(seed_list, map_dict, seed_location_dict)
    seed_location_dict = find_water_type(seed_list, map_dict, seed_location_dict)
    seed_location_dict = find_light_type(seed_list, map_dict, seed_location_dict)
    seed_location_dict = find_temp_type(seed_list, map_dict, seed_location_dict)
    seed_location_dict = find_humidity_type(seed_list, map_dict, seed_location_dict)
    seed_location_dict = find_location(seed_list, map_dict, seed_location_dict)

    return min([dictionary['humidity-to-location map'] for dictionary in seed_location_dict.values()])
        

# find the location for each seed
def find_soil_type(map_dict, seed_location_dict):

    for seed in seed_location_dict:
            for soil_type in map_dict["seed-to-soil map"]:
                if int(soil_type[1]) <= int(seed) < int(soil_type[1]) + int(soil_type[2]):
                    seed_location_dict[seed]["seed-to-soil map"] = int(seed) + int(soil_type[0]) - int(soil_type[1])
            if "seed-to-soil map" not in seed_location_dict[seed]:
                seed_location_dict[seed]["seed-to-soil map"] = int(seed)
    
    return seed_location_dict


# find the fertilizer for each seed
def find_fertilizer_type(seed_list, map_dict, seed_location_dict):

    for seed in seed_list:
        for fertilizer_type in map_dict["soil-to-fertilizer map"]:
            if int(fertilizer_type[1]) <= int(seed_location_dict[seed]["seed-to-soil map"]) < int(fertilizer_type[1]) + int(fertilizer_type[2]):
                seed_location_dict[seed]["soil-to-fertilizer map"] = int(seed_location_dict[seed]["seed-to-soil map"]) + int(fertilizer_type[0]) - int(fertilizer_type[1])
        if "soil-to-fertilizer map" not in seed_location_dict[seed]:
            seed_location_dict[seed]["soil-to-fertilizer map"] = int(seed_location_dict[seed]["seed-to-soil map"])

    return seed_location_dict


# find the water type for each seed
def find_water_type(seed_list, map_dict, seed_location_dict):

    for seed in seed_list:
        for water_type in map_dict["fertilizer-to-water map"]:
            if int(water_type[1]) <= int(seed_location_dict[seed]["soil-to-fertilizer map"]) < int(water_type[1]) + int(water_type[2]):
                seed_location_dict[seed]["fertilizer-to-water map"] = int(seed_location_dict[seed]["soil-to-fertilizer map"]) + int(water_type[0]) - int(water_type[1])
        if "fertilizer-to-water map" not in seed_location_dict[seed]:
            seed_location_dict[seed]["fertilizer-to-water map"] = int(seed_location_dict[seed]["soil-to-fertilizer map"])        
    
    return seed_location_dict

# find the light type for each seed
def find_light_type(seed_list, map_dict, seed_location_dict):

    for seed in seed_list:
        for light_type in map_dict["water-to-light map"]:
            if int(light_type[1]) <= int(seed_location_dict[seed]["fertilizer-to-water map"]) < int(light_type[1]) + int(light_type[2]):
                seed_location_dict[seed]["water-to-light map"] = int(seed_location_dict[seed]["fertilizer-to-water map"]) + int(light_type[0]) - int(light_type[1])
        if "water-to-light map" not in seed_location_dict[seed]:
            seed_location_dict[seed]["water-to-light map"] = int(seed_location_dict[seed]["fertilizer-to-water map"])

    return seed_location_dict


# find the temperature for each seed
def find_temp_type(seed_list, map_dict, seed_location_dict):

    for seed in seed_list:
        for temp_type in map_dict["light-to-temperature map"]:
            if int(temp_type[1]) <= int(seed_location_dict[seed]["water-to-light map"]) < int(temp_type[1]) + int(temp_type[2]):
                seed_location_dict[seed]["light-to-temperature map"] = int(seed_location_dict[seed]["water-to-light map"]) + int(temp_type[0]) - int(temp_type[1])
        if "light-to-temperature map" not in seed_location_dict[seed]:
                seed_location_dict[seed]["light-to-temperature map"] = int(seed_location_dict[seed]["water-to-light map"])

    return seed_location_dict


# find the humidity for each seed
def find_humidity_type(seed_list, map_dict, seed_location_dict):

    for seed in seed_list:
        for humidity_type in map_dict["temperature-to-humidity map"]:
            if int(humidity_type[1]) <= int(seed_location_dict[seed]["light-to-temperature map"]) < int(humidity_type[1]) + int(humidity_type[2]):
                seed_location_dict[seed]["temperature-to-humidity map"] = int(seed_location_dict[seed]["light-to-temperature map"]) + int(humidity_type[0]) - int(humidity_type[1])
        if "temperature-to-humidity map" not in seed_location_dict[seed]:
                seed_location_dict[seed]["temperature-to-humidity map"] = int(seed_location_dict[seed]["light-to-temperature map"])

    return seed_location_dict

# find the location for each seed
def find_location(seed_list, map_dict, seed_location_dict):

    for seed in seed_list:
        for location in map_dict["humidity-to-location map"]:
            if int(location[1]) <= int(seed_location_dict[seed]["temperature-to-humidity map"]) < int(location[1]) + int(location[2]):
                seed_location_dict[seed]["humidity-to-location map"] = int(seed_location_dict[seed]["temperature-to-humidity map"]) + int(location[0]) - int(location[1])
        if "humidity-to-location map" not in seed_location_dict[seed]:
                seed_location_dict[seed]["humidity-to-location map"] = int(seed_location_dict[seed]["temperature-to-humidity map"])

    return seed_location_dict

def parse(buffer):
    
    buffer_split = buffer.split("\n\n")
    seed_location_dict = {}
    map_dict = {}

    # extract seeds
    title, elements= buffer_split[0].split(":")
    for element in elements.split():
        seed_location_dict[element] = {}
    
    # extract maps
    for split in buffer_split[1:]:
        title, elements = split.split(":")

        title = title.strip()
        elements = elements.strip()
        
        element_list = []

        for element in elements.split("\n"):
            element_list.append(element.split())
            map_dict[title] = element_list
    
    return map_dict, seed_location_dict


# pytest unit test
def test_solution():
    test_input = """ seeds: 79 14 55 13

                    seed-to-soil map:
                    50 98 2
                    52 50 48

                    soil-to-fertilizer map:
                    0 15 37
                    37 52 2
                    39 0 15

                    fertilizer-to-water map:
                    49 53 8
                    0 11 42
                    42 0 7
                    57 7 4

                    water-to-light map:
                    88 18 7
                    18 25 70

                    light-to-temperature map:
                    45 77 23
                    81 45 19
                    68 64 13

                    temperature-to-humidity map:
                    0 69 1
                    1 0 69

                    humidity-to-location map:
                    60 56 37
                    56 93 4
                    """
    
    assert find_lowest_location_number(test_input) == 35


def test_partial_solution_soil():
    
    test_map_dict = {'seed-to-soil map': [['50', '98', '2'], ['52', '50', '48']], 'soil-to-fertilizer map': 
                    [['0', '15', '37'], ['37', '52', '2'], ['39', '0', '15']], 
                    'fertilizer-to-water map': [['49', '53', '8'], ['0', '11', '42'], 
                    ['42', '0', '7'], ['57', '7', '4']], 'water-to-light map': [['88', '18', '7'], 
                    ['18', '25', '70']], 'light-to-temperature map': [['45', '77', '23'], 
                    ['81', '45', '19'], ['68', '64', '13']], 'temperature-to-humidity map': 
                    [['0', '69', '1'], ['1', '0', '69']], 'humidity-to-location map': [['60', '56', '37'], 
                    ['56', '93', '4']]}
    
    test_seed_data =     {'79': {}, '14': {}, '55': {}, '13': {}}

    assert find_soil_type(test_map_dict, test_seed_data) == {'79': {'seed-to-soil map': 81}, '14': {'seed-to-soil map': 14}, 
                                                            '55': {'seed-to-soil map': 57}, '13': {'seed-to-soil map': 13}}


def test_partial_solution_fert():
    
    test_map_dict = {'seed-to-soil map': [['50', '98', '2'], ['52', '50', '48']], 'soil-to-fertilizer map': 
                    [['0', '15', '37'], ['37', '52', '2'], ['39', '0', '15']], 
                    'fertilizer-to-water map': [['49', '53', '8'], ['0', '11', '42'], 
                    ['42', '0', '7'], ['57', '7', '4']], 'water-to-light map': [['88', '18', '7'], 
                    ['18', '25', '70']], 'light-to-temperature map': [['45', '77', '23'], 
                    ['81', '45', '19'], ['68', '64', '13']], 'temperature-to-humidity map': 
                    [['0', '69', '1'], ['1', '0', '69']], 'humidity-to-location map': [['60', '56', '37'], 
                    ['56', '93', '4']]}

    test_soil_data =   {'79': {'seed-to-soil map': 81}, '14': {'seed-to-soil map': 14}, 
                        '55': {'seed-to-soil map': 57}, '13': {'seed-to-soil map': 13}}

    seed_list = [seed for seed in test_soil_data]

    assert find_fertilizer_type(seed_list, test_map_dict, test_soil_data) == {'79': {'seed-to-soil map': 81, 'soil-to-fertilizer map': 81}, 
                        '14': {'seed-to-soil map': 14, 'soil-to-fertilizer map': 53},  
                        '55': {'seed-to-soil map': 57, 'soil-to-fertilizer map': 57}, 
                        '13': {'seed-to-soil map': 13, 'soil-to-fertilizer map': 52}}
    

def test_partial_solution_water():
    
    test_map_dict = {'seed-to-soil map': [['50', '98', '2'], ['52', '50', '48']], 'soil-to-fertilizer map': 
                    [['0', '15', '37'], ['37', '52', '2'], ['39', '0', '15']], 
                    'fertilizer-to-water map': [['49', '53', '8'], ['0', '11', '42'], 
                    ['42', '0', '7'], ['57', '7', '4']], 'water-to-light map': [['88', '18', '7'], 
                    ['18', '25', '70']], 'light-to-temperature map': [['45', '77', '23'], 
                    ['81', '45', '19'], ['68', '64', '13']], 'temperature-to-humidity map': 
                    [['0', '69', '1'], ['1', '0', '69']], 'humidity-to-location map': [['60', '56', '37'], 
                    ['56', '93', '4']]}

    test_fert_data =   {'79': {'seed-to-soil map': 81, 'soil-to-fertilizer map': 81}, 
                        '14': {'seed-to-soil map': 14, 'soil-to-fertilizer map': 53},  
                        '55': {'seed-to-soil map': 57, 'soil-to-fertilizer map': 57}, 
                        '13': {'seed-to-soil map': 13, 'soil-to-fertilizer map': 52}}

    seed_list = [seed for seed in test_fert_data]

    assert find_water_type(seed_list, test_map_dict, test_fert_data) == {
                        '79': {'seed-to-soil map': 81, 'soil-to-fertilizer map': 81, 'fertilizer-to-water map': 81}, 
                        '14': {'seed-to-soil map': 14, 'soil-to-fertilizer map': 53, 'fertilizer-to-water map': 49},  
                        '55': {'seed-to-soil map': 57, 'soil-to-fertilizer map': 57, 'fertilizer-to-water map': 53}, 
                        '13': {'seed-to-soil map': 13, 'soil-to-fertilizer map': 52, 'fertilizer-to-water map': 41}}


def test_partial_solution_light():

        
    test_map_dict = {'seed-to-soil map': [['50', '98', '2'], ['52', '50', '48']], 'soil-to-fertilizer map': 
                    [['0', '15', '37'], ['37', '52', '2'], ['39', '0', '15']], 
                    'fertilizer-to-water map': [['49', '53', '8'], ['0', '11', '42'], 
                    ['42', '0', '7'], ['57', '7', '4']], 'water-to-light map': [['88', '18', '7'], 
                    ['18', '25', '70']], 'light-to-temperature map': [['45', '77', '23'], 
                    ['81', '45', '19'], ['68', '64', '13']], 'temperature-to-humidity map': 
                    [['0', '69', '1'], ['1', '0', '69']], 'humidity-to-location map': [['60', '56', '37'], 
                    ['56', '93', '4']]}

    test_water_data =    {'79': {'seed-to-soil map': 81, 'soil-to-fertilizer map': 81, 'fertilizer-to-water map': 81}, 
                        '14': {'seed-to-soil map': 14, 'soil-to-fertilizer map': 53, 'fertilizer-to-water map': 49},  
                        '55': {'seed-to-soil map': 57, 'soil-to-fertilizer map': 57, 'fertilizer-to-water map': 53}, 
                        '13': {'seed-to-soil map': 13, 'soil-to-fertilizer map': 52, 'fertilizer-to-water map': 41}}

    seed_list = [seed for seed in test_water_data]

    assert find_light_type(seed_list, test_map_dict, test_water_data) == {
                        '79': {'seed-to-soil map': 81, 'soil-to-fertilizer map': 81, 
                               'fertilizer-to-water map': 81, 'water-to-light map': 74}, 
                        '14': {'seed-to-soil map': 14, 'soil-to-fertilizer map': 53, 
                               'fertilizer-to-water map': 49, 'water-to-light map': 42},  
                        '55': {'seed-to-soil map': 57, 'soil-to-fertilizer map': 57, 
                               'fertilizer-to-water map': 53, 'water-to-light map': 46}, 
                        '13': {'seed-to-soil map': 13, 'soil-to-fertilizer map': 52, 
                               'fertilizer-to-water map': 41, 'water-to-light map': 34}}


def test_partial_solution_temp():
        
    test_map_dict = {'seed-to-soil map': [['50', '98', '2'], ['52', '50', '48']], 'soil-to-fertilizer map': 
                    [['0', '15', '37'], ['37', '52', '2'], ['39', '0', '15']], 
                    'fertilizer-to-water map': [['49', '53', '8'], ['0', '11', '42'], 
                    ['42', '0', '7'], ['57', '7', '4']], 'water-to-light map': [['88', '18', '7'], 
                    ['18', '25', '70']], 'light-to-temperature map': [['45', '77', '23'], 
                    ['81', '45', '19'], ['68', '64', '13']], 'temperature-to-humidity map': 
                    [['0', '69', '1'], ['1', '0', '69']], 'humidity-to-location map': [['60', '56', '37'], 
                    ['56', '93', '4']]}

    test_light_data =   {'79': {'seed-to-soil map': 81, 'soil-to-fertilizer map': 81, 
                               'fertilizer-to-water map': 81, 'water-to-light map': 74}, 
                        '14': {'seed-to-soil map': 14, 'soil-to-fertilizer map': 53, 
                               'fertilizer-to-water map': 49, 'water-to-light map': 42},  
                        '55': {'seed-to-soil map': 57, 'soil-to-fertilizer map': 57, 
                               'fertilizer-to-water map': 53, 'water-to-light map': 46}, 
                        '13': {'seed-to-soil map': 13, 'soil-to-fertilizer map': 52, 
                               'fertilizer-to-water map': 41, 'water-to-light map': 34}}

    seed_list = [seed for seed in test_light_data]

    assert find_temp_type(seed_list, test_map_dict, test_light_data) == {
                        '79': {'seed-to-soil map': 81, 'soil-to-fertilizer map': 81, 
                               'fertilizer-to-water map': 81, 'water-to-light map': 74,
                               'light-to-temperature map': 78}, 
                        '14': {'seed-to-soil map': 14, 'soil-to-fertilizer map': 53, 
                               'fertilizer-to-water map': 49, 'water-to-light map': 42,
                               'light-to-temperature map': 42},  
                        '55': {'seed-to-soil map': 57, 'soil-to-fertilizer map': 57, 
                               'fertilizer-to-water map': 53, 'water-to-light map': 46, 
                               'light-to-temperature map': 82}, 
                        '13': {'seed-to-soil map': 13, 'soil-to-fertilizer map': 52, 
                               'fertilizer-to-water map': 41, 'water-to-light map': 34, 
                               'light-to-temperature map': 34}}


def test_partial_solution_humidity():
        
    test_map_dict = {'seed-to-soil map': [['50', '98', '2'], ['52', '50', '48']], 'soil-to-fertilizer map': 
                    [['0', '15', '37'], ['37', '52', '2'], ['39', '0', '15']], 
                    'fertilizer-to-water map': [['49', '53', '8'], ['0', '11', '42'], 
                    ['42', '0', '7'], ['57', '7', '4']], 'water-to-light map': [['88', '18', '7'], 
                    ['18', '25', '70']], 'light-to-temperature map': [['45', '77', '23'], 
                    ['81', '45', '19'], ['68', '64', '13']], 'temperature-to-humidity map': 
                    [['0', '69', '1'], ['1', '0', '69']], 'humidity-to-location map': [['60', '56', '37'], 
                    ['56', '93', '4']]}

    test_temp_data =    {'79': {'seed-to-soil map': 81, 'soil-to-fertilizer map': 81, 
                               'fertilizer-to-water map': 81, 'water-to-light map': 74,
                               'light-to-temperature map': 78}, 
                        '14': {'seed-to-soil map': 14, 'soil-to-fertilizer map': 53, 
                               'fertilizer-to-water map': 49, 'water-to-light map': 42,
                               'light-to-temperature map': 42},  
                        '55': {'seed-to-soil map': 57, 'soil-to-fertilizer map': 57, 
                               'fertilizer-to-water map': 53, 'water-to-light map': 46, 
                               'light-to-temperature map': 82}, 
                        '13': {'seed-to-soil map': 13, 'soil-to-fertilizer map': 52, 
                               'fertilizer-to-water map': 41, 'water-to-light map': 34, 
                               'light-to-temperature map': 34}}
    
    seed_list = [seed for seed in test_temp_data]

    assert find_humidity_type(seed_list, test_map_dict, test_temp_data) == {
                    '79': {'seed-to-soil map': 81, 'soil-to-fertilizer map': 81, 
                            'fertilizer-to-water map': 81, 'water-to-light map': 74,
                            'light-to-temperature map': 78, 'temperature-to-humidity map': 78}, 
                    '14': {'seed-to-soil map': 14, 'soil-to-fertilizer map': 53, 
                            'fertilizer-to-water map': 49, 'water-to-light map': 42,
                            'light-to-temperature map': 42, 'temperature-to-humidity map': 43},  
                    '55': {'seed-to-soil map': 57, 'soil-to-fertilizer map': 57, 
                            'fertilizer-to-water map': 53, 'water-to-light map': 46, 
                            'light-to-temperature map': 82, 'temperature-to-humidity map': 82},
                    '13': {'seed-to-soil map': 13, 'soil-to-fertilizer map': 52, 
                            'fertilizer-to-water map': 41, 'water-to-light map': 34, 
                            'light-to-temperature map': 34, 'temperature-to-humidity map': 35}}


def test_partial_solution_location():
        
    test_map_dict = {'seed-to-soil map': [['50', '98', '2'], ['52', '50', '48']], 'soil-to-fertilizer map': 
                    [['0', '15', '37'], ['37', '52', '2'], ['39', '0', '15']], 
                    'fertilizer-to-water map': [['49', '53', '8'], ['0', '11', '42'], 
                    ['42', '0', '7'], ['57', '7', '4']], 'water-to-light map': [['88', '18', '7'], 
                    ['18', '25', '70']], 'light-to-temperature map': [['45', '77', '23'], 
                    ['81', '45', '19'], ['68', '64', '13']], 'temperature-to-humidity map': 
                    [['0', '69', '1'], ['1', '0', '69']], 'humidity-to-location map': [['60', '56', '37'], 
                    ['56', '93', '4']]}

    test_humidity_data = {'79': {'seed-to-soil map': 81, 'soil-to-fertilizer map': 81, 
                            'fertilizer-to-water map': 81, 'water-to-light map': 74,
                            'light-to-temperature map': 78, 'temperature-to-humidity map': 78}, 
                    '14': {'seed-to-soil map': 14, 'soil-to-fertilizer map': 53, 
                            'fertilizer-to-water map': 49, 'water-to-light map': 42,
                            'light-to-temperature map': 42, 'temperature-to-humidity map': 43},  
                    '55': {'seed-to-soil map': 57, 'soil-to-fertilizer map': 57, 
                            'fertilizer-to-water map': 53, 'water-to-light map': 46, 
                            'light-to-temperature map': 82, 'temperature-to-humidity map': 82},
                    '13': {'seed-to-soil map': 13, 'soil-to-fertilizer map': 52, 
                            'fertilizer-to-water map': 41, 'water-to-light map': 34, 
                            'light-to-temperature map': 34, 'temperature-to-humidity map': 35}}
    seed_list = [seed for seed in test_humidity_data]

    assert find_location(seed_list, test_map_dict, test_humidity_data) == {
                    '79': {'seed-to-soil map': 81, 'soil-to-fertilizer map': 81, 
                            'fertilizer-to-water map': 81, 'water-to-light map': 74,
                            'light-to-temperature map': 78, 'temperature-to-humidity map': 78,
                            'humidity-to-location map': 82}, 
                    '14': {'seed-to-soil map': 14, 'soil-to-fertilizer map': 53, 
                            'fertilizer-to-water map': 49, 'water-to-light map': 42,
                            'light-to-temperature map': 42, 'temperature-to-humidity map': 43,
                            'humidity-to-location map': 43},  
                    '55': {'seed-to-soil map': 57, 'soil-to-fertilizer map': 57, 
                            'fertilizer-to-water map': 53, 'water-to-light map': 46, 
                            'light-to-temperature map': 82, 'temperature-to-humidity map': 82,
                            'humidity-to-location map': 86},
                    '13': {'seed-to-soil map': 13, 'soil-to-fertilizer map': 52, 
                            'fertilizer-to-water map': 41, 'water-to-light map': 34, 
                            'light-to-temperature map': 34, 'temperature-to-humidity map': 35,
                            'humidity-to-location map': 35}}


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        buffer = file.read()
        print(find_lowest_location_number(buffer))