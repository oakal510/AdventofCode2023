# advent of code day 6, part 1

def calculate_product_of_wins(buffer):

    values = buffer.splitlines()
    
    times = values[0].split()
    distances = values[1].split()
    times_and_distances = {int(x): int(y) for x, y in zip((times[1:]), distances[1:])}

    return win_counter(times_and_distances)


def win_counter(times_and_distances):

    win_count = 1

    for time in times_and_distances:

        game_win_count = 0
        
        for charge in range(time):
            time_remaining = time - charge
            
            if charge * time_remaining > times_and_distances[time]:
                game_win_count += 1

        win_count *= game_win_count

    return win_count


def test_solution():

    with open('test_input.txt', 'r') as file:
        buffer = file.read()
    
    assert calculate_product_of_wins(buffer) == 288


if __name__ == "__main__":

    with open('input.txt', 'r') as file:
        buffer = file.read()
        print(calculate_product_of_wins(buffer))