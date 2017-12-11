if __name__ == '__main__':
    total = 0
    part_1 = 0
    part_2 = 0
    with open('input.txt') as file:
        for passphrase in file:
            uniques = set(passphrase.split())
            if(len(uniques) < len(passphrase.split())):
                part_1 += 1
            else:
                for unique in uniques:
                    do_break = False
                    for compare in uniques:
                        if compare != unique and sorted(compare) == sorted(unique):
                            part_2 += 1
                            do_break = True
                            break
                    if do_break:
                        break

            total += 1

    print('part 1:', total - part_1)
    print('part 2:', abs(total - part_2 - part_1))

