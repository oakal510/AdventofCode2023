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

    sum_parts_number = 0

    # create a y coordinate for each line in the array
    for y_coord, line in enumerate(engine_parts_array):
        
        # find all the part numbers in each line
        matches = re.finditer(r'\d+', line)
        
        # determine which part numbers to drop
        for match in matches:
            part_number = match.group(0)
            start_x_coord = match.start(0)
            end_x_coord = match.end(0)
            keep_part_number = False

            # check each coordinate by inspecting every adjacent coordinate for each grid space around any digit of a part number
            for x_coord in range(start_x_coord, end_x_coord):
                # create an offset for x-coordinates to check the surrounding coordinates
                for x_offset in (-1, 0, 1):
                    # create an offset for y-coordinates to check the surrounding coordinates
                    for y_offset in (-1, 0, 1):
                        try: 
                            value = engine_parts_array[y_coord + y_offset][x_coord + x_offset]
                            # check the surrounding coordinates for a "." or a digit to determine if the part number is relevant
                            if not (value == "." or value.isdigit()):
                                keep_part_number = True
                        # ignore IndexError exceptions for the coordinates that are out of range
                        except IndexError:
                            continue
            
            # add the part number to the sum if it is relevant
            if keep_part_number:
                sum_parts_number += int(part_number)    

    return sum_parts_number


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

    assert part_number_calculation(test_input) == 4361

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        engine_parts_array = create_array(file)
        print(part_number_calculation(engine_parts_array))