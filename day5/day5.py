if __name__ == '__main__':
    def format_jump(jump):
        jump = jump.strip()
        return int(jump)

    jumps = list(map(format_jump, open('input.txt').readlines()))
    current = 0
    steps = 0

    while current < len(jumps):
        modifier = jumps[current]
        jumps[current] += 1
        current += modifier
        steps += 1

    print('part 1:', steps)

    jumps = list(map(format_jump, open('input.txt').readlines()))
    current = 0
    steps = 0

    while current < len(jumps):
        modifier = jumps[current]
        if modifier >=  3:
            jumps[current] -= 1
        else:
            jumps[current] += 1

        current += modifier
        steps += 1

    print('part 2:', steps)

