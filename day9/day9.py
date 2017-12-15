if __name__ == '__main__':
    def sanitize_nots(river):
        index = 0
        while index < len(river):
            if river[index] == '!':
                chop_distance = 2
                while river[index + chop_distance] == '!':
                    chop_distance += 2
                river = river[:index] + river[index + chop_distance:]
            index += 1

        return river

    def remove_garbage(river):
        index = 0
        chop_start = 0
        number_of_chars_removed = 0
        while index < len(river):
            if river[index] == '<' and chop_start == 0:
                chop_start = index
                index += 1
            elif river[index] == '>' and chop_start > 0:
                river = river[:chop_start] + river[index + 1:]
                number_of_chars_removed += (index - chop_start) - 1
                index = index - chop_start
                chop_start = 0
            else:
                index += 1

        print('part 2', number_of_chars_removed)
        return river

    river = ''
    with open('input.txt') as file:
        river = file.readline()

    river = sanitize_nots(river)
    river = remove_garbage(river)
    total_score = 0
    index = 0
    group_index_stack = []
    while index < len(river):
        if river[index] == '{':
            group_index_stack.append(index)
        elif river[index] == '}':
            total_score += len(group_index_stack)
            group_index_stack.pop()
        index += 1

    print(river.strip())
    print('part 1', total_score)
