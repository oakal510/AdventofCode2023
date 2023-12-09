# advent of code day 8, part 2

from math import lcm

def calculate_steps(buffer):
    directions, locations_dict = parse(buffer)

    step_counter = 0
    current_locations = []
    end_locations = []
    step_counter_dict = {}

    # set starting location at origins
    for location in locations_dict:
        if location[2] == "A":
            current_locations.append(location)

    for location in locations_dict:
        if location[2] == "Z":
            end_locations.append(location)

    while len(end_locations) > 0:
        for direction in directions:
            if len(end_locations) > 0:
                for i, location in enumerate(current_locations):
                    # run directions until the destintation is reached
                    if direction == "L":
                        current_locations[i] = locations_dict[location]["left"]
                        
                    else:
                        current_locations[i] = locations_dict[location]["right"]
                step_counter += 1
            
            else:
                break

            # check if any of the end locations are the current locations    
            for location in current_locations:
                # if an end location is reached, record the step counter for that location and remove it from the list
                if location in end_locations:
                    step_counter_dict[location] = int(step_counter)
                    end_locations.remove(location)   

    # find the least comomon multiple of all the step_counter values for every journey to get the total step counter
    total_step_counter = lcm(*list(step_counter_dict.values()))

    return total_step_counter

def parse(data):
    directions, locations = data.split('\n\n')
    locations_dict = {}

    for location in locations.splitlines():
        location_items = location.split('=')
        location_origin = location_items[0].strip()
        left, right = location_items[1].split(',')
        left = left.replace('(', '').strip()
        right = right.strip().replace(')','')
        locations_dict[location_origin] = {"left": left, "right": right}

    return directions, locations_dict


def test_solution_easy_instruction():

    buffer = """LR

            11A = (11B, XXX)
            11B = (XXX, 11Z)
            11Z = (11B, XXX)
            22A = (22B, XXX)
            22B = (22C, 22C)
            22C = (22Z, 22Z)
            22Z = (22B, 22B)
            XXX = (XXX, XXX) """
                
    assert calculate_steps(buffer) == 6


if __name__ == "__main__":

    with open('input.txt', 'r') as file:
        buffer = file.read()
        print(calculate_steps(buffer))