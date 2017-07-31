def score(game):
    result = 0
    frame = 1
    SPARE = '/'
    STRIKE = 'X'
    in_first_half = True
    for roll in range(len(game)):
        if game[roll] == '/':
            result += 10 - last
        else:
            result += get_value(game[roll])
        if frame < 10 and get_value(game[roll]) == 10:
            if game[roll] == '/':
                result += get_value(game[roll+1])
            elif game[roll] == 'X' or game[roll] == 'x':
                result += get_value(game[roll+1])
                if game[roll+2] == '/':
                    result += 10 - get_value(game[roll+1])
                else:
                    result += get_value(game[roll+2])
        last = get_value(game[roll])
        if not in_first_half:
            frame += 1
        in_first_half = not in_first_half
        if game[roll].upper() == 'X':
            in_first_half = True
            frame += 1
    return result

def get_value(char):
    if char >= '1' and char <= '9':
        return int(char)
    elif char == 'X' or char == 'x':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
