# day 9, part 1

def sum_extrapolated_values(buffer):
    
    oasis_data = parse(buffer)

    for sequence in oasis_data:
        new_value = recursive_extrapolation(sequence, 0)

    return 0


# write a recursive function that extrapolates the values of the sequence
def recursive_extrapolation(sequence, new_value):
    
    if sum(sequence) > 0:

        for value in sequence:
            pass
                
    
    else:
        return new_value

            

def parse(data):

    oasis_data = []

    for line in data.splitlines():
        values = line.strip().split(" ")
        sequence_values = []
        print(values)
        for value in values:
            number_value = int(value)
            sequence_values.append(number_value)
        oasis_data.append(sequence_values)

    return oasis_data


def test_sum_extrapolated_values():

    buffer = """0 3 6 9 12 15
                1 3 6 10 15 21
                10 13 16 21 30 45 """
                
    assert sum_extrapolated_values(buffer) == 114


if __name__ == "__main__":

    with open('input.txt', 'r') as file:
        buffer = file.read()
        print(sum_extrapolated_values(buffer))