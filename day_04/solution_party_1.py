# solution of Advent of Code day 4 part 1

def score_scratchers(file):
    
    points_sum = 0

    for line in file: 
        scratcher_data = line.split(":")
        winning_numbers, scratcher_numbers = scratcher_data[1].split("|")
        winning_numbers = [int(n) for n in winning_numbers.split(" ") if n != ""]
        scratcher_numbers = [int(n) for n in scratcher_numbers.split(" ") if n != ""]

        winning_card_counter = 0

        for winning_number in winning_numbers:
            if winning_number in scratcher_numbers:
                winning_card_counter += 1  

        points_sum += points_calculation(winning_card_counter)
    
    return points_sum


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

    assert score_scratchers(test_input) == 13


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        print(score_scratchers(file))