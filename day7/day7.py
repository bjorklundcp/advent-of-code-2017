import sys

if __name__ == '__main__':
    def recursive_dive(node):
        children_weight = 0
        for child in nodes.get(node).get('connections'):
            if nodes.get(child):
                nodes.get(child)['connections_weight'] = recursive_dive(child)
                weights = []
                connection_weights = {}
                for connection in nodes.get(child).get('connections'):
                    if nodes.get(connection):
                        node_weight = nodes.get(connection).get('weight') + nodes.get(connection).get('connections_weight')
                        weights.append(node_weight)
                        connection_weights[connection] = node_weight
                    else:
                        weights.append(ends.get(connection))
                        connection_weights[connection] = ends.get(connection)

                unique_weights = set(weights)
                if(len(unique_weights) == 2):
                    unbalanced_weight = 0
                    balanced_weight = 0
                    for unique_weight in unique_weights:
                        if weights.count(unique_weight) == 1:
                            unbalanced_weight = unique_weight
                        else:
                            balanced_weight = unique_weight

                    for conn, weight in connection_weights.items():
                        if weight == unbalanced_weight:
                            difference = unbalanced_weight - balanced_weight
                            if nodes.get(conn).get('weight') > difference:
                                nodes.get(conn)['weight'] -= difference
                            else:
                                nodes.get(conn)['weight'] += difference
                            sys.exit()

                children_weight += nodes.get(child)['connections_weight'] + nodes.get(child)['weight']
            else:
                children_weight += ends.get(child)

        return children_weight

    bottom_program = ''
    nodes = {}
    ends = {}
    possible_parents = []
    parent_connections = []
    with open('input.txt') as file:
        for line in file:
            if '->' in line:
                bits = line.strip().replace(',', '').replace('(', '').replace(')', '').split(' ')
                possible_parents.append(bits[0])
                parent_connections.extend(bits[3:])
                nodes[bits[0]] = {
                    'weight': int(bits[1]),
                    'connections': bits[3:],
                    'connections_weight': 0
                }
            else:
                bits = line.strip().replace(',', '').replace('(', '').replace(')', '').split(' ')
                ends[bits[0]] = int(bits[1])

    for possible_parent in possible_parents:
        if possible_parent not in parent_connections:
            bottom_program = possible_parent
            break

    print('part 1:', bottom_program)

    recursive_dive(bottom_program)

