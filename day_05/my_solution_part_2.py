# solution to Advent of Code day 5 part 2

class Seed:
    def __init__(self, seed_value, range):
        self.initial_seed_value = int(seed_value)
        self.seed_value = int(seed_value)
        self.range = int(range)
        self.location_found = False
    
    def find_seed_location(self, map_dict):

        new_seed_list = []

        for seed_map in map_dict:
            for line in map_dict[seed_map]:
                map_output = int(line[0])
                map_input = int(line[1])
                map_range = int(line[2])
                if map_input <= self.seed_value < map_input + map_range:
                    # find the range overflows to create new seed / range objects
                    if self.range + self.seed_value > map_input + map_range:
                        
                        current_seed_range = map_input + map_range - self.seed_value
                        new_seed_range = self.range - current_seed_range
                        new_seed_value = self.initial_seed_value + current_seed_range
                        new_seed = Seed(new_seed_value, new_seed_range)
                        new_seed_list.append(new_seed)  
                        
                        self.seed_value = self.seed_value + map_output - map_input
                        self.range = current_seed_range
                        break
                    else:
                        
                        self.seed_value = self.seed_value + map_output - map_input
                        break
                        
            
        self.location_found = True
        return new_seed_list


def find_lowest_location_number(buffer):

    map_dict, primary_seed_list = parse(buffer)
    new_seed_list = []

    for seed in primary_seed_list:
        if seed.location_found == False:
            new_seed_list = seed.find_seed_location(map_dict)
        primary_seed_list.extend(new_seed_list)
    

    return min([seed.seed_value for seed in primary_seed_list])


def parse(buffer):
    
    buffer_split = buffer.split("\n\n")
    seed_list = []
    map_dict = {}

    # extract seeds
    title, elements= buffer_split[0].split(":")
    element_list = [int(element) for element in elements.split()]
    
    for i, element in enumerate(element_list):
        if i % 2 == 0:
            seed = Seed(int(element), int(element_list[i+1]))
            seed_list.append(seed)

    # extract maps
    for split in buffer_split[1:]:
        title, elements = split.split(":")

        title = title.strip()
        elements = elements.strip()
        
        element_list = []

        for element in elements.split("\n"):
            element_list.append(element.split())
            map_dict[title] = element_list
    
    return map_dict, seed_list


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


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        buffer = file.read()
        print(find_lowest_location_number(buffer))