# advent of code day 6, part 2

def calculate_wins(buffer):

    values = buffer.splitlines()
    time = ''
    distance = ''
    
    for value in values[0].strip():
        if value.isnumeric():
            time += value
        print(time)

    for value in values[1].strip():
        if value.isnumeric():
            distance += value
        print(distance)

    return win_counter(time, distance)


def win_counter(time, distance):

    win_count = 0

    for charge in range(int(time)):
        time_remaining = int(time) - charge
            
        if charge * time_remaining > int(distance):
            win_count += 1

    return win_count


def test_solution():

    with open('test_input.txt', 'r') as file:
        buffer = file.read()
    
    assert calculate_wins(buffer) == 71503


if __name__ == "__main__":

    with open('input.txt', 'r') as file:
        buffer = file.read()
        print(calculate_wins(buffer))