if __name__ == '__main__':
    total_1 = 0
    total_2 = 0
    input = ''

    with open('input.txt') as file:
        input = file.read().strip()

    values = list(map(int, input))
    step = int(len(values)/2)

    for index, value in enumerate(values):
        if value == values[(index+1) % len(values)]:
            total_1 += value

        if value == values[(index + step) % len(values)]:
            total_2 += value

    print('part 1:', total_1)
    print('part 2:', total_2)

