def recursive_programe_dive(test_connections, group):
    global connections, known_connections
    for connection in test_connections:
        if connection not in known_connections:
            known_connections.append(connection)
            group.append(connection)
            group = recursive_programe_dive(connections.get(connection), group)

    return group

if __name__ == '__main__':
    connections = {}
    with open('input.txt') as file:
        for line in file:
            bits = line.strip().replace(',', '').split(' ')
            connections[int(bits[0])] = list(map(int, bits[2:]))

    known_connections = [0]
    group = [0]
    group = recursive_programe_dive(connections.get(0), group)

    print('part 1', len(known_connections))

    groups = []
    groups.append(group)
    index = 0
    while len(known_connections) < len(connections):
        if index not in known_connections:
            known_connections.append(index)
            group = [index]
            group = recursive_programe_dive(connections.get(index), group)
            groups.append(group)

        index += 1

    print('part 2', len(groups))

