# Advent of Code 2023 Day 3, Part 1

import re

# create a 2-d array of all the characters in the input file
def create_array(file):
    engine_parts_array = []
    for line in file:
        engine_parts_array.append(line.strip())
    
    return engine_parts_array


# use the array to determine which engine parts are not relevant to the calculation
def part_number_calculation(engine_parts_array):

    sum_gear_ratio = 0
    part_number_location_dict = {}
    
    # ensure that parts with the same part number have a unique identifier
    part_counter = 0

    # create a y coordinate for each line in the array
    for y_coord, line in enumerate(engine_parts_array):

        # find all the part numbers in each line
        part_matches = re.finditer(r'\d+', line)

        for match in part_matches:
            part_counter += 1
            for x_coord in range(match.start(0), match.end(0)):
                # the part_counter serves as a unique identifier for each part
                part_number_location_dict[(x_coord, y_coord)] = match.group(0), part_counter

    # create a y coordinate for each line in the array
    for y_coord, line in enumerate(engine_parts_array):
        
        # find all the gear matches in each line
        gear_matches = re.finditer(r'\*', line)
        
        # determine which gears are touching exactly two part numbers
        for match in gear_matches:
            start_x_coord = match.start(0)
            end_x_coord = match.end(0)
            gear_touching_part = set()

            # check each coordinate by inspecting every adjacent coordinate for each grid space around any gear
            for x_coord in range(start_x_coord, end_x_coord):
                # create an offset for x-coordinates to check the surrounding coordinates
                for x_offset in (-1, 0, 1):
                    # create an offset for y-coordinates to check the surrounding coordinates
                    for y_offset in (-1, 0, 1):
                        try: 
                            # find the unique parts (may have the same part number) that are touching the gear
                            gear_touching_part.add(part_number_location_dict[(x_coord + x_offset, y_coord + y_offset)])
                        # ignore IndexError and Keyerror exceptions for the coordinates that are out of range
                        except (IndexError, KeyError):
                            continue
            
            # add the part number for ratio calculation and then sum the gear ratios
            if len(gear_touching_part) == 2:
                gear_touching_part = list(gear_touching_part)
                gear_ratio = int(gear_touching_part[0][0]) * int(gear_touching_part[1][0])
                sum_gear_ratio += gear_ratio

    return sum_gear_ratio


# pytest unit test
def test_solution():
    test_input = """ 
                467..114..
                ...*......
                ..35..633.
                ......#...
                617*......
                .....+.58.
                ..592.....
                ......755.
                ...$.*....
                .664.598.. """.split("\n")

    assert part_number_calculation(test_input) == 467835


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        engine_parts_array = create_array(file)
        print(part_number_calculation(engine_parts_array))