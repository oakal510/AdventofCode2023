# solution of Advent of Code day 4 part 2

def score_scratchers(buffer):

    game_IDs = len(buffer)

    card_copies_dict = {game_ID + 1: 1 for game_ID in range(game_IDs)}

    for line in buffer: 
        scratcher_data = line.split(":")
        game_ID = int(scratcher_data[0].split()[1])
        winning_numbers, scratcher_numbers = scratcher_data[1].split("|")
        winning_numbers = [int(n) for n in winning_numbers.split(" ") if n != ""]
        scratcher_numbers = [int(n) for n in scratcher_numbers.split(" ") if n != ""]


        count = 1
            
        for winning_number in winning_numbers:
            if winning_number in scratcher_numbers:
                card_copies_dict[game_ID + count] += card_copies_dict[game_ID]
                count += 1
    
    return sum(card_copies_dict.values())


def points_calculation(winning_card_counter):
    if winning_card_counter == 0:
        return 0
    else:
        return 2 ** (winning_card_counter - 1)


# pytest unit test
def test_solution():
    test_input = """ Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
                Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
                Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
                Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
                Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
                Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split("\n")

    assert score_scratchers(test_input) == 30


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        buffer = file.read().split("\n")
        print(score_scratchers(buffer))