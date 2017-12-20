def solve_for_distance(x_distance, y_distance):
    x_steps = abs(x_distance) * 2
    y_steps = abs(y_distance - x_distance)
    return x_steps + y_steps

if __name__ == '__main__':
    child_path = []
    with open('input.txt') as file:
        child_path = file.readline().strip().split(',')

    modification = {
        'n': (0,1),
        'ne': (0.5,0.5),
        'se': (0.5,-0.5),
        's': (0, -1),
        'sw': (-0.5, -0.5),
        'nw': (-0.5, 0.5)
    }

    x_distance = 0
    y_distance = 0
    max_distance = 0

    for step in child_path:
        x_distance += modification[step][0]
        y_distance += modification[step][1]
        distance = solve_for_distance(x_distance, y_distance)
        if distance > max_distance:
            max_distance = distance

    print('part 1', solve_for_distance(x_distance, y_distance))
    print('part 2', max_distance)

