# advent of code day 8, part 1

def calculate_steps(buffer):
    directions, locations_dict = parse(buffer)

    step_counter = 0
    # set starting location at origin
    location = "AAA"

    while location != "ZZZ":
        for direction in directions:
            # run directions until the destintation is reached
            if location != "ZZZ":
                if direction == "L":
                    location = locations_dict[location]["left"]
                    step_counter += 1
                else:
                    location = locations_dict[location]["right"]
                    step_counter += 1
            else:
                break
    
    return step_counter


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

    buffer = """RL

                AAA = (BBB, CCC)
                BBB = (DDD, EEE)
                CCC = (ZZZ, GGG)
                DDD = (DDD, DDD)
                EEE = (EEE, EEE)
                GGG = (GGG, GGG)
                ZZZ = (ZZZ, ZZZ) """
    
    assert calculate_steps(buffer) == 2


def test_solution_reg_instruction():

    buffer = """LLR

            AAA = (BBB, BBB)
            BBB = (AAA, ZZZ)
            ZZZ = (ZZZ, ZZZ)) """
    
    assert calculate_steps(buffer) == 6


if __name__ == "__main__":

    with open('input.txt', 'r') as file:
        buffer = file.read()
        print(calculate_steps(buffer))