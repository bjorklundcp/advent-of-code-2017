if __name__ == '__main__':
    largest_value_ever = 0
    registers = {}
    with open('input.txt') as file:
        for line in file:
            bits = line.split()
            if not registers.get(bits[0]):
                registers[bits[0]] = 0
            if not registers.get(bits[4]):
                registers[bits[4]] = 0
            eval_string = '{} {} {}'.format(int(registers.get(bits[4])), bits[5], int(bits[6]))
            if(eval(eval_string)):
                modifier = int(bits[2])
                if bits[1] == 'dec':
                    modifier = -modifier
                registers[bits[0]] += modifier
                if registers[bits[0]] > largest_value_ever:
                    largest_value_ever = registers[bits[0]]

    largest_value = 0
    for register, value in registers.items():
        if value > largest_value:
            largest_value = value

    print('part 1:', largest_value)
    print('part 2:', largest_value_ever)

