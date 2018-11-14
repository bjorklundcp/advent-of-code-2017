import copy

def cycle_scanners(firewall):
    for key, value in firewall.items():
        if value.get('range') == value.get('location') + 1 or value.get('location') == 0:
            value['move_down'] = not value.get('move_down')

        if value.get('move_down'):
            value['location'] += 1
        else:
            value['location'] -= 1

    return firewall

def attempt_run(firewall, break_early = False):
    severity = 0
    for current_pos in range(0, max(firewall.keys()) + 1):
        if firewall.get(current_pos):
            if firewall.get(current_pos).get('location') == 0:
                severity += (current_pos * firewall.get(current_pos).get('range'))
                if break_early:
                    severity = -1
                    break

        firewall = cycle_scanners(firewall)

    return severity

if __name__ == '__main__':
    with open('input.txt') as file:
        firewall = {}
        for line in file:
            depth, in_range = line.strip().split()
            firewall[int(depth.replace(':', ''))] = {
                'range': int(in_range),
                'location': 0,
                'move_down': False
            }

        # firewall = {
        #     0: {
        #         'range': 3,
        #         'location': 0,
        #         'move_down': False
        #     },
        #     1: {
        #         'range': 2,
        #         'location': 0,
        #         'move_down': False
        #     },
        #     4: {
        #         'range': 4,
        #         'location': 0,
        #         'move_down': False
        #     },
        #     6: {
        #         'range': 4,
        #         'location': 0,
        #         'move_down': False
        #     }
        # }
        # print('part 1', attempt_run(copy.deepcopy(firewall)))

        delay = 0
        not_done = True

        # for n in range(0, 3966414):
        #     print(n)
        #     firewall = cycle_scanners(firewall)

        # print(attempt_run(firewall, True))

        while not_done:
            if attempt_run(copy.deepcopy(firewall), True) == 0:
                not_done = False
            else:
                delay += 1
                firewall = cycle_scanners(firewall)

        print('part 2', delay)


