import argparse
import itertools

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code - Day 2')
    parser.add_argument("file")
    args = parser.parse_args()

    final_1 = 0
    final_2 = 0
    with open(args.file) as file:
        for line in file:
            values = list(map(int, line.strip().split('\t')))
            final_1 += max(values) - min(values)
            for iter in itertools.combinations(values, 2):
                if max(iter) % min(iter) == 0:
                    final_2 += int(max(iter) / min(iter))

    print("part 1:", final_1)
    print("part 2:", final_2)

