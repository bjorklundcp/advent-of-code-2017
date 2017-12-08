import itertools

if __name__ == '__main__':
    final_1 = 0
    final_2 = 0
    with open('input.txt') as file:
        for line in file:
            values = list(map(int, line.strip().split('\t')))
            final_1 += max(values) - min(values)
            for iter in itertools.combinations(values, 2):
                if max(iter) % min(iter) == 0:
                    final_2 += int(max(iter) / min(iter))

    print('part 1:', final_1)
    print('part 2:', final_2)

