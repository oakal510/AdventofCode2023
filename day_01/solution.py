""" Solution for Advent of Code Day 1"""

def spelled_lines(line, digit=0):
    
    spelled_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    if digit == 0:
        
        spelled_digit_dict = {}

        for spelled_digit in spelled_digits:
            if spelled_digit in line: 
                spelled_digit_dict[spelled_digit] = line.index(spelled_digit)
            
        if spelled_digit_dict:
            # sort by lowest key value in dict
            first_spelled_digit = sorted(spelled_digit_dict.items(), key=lambda x: x[1])[0][0]
            line = line.replace(first_spelled_digit, str(spelled_digits.index(first_spelled_digit) + 1))

    else:
        
        reverse_spelled_digit_dict = {}

        for spelled_digit in spelled_digits:
            if spelled_digit in line: 
                reverse_spelled_digit_dict[spelled_digit] = line.rindex(spelled_digit)
    
        if reverse_spelled_digit_dict:
            # sort by highest key value in dict
            first_spelled_digit = sorted(reverse_spelled_digit_dict.items(), key=lambda x: x[1])[-1][0]
            line = line.replace(first_spelled_digit, str(spelled_digits.index(first_spelled_digit) + 1))

    return line    


def fwd_calib_value(line):

    digit = ""

    for i in spelled_lines(line):
        if i.isdigit():
            digit += (i)
            break

    return digit


def bwd_calib_value(line, digit):

    line = spelled_lines(line, digit)
    line_reverse = line[::-1]

    for i in line_reverse:
        if i.isdigit():
            digit += (i)
            break
    return digit


calib_sum = 0

with open("input.txt", "r") as calib_doc:
    for line in calib_doc:
        calib_sum += int(bwd_calib_value(line, fwd_calib_value(line)))

print(calib_sum)