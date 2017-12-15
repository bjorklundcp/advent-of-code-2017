if __name__ == '__main__':
    def find_matching_state(state):
        found_matching_state = False
        counter = 0
        states = []
        states.append(list(state))

        while not found_matching_state:
            distribute_times = max(state)
            index_to_change = 0
            for index, value in enumerate(state):
                if value == max(state):
                    state[index] = 0
                    index_to_change = (index + 1) % len(state)
                    break

            while distribute_times > 0:
                state[index_to_change] += 1
                distribute_times -= 1
                index_to_change = (index_to_change + 1) % len(state)

            if state in states:
                found_matching_state = True
            else:
                states.append(list(state))

            counter += 1

        return state, counter

    values = []
    with open('input.txt') as file:
        for line in file:
            values = list(map(int, line.strip().split('\t')))

    part_1_state, part_1 = find_matching_state(values)

    print('part 1:', part_1)

    part_2_state, part_2 = find_matching_state(part_1_state)

    print('part 2:', part_2)

