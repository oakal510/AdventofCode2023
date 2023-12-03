# solution of Advent of Code day 2

def cube_comparison(value, color):
    if color == "red":
        if int(value) > 12:
            return False
    elif color == "green":
        if int(value) > 13:
            return False
    elif color == "blue":
        if int(value) > 14:
            return False

    return True
    

def game_analysis(game_ID, data_list):
    
    game_data_list = data_list.split(";")

    for game in game_data_list:
        cube_showings = game.split(",")
        for show in cube_showings:
            value, color = show.strip().split(" ")
            if not cube_comparison(value, color):
                return 0

    return game_ID


def validate_games(file):
    
    game_ID_sum = 0

    for i, line in enumerate(file):
        game_ID = i + 1
        game_data = line.split(":")
        game_ID_sum += game_analysis(game_ID, game_data[1]) 
    
    return game_ID_sum
     
        
# pytest unit test
def test_solution():
    test_input = """ Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green """.split("\n")

    assert validate_games(test_input) == 8


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        print(validate_games(file))


