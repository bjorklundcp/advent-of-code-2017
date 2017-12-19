from functools import reduce

def do_run(lengths, values, current_position, skip_size):
    for length in lengths:
        # get our sub list
        sub = []
        for index in range(0, length):
            sub.append(values[(current_position + index) % len(values)])
        # flip it and reverse it
        rev = list(reversed(sub))
        # swap values in
        for index, value in enumerate(rev):
            values[(current_position + index) % len(values)] = value
        # move our current position
        step_distance = length + skip_size
        current_position = (current_position + step_distance) % len(values)

        # increment skip
        skip_size += 1

    return values, current_position, skip_size

if __name__ == '__main__':
    lengths_part_1 = []
    lengths_part_2 = []
    with open('input.txt') as file:
        input_string = file.readline().strip()
        lengths_part_1 = list(map(int, input_string.split(',')))
        lengths_part_2 = list(map(ord, input_string))
        lengths_part_2.extend([17, 31, 73, 47, 23])

    values = do_run(lengths_part_1, list(range(0,256)), 0, 0)[0]
    print('part 1', (values[0] * values[1]))

    values = list(range(0,256))
    current_position = 0
    skip_size = 0
    for iteration in range(0, 64):
        values, current_position, skip_size = do_run(lengths_part_2, values, current_position, skip_size)

    dense_hash = []
    temp = []
    index = 0
    while len(dense_hash) < 16:
        if len(temp) == 16:
            dense_hash.append(reduce((lambda x, y: x^y), temp))
            temp = []
        else:
            temp.append(values[index])
            index += 1

    hex_string = ''
    for each in dense_hash:
        hex_string += hex(each)[2:].zfill(2)

    print('part 2', hex_string)


