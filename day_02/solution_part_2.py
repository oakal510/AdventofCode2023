def game_analysis(data_list):
    
    game_data_list = data_list.split(";")

    cube_dict = {}

    for game in game_data_list:
        cube_showings = game.split(",")
        for show in cube_showings:
            value, color = show.strip().split(" ")
            # update the value of dictionary key if the value is lower than a new value
            if color in cube_dict:
                if int(value) > cube_dict[color]:
                    cube_dict[color] = int(value)
            else:
                cube_dict[color] = int(value)
    
    cube_powers = 1
    for value in cube_dict.values():
        cube_powers *= value

    return cube_powers


def fewest_cubes_calculation(file):

    cube_powers_sum = 0

    for i, line in enumerate(file):
        game_data = line.split(":")
        cube_powers_sum += game_analysis(game_data[1]) 
    
    return cube_powers_sum


# pytest unit test
def test_solution():
    test_input = """ Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
                Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
                Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
                Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
                Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green """.split("\n")

    assert fewest_cubes_calculation(test_input) == 2286


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        print(fewest_cubes_calculation(file))