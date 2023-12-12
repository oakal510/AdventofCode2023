# day 10, part 1

class Tile:
    def __init__(self, tile, x_coord, y_coord):
        self.tile = tile
        self.x_coord =  x_coord
        self.y_coord = y_coord
        self.type = self.find_type()
        self.flow_directions = self.find_flow_directions()


    def __str__(self):
        return f"Tile: {self.tile}, x: {self.x_coord}, y: {self.y_coord}, type: {self.type}, flow directions: {self.flow_directions}"

    def find_type(self):

        pipe = ['|', '-', '7', 'L', 'F', 'J', 'S']
        if self.tile in pipe:
            return 'pipe'
        else:
            return 'ground'
        

    def find_flow_directions(self):

        if self.type == 'ground':
            return None
        elif self.type == 'pipe':
            if self.tile == 'S':
                return ['north', 'south', 'east', 'west']
            elif self.tile == '|':
                return ['north', 'south']
            elif self.tile == '-':
                return ['east', 'west']
            elif self.tile == 'L':
                return ['north', 'east']
            elif self.tile == 'J':
                return ['north', 'west'] 
            elif self.tile == '7':
                return ['south', 'west']
            elif self.tile == 'F':
                return ['south', 'east']


def find_furthest_tile(buffer):
    
    pipe_schematic, starting_x_coord, starting_y_coord = parse(buffer)
    loop = find_loop(pipe_schematic, starting_x_coord, starting_y_coord)

    return (len(loop) / 2)


def find_loop(pipe_schematic, starting_x_coord, starting_y_coord):
   
    starting_tile = pipe_schematic[starting_x_coord, starting_y_coord]
    relevant_adj_tiles = validate_adj_tiles(pipe_schematic, starting_x_coord, starting_y_coord)
    
    loop = []

    for tile in relevant_adj_tiles:

        last_tile = starting_tile
        loop.append(tile)

        for tile in loop:
            current_tile = tile            
            
            if current_tile.type != 'pipe':
                loop.remove(current_tile)

            if current_tile == last_tile: 
                loop.remove(current_tile)

            elif current_tile != starting_tile:

                if 'north' in current_tile.flow_directions:
                    new_tile = pipe_schematic[current_tile.x_coord, current_tile.y_coord - 1]
                    if new_tile not in loop and new_tile != last_tile:
                        loop.append(new_tile)
                if 'south' in current_tile.flow_directions:
                    new_tile = pipe_schematic[current_tile.x_coord, current_tile.y_coord + 1]
                    if new_tile not in loop and new_tile != last_tile:
                        loop.append(new_tile)
                if 'east' in current_tile.flow_directions:
                    new_tile = pipe_schematic[current_tile.x_coord + 1, current_tile.y_coord]
                    if new_tile not in loop and new_tile != last_tile:
                        loop.append(new_tile)
                if 'west' in current_tile.flow_directions:  
                    new_tile = pipe_schematic[current_tile.x_coord - 1, current_tile.y_coord]
                    if new_tile not in loop and new_tile != last_tile:
                        loop.append(new_tile)
            else:
                return loop

            last_tile = current_tile


def validate_adj_tiles(pipe_schematic, starting_x_coord, starting_y_coord):
   
    starting_tile = pipe_schematic[starting_x_coord, starting_y_coord]

    adjacent_tiles = []

    if not starting_tile.x_coord == 0:
        adjacent_tiles.append(pipe_schematic[starting_x_coord - 1, starting_y_coord])
    if not starting_tile.x_coord == 5:
        adjacent_tiles.append(pipe_schematic[starting_x_coord + 1, starting_y_coord])
    if not starting_tile.y_coord == 0:
        adjacent_tiles.append(pipe_schematic[starting_x_coord, starting_y_coord - 1])
    if not starting_tile.y_coord == 5:
        adjacent_tiles.append(pipe_schematic[starting_x_coord, starting_y_coord + 1])
                    
    relevant_adj_tiles = validate_adjacency(adjacent_tiles, starting_tile)

    return relevant_adj_tiles


def validate_adjacency(adjacent_tiles, starting_tile):

    relevant_adj_tiles = []

    for tile in adjacent_tiles:
        if tile.type == 'pipe':
            if 'north' in tile.flow_directions:
                if tile.x_coord == starting_tile.x_coord and tile.y_coord - 1 == starting_tile.y_coord:
                    relevant_adj_tiles.append(tile)
            if 'south' in tile.flow_directions:
                if tile.x_coord == starting_tile.x_coord and tile.y_coord + 1 == starting_tile.y_coord:
                    relevant_adj_tiles.append(tile)
            if 'east' in tile.flow_directions:
                if tile.x_coord + 1 == starting_tile.x_coord and tile.y_coord == starting_tile.y_coord:
                    relevant_adj_tiles.append(tile)
            if 'west' in tile.flow_directions:  
                if tile.x_coord - 1 == starting_tile.x_coord and tile.y_coord == starting_tile.y_coord:
                    relevant_adj_tiles.append(tile)
        
    return relevant_adj_tiles


def parse(buffer):

    pipe_schematic = {}
    
    for i, line in enumerate(buffer.splitlines()):
        y_coord = i
        for i, tile in enumerate(line.strip()):
            x_coord = i
            new_tile = (Tile(tile, x_coord, y_coord))
            pipe_schematic[(x_coord, y_coord)] = new_tile
            if tile == 'S':
                starting_x_coord = x_coord
                starting_y_coord = y_coord
    
    return pipe_schematic, starting_x_coord, starting_y_coord


def test_solution_easy_connected_pipes():

    test_input = """    
                    .....
                    .S-7.
                    .|.|.
                    .L-J.
                    ..... 
                """
    
    assert find_furthest_tile(test_input) == 4


def test_solution_easy_all_pipes():
    
    test_input = """    
                    -L|F7
                    7S-7|
                    L|7||
                    -L-J|
                    L|-JF
                """
    

    assert find_furthest_tile(test_input) == 4


def test_solution_complex_connected_pipes():

    test_input = """    
                ..F7.
                .FJ|.
                SJ.L7
                |F--J
                LJ...
                """
    
    assert find_furthest_tile(test_input) == 8


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        buffer = file.read()
        print(find_furthest_tile(buffer))