# solution to Advent of Code day 5 part 2

import pprint

def find_lowest_location_number(buffer):

    map_dict, seed_location_dict = parse(buffer)
    # pprint.pprint(seed_location_dict)
    seed_location_dict = find_soil_type(map_dict, seed_location_dict)
    pprint.pprint(seed_location_dict)
    seed_location_dict = find_fertilizer_type(map_dict, seed_location_dict)
    # pprint.pprint(seed_location_dict)
    seed_location_dict = find_water_type(map_dict, seed_location_dict)
    # pprint.pprint(seed_location_dict)
    seed_location_dict = find_light_type(map_dict, seed_location_dict)
    # pprint.pprint(seed_location_dict)
    seed_location_dict = find_temp_type(map_dict, seed_location_dict)
    # pprint.pprint(seed_location_dict)
    seed_location_dict = find_humidity_type(map_dict, seed_location_dict)
    # pprint.pprint(seed_location_dict)
    seed_location_dict = find_location(map_dict, seed_location_dict)

    # pprint.pprint(seed_location_dict)

    return min([dictionary['value'] for dictionary in seed_location_dict.values()])
        

def range_checker(initial_check, range_check, seed_value, seed_range, map_in_value, map_out_value, map_range):
    
    if not initial_check:
        if map_in_value <= seed_value < map_in_value + map_range:
            initial_check = True
        
            if map_in_value <= seed_value + seed_range < map_in_value + map_range:
                range_check = True
                return initial_check, range_check, seed_value + map_out_value - map_in_value
            
            return initial_check, range_check, seed_value + map_out_value - map_in_value
    
        else:
            return initial_check, range_check, seed_value

    else:
        pass



        return initial_check, range_check, seed_value


# find the location for each seed
def find_soil_type(map_dict, seed_location_dict):

    soil_check_complete = False
    range_check = False

    for seed in seed_location_dict:
        for soil in map_dict["seed-to-soil map"]:
            range_check, soil_check_complete, new_value = range_checker(soil_check_complete, range_check, 
                                                                        seed_location_dict[seed]["value"], 
                                                                        seed_location_dict[seed]["range"], 
                                                                        int(soil[1]), int(soil[0]), 
                                                                        int(soil[2]))
            
            if soil_check_complete:
                seed_location_dict[seed]["value"] = new_value
                range_check, soil_check_complete, new_value = range_checker(soil_check_complete, range_check, 
                                                                            seed_location_dict[seed]["value"], 
                                                                            seed_location_dict[seed]["range"], 
                                                                            int(soil[1]), int(soil[0]), 
                                                                            int(soil[2]))
                
                while not range_check:
                        
                    restart_check = False
                    seed_location_dict[new_value + int(soil[2])]["value"] = seed + int(soil[2])
                    seed_location_dict[new_value + int(soil[2])]["range"] = seed_location_dict[seed]["range"] - int(soil[2])

                    for soil in map_dict["seed-to-soil map"]:
                        range_check, restart_check, new_value = range_checker(restart_check, range_check, 
                                                                            seed_location_dict[int(soil[0]) + int(soil[2])]["value"], 
                                                                            seed_location_dict[int(soil[0]) + int(soil[2])]["range"], 
                                                                            int(soil[1]), int(soil[0]), 
                                                                            int(soil[2]))
                        
                        if restart_check:
                            pass

                
                if range_check:
                    break

    return seed_location_dict


# find the fertilizer for each seed
def find_fertilizer_type(map_dict, seed_location_dict):

    seed_list = [seed for seed in seed_location_dict]

    for seed in seed_list:
        for fertilizer_type in map_dict["soil-to-fertilizer map"]:
            if int(fertilizer_type[1]) <= int(seed_location_dict[seed]) < int(fertilizer_type[1]) + int(fertilizer_type[2]):
                seed_location_dict[seed] = int(seed_location_dict[seed]) + int(fertilizer_type[0]) - int(fertilizer_type[1])
                break

    return seed_location_dict


# find the water type for each seed
def find_water_type(map_dict, seed_location_dict):

    seed_list = [seed for seed in seed_location_dict]

    for seed in seed_list:
        for water_type in map_dict["fertilizer-to-water map"]:
            if int(water_type[1]) <= int(seed_location_dict[seed]) < int(water_type[1]) + int(water_type[2]):
                seed_location_dict[seed] = int(seed_location_dict[seed]) + int(water_type[0]) - int(water_type[1])
                break

    return seed_location_dict


# find the light type for each seed
def find_light_type(map_dict, seed_location_dict):

    seed_list = [seed for seed in seed_location_dict]

    for seed in seed_list:
        for light_type in map_dict["water-to-light map"]:
            if int(light_type[1]) <= int(seed_location_dict[seed]) < int(light_type[1]) + int(light_type[2]):
                seed_location_dict[seed] = int(seed_location_dict[seed]) + int(light_type[0]) - int(light_type[1])
                break

    return seed_location_dict


# find the temperature for each seed
def find_temp_type(map_dict, seed_location_dict):

    seed_list = [seed for seed in seed_location_dict]

    for seed in seed_list:
        for temp_type in map_dict["light-to-temperature map"]:
            if int(temp_type[1]) <= int(seed_location_dict[seed]) < int(temp_type[1]) + int(temp_type[2]):
                seed_location_dict[seed] = int(seed_location_dict[seed]) + int(temp_type[0]) - int(temp_type[1])
                break

    return seed_location_dict


# find the humidity for each seed
def find_humidity_type(map_dict, seed_location_dict):

    seed_list = [seed for seed in seed_location_dict]

    for seed in seed_list:
        for humidity_type in map_dict["temperature-to-humidity map"]:
            if int(humidity_type[1]) <= int(seed_location_dict[seed]) < int(humidity_type[1]) + int(humidity_type[2]):
                seed_location_dict[seed] = int(seed_location_dict[seed]) + int(humidity_type[0]) - int(humidity_type[1])
                break 

    return seed_location_dict


# find the location for each seed
def find_location(map_dict, seed_location_dict):

    seed_list = [seed for seed in seed_location_dict]

    for seed in seed_list:
        for location in map_dict["humidity-to-location map"]:
            if int(location[1]) <= int(seed_location_dict[seed]) < int(location[1]) + int(location[2]):
                seed_location_dict[seed] = int(seed_location_dict[seed]) + int(location[0]) - int(location[1])
                break

    return seed_location_dict


def parse(buffer):
    
    buffer_split = buffer.split("\n\n")
    seed_location_dict = {}
    map_dict = {}

    # extract seeds
    title, elements= buffer_split[0].split(":")
    element_list = [int(element) for element in elements.split()]

    for i, element in enumerate(element_list):
        if i % 2 == 0:
            seed_location_dict[element] = {"value": int(element), "range": int(element_list[i+1])}

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
    
    assert find_lowest_location_number(test_input) == 46

def test_seed_79_soil():

    test_map_dict = {'seed-to-soil map': [['50', '98', '2'], ['52', '50', '48']], 'soil-to-fertilizer map': 
                    [['0', '15', '37'], ['37', '52', '2'], ['39', '0', '15']], 
                    'fertilizer-to-water map': [['49', '53', '8'], ['0', '11', '42'], 
                    ['42', '0', '7'], ['57', '7', '4']], 'water-to-light map': [['88', '18', '7'], 
                    ['18', '25', '70']], 'light-to-temperature map': [['45', '77', '23'], 
                    ['81', '45', '19'], ['68', '64', '13']], 'temperature-to-humidity map': 
                    [['0', '69', '1'], ['1', '0', '69']], 'humidity-to-location map': [['60', '56', '37'], 
                    ['56', '93', '4']]}

    test_seed_dict = {79: {'value': 79, 'range': 14}}

    assert find_soil_type(test_map_dict, test_seed_dict) == {79: {'value': 81, 'range': 14}}


def test_seed_82_soil():

    test_map_dict = {'seed-to-soil map': [['50', '98', '2'], ['52', '50', '48']], 'soil-to-fertilizer map': 
                    [['0', '15', '37'], ['37', '52', '2'], ['39', '0', '15']], 
                    'fertilizer-to-water map': [['49', '53', '8'], ['0', '11', '42'], 
                    ['42', '0', '7'], ['57', '7', '4']], 'water-to-light map': [['88', '18', '7'], 
                    ['18', '25', '70']], 'light-to-temperature map': [['45', '77', '23'], 
                    ['81', '45', '19'], ['68', '64', '13']], 'temperature-to-humidity map': 
                    [['0', '69', '1'], ['1', '0', '69']], 'humidity-to-location map': [['60', '56', '37'], 
                    ['56', '93', '4']]}

    test_seed_dict = {79: {'value': 79, 'range': 14}}

    assert find_soil_type(test_map_dict, test_seed_dict)[79]["value"] + 3 == 84


def test_seed_out_of_range_soil():

    test_map_dict = {'seed-to-soil map': [['50', '98', '2'], ['52', '50', '48']], 'soil-to-fertilizer map': 
                    [['0', '15', '37'], ['37', '52', '2'], ['39', '0', '15']], 
                    'fertilizer-to-water map': [['49', '53', '8'], ['0', '11', '42'], 
                    ['42', '0', '7'], ['57', '7', '4']], 'water-to-light map': [['88', '18', '7'], 
                    ['18', '25', '70']], 'light-to-temperature map': [['45', '77', '23'], 
                    ['81', '45', '19'], ['68', '64', '13']], 'temperature-to-humidity map': 
                    [['0', '69', '1'], ['1', '0', '69']], 'humidity-to-location map': [['60', '56', '37'], 
                    ['56', '93', '4']]}

    test_seed_dict = {98: {'value': 98, 'range': 3}}

    assert find_soil_type(test_map_dict, test_seed_dict) == {98: {'value': 98, 'range': 2}, 100: {'value': 100, 'range': 1}}


def test_seed_82_fert():

    test_map_dict = {'seed-to-soil map': [['50', '98', '2'], ['52', '50', '48']], 'soil-to-fertilizer map': 
                    [['0', '15', '37'], ['37', '52', '2'], ['39', '0', '15']], 
                    'fertilizer-to-water map': [['49', '53', '8'], ['0', '11', '42'], 
                    ['42', '0', '7'], ['57', '7', '4']], 'water-to-light map': [['88', '18', '7'], 
                    ['18', '25', '70']], 'light-to-temperature map': [['45', '77', '23'], 
                    ['81', '45', '19'], ['68', '64', '13']], 'temperature-to-humidity map': 
                    [['0', '69', '1'], ['1', '0', '69']], 'humidity-to-location map': [['60', '56', '37'], 
                    ['56', '93', '4']]}

    test_seed_dict = {82: 84}

    assert find_fertilizer_type(test_map_dict, test_seed_dict) == {82: 84}


def test_seed_82_water():

    test_map_dict = {'seed-to-soil map': [['50', '98', '2'], ['52', '50', '48']], 'soil-to-fertilizer map': 
                    [['0', '15', '37'], ['37', '52', '2'], ['39', '0', '15']], 
                    'fertilizer-to-water map': [['49', '53', '8'], ['0', '11', '42'], 
                    ['42', '0', '7'], ['57', '7', '4']], 'water-to-light map': [['88', '18', '7'], 
                    ['18', '25', '70']], 'light-to-temperature map': [['45', '77', '23'], 
                    ['81', '45', '19'], ['68', '64', '13']], 'temperature-to-humidity map': 
                    [['0', '69', '1'], ['1', '0', '69']], 'humidity-to-location map': [['60', '56', '37'], 
                    ['56', '93', '4']]}

    test_seed_dict = {82: 84}

    assert find_water_type(test_map_dict, test_seed_dict) == {82: 84}


