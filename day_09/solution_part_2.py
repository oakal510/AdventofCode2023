# day 9, part 2

def sum_extrapolated_values(buffer):
    
    oasis_data = parse(buffer)

    sum_of_new_values = 0

    for sequence in oasis_data:
        new_value = recursive_extrapolation(sequence, sequence[0], 0)
        sum_of_new_values += new_value

    return sum_of_new_values


# recursive function that extrapolates the values of the sequence
def recursive_extrapolation(sequence, start_value, new_value):
    
    if set(sequence) != {0}:

        difference_list = []

        for i, value in enumerate(sequence):
            if i < len(sequence) - 1:
                difference_list.append(sequence[i+1] - value)

        new_value =  start_value - recursive_extrapolation(difference_list, difference_list[0], new_value)
        
        return new_value
    
    else:
        return new_value
            

def parse(data):

    oasis_data = []

    for line in data.splitlines():
        values = line.strip().split(" ")
        sequence_values = []
        for value in values:
            number_value = int(value)
            sequence_values.append(number_value)
        oasis_data.append(sequence_values)

    return oasis_data


def test_sum_extrapolated_values():

    buffer = """0 3 6 9 12 15
                1 3 6 10 15 21
                10 13 16 21 30 45 """
                
    assert sum_extrapolated_values(buffer) == 2


if __name__ == "__main__":

    with open('input.txt', 'r') as file:
        buffer = file.read()
        print(sum_extrapolated_values(buffer))