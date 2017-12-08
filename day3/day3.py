import math
import argparse

def part_1(target):
    outer_ring_corner = target
    side_length = 0
    while True:
        side_length = math.sqrt(outer_ring_corner)
        if side_length.is_integer() and side_length % 2 != 0:
            side_length = int(side_length)
            break;

        outer_ring_corner += 1

    placement_not_found = True
    max_steps_needed = side_length - 1
    half_side_step = (math.floor(side_length / 2))
    side_middle = outer_ring_corner - half_side_step
    corner_1 = side_middle + half_side_step
    corner_2 = side_middle - half_side_step

    while placement_not_found:
        # Left or on the middle
        if target >= corner_2 and target <= corner_1:
            steps_needed_to_middle = abs(target - side_middle)
            steps_difference = abs(steps_needed_to_middle - half_side_step)
            placement_not_found = False

        # switch side
        corner_1 -= side_length - 1
        corner_2 -= side_length - 1
        side_middle -= side_length - 1

    # The result is the difference between the worse case scenario (the corner)
    # and how far from the corer we are in regards to the middle
    return (max_steps_needed - steps_difference)

def part_2(target):
    spiral_matrix = {(0,0): 1}
    direction_to_left = {'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S'}
    direction_to_coords = {
        'N': (0, 1),
        'NE': (1, 1),
        'E': (1, 0),
        'SE': (1, -1),
        'S': (0, -1),
        'SW': (-1, -1),
        'W': (-1, 0),
        'NW': (-1, 1)
    }

    def sum_surroundings(location):
        total = 0;
        for direction, change in direction_to_coords.items():
            coord = (location[0] + change[0], location[1] + change[1])
            total += spiral_matrix.get(coord, 0)

        return total

    def get_coord_to_left(current_location, current_direction):
        coord_to_left_mod = direction_to_coords.get(direction_to_left.get(current_direction))
        return (current_location[0] + coord_to_left_mod[0], current_location[1] + coord_to_left_mod[1])

    value = 1
    current_location = (0,0)
    current_direction = 'S'

    while value <= target:
        coord_to_left = get_coord_to_left(current_location, current_direction)
        # There is something to our left so we cannot turn left
        if spiral_matrix.get(coord_to_left):
            current_direction_mod = direction_to_coords.get(current_direction)
            current_location = (current_location[0] + current_direction_mod[0], current_location[1] + current_direction_mod[1])
            value = sum_surroundings(current_location)
            spiral_matrix[current_location] = value
        # Nothing to the left so we should turn
        else:
            current_location = coord_to_left
            value = sum_surroundings(coord_to_left)
            spiral_matrix[current_location] = value
            current_direction = direction_to_left.get(current_direction)

    return value

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code - Day 3')
    parser.add_argument('target', type=int)
    args = parser.parse_args()

    part_1_result = part_1(args.target)
    part_2_result = part_2(args.target)
    print('part 1:', part_1_result)
    print('part 2:', part_2_result)