def test_seed_82_light():

    test_map_dict = {'seed-to-soil map': [['50', '98', '2'], ['52', '50', '48']], 'soil-to-fertilizer map': 
                    [['0', '15', '37'], ['37', '52', '2'], ['39', '0', '15']], 
                    'fertilizer-to-water map': [['49', '53', '8'], ['0', '11', '42'], 
                    ['42', '0', '7'], ['57', '7', '4']], 'water-to-light map': [['88', '18', '7'], 
                    ['18', '25', '70']], 'light-to-temperature map': [['45', '77', '23'], 
                    ['81', '45', '19'], ['68', '64', '13']], 'temperature-to-humidity map': 
                    [['0', '69', '1'], ['1', '0', '69']], 'humidity-to-location map': [['60', '56', '37'], 
                    ['56', '93', '4']]}

    test_seed_dict = {82: 84}

    assert find_light_type(test_map_dict, test_seed_dict) == {82: 77}


def test_seed_82_temp():

    test_map_dict = {'seed-to-soil map': [['50', '98', '2'], ['52', '50', '48']], 'soil-to-fertilizer map': 
                    [['0', '15', '37'], ['37', '52', '2'], ['39', '0', '15']], 
                    'fertilizer-to-water map': [['49', '53', '8'], ['0', '11', '42'], 
                    ['42', '0', '7'], ['57', '7', '4']], 'water-to-light map': [['88', '18', '7'], 
                    ['18', '25', '70']], 'light-to-temperature map': [['45', '77', '23'], 
                    ['81', '45', '19'], ['68', '64', '13']], 'temperature-to-humidity map': 
                    [['0', '69', '1'], ['1', '0', '69']], 'humidity-to-location map': [['60', '56', '37'], 
                    ['56', '93', '4']]}

    test_seed_dict = {82: 77}

    assert find_temp_type(test_map_dict, test_seed_dict) == {82: 45}


def test_seed_82_humidity():

    test_map_dict = {'seed-to-soil map': [['50', '98', '2'], ['52', '50', '48']], 'soil-to-fertilizer map': 
                    [['0', '15', '37'], ['37', '52', '2'], ['39', '0', '15']], 
                    'fertilizer-to-water map': [['49', '53', '8'], ['0', '11', '42'], 
                    ['42', '0', '7'], ['57', '7', '4']], 'water-to-light map': [['88', '18', '7'], 
                    ['18', '25', '70']], 'light-to-temperature map': [['45', '77', '23'], 
                    ['81', '45', '19'], ['68', '64', '13']], 'temperature-to-humidity map': 
                    [['0', '69', '1'], ['1', '0', '69']], 'humidity-to-location map': [['60', '56', '37'], 
                    ['56', '93', '4']]}

    test_seed_dict = {82: 45}

    assert find_humidity_type(test_map_dict, test_seed_dict) == {82: 46}


def test_seed_82_location():

    test_map_dict = {'seed-to-soil map': [['50', '98', '2'], ['52', '50', '48']], 'soil-to-fertilizer map': 
                    [['0', '15', '37'], ['37', '52', '2'], ['39', '0', '15']], 
                    'fertilizer-to-water map': [['49', '53', '8'], ['0', '11', '42'], 
                    ['42', '0', '7'], ['57', '7', '4']], 'water-to-light map': [['88', '18', '7'], 
                    ['18', '25', '70']], 'light-to-temperature map': [['45', '77', '23'], 
                    ['81', '45', '19'], ['68', '64', '13']], 'temperature-to-humidity map': 
                    [['0', '69', '1'], ['1', '0', '69']], 'humidity-to-location map': [['60', '56', '37'], 
                    ['56', '93', '4']]}

    test_seed_dict = {82: 46}

    assert find_location(test_map_dict, test_seed_dict) == {82: 46}


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        buffer = file.read()
        print(find_lowest_location_number(buffer))