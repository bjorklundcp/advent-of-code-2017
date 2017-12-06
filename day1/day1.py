import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code - Day 1')
    parser.add_argument("input")
    args = parser.parse_args()

    values = list(map(int, args.input))
    total = 0

    for index, value in enumerate(values[:-1]):
        if value == values[index+1]:
            total += value

    if values[0] == values[-1]:
        total += values[0]

    print(total)

