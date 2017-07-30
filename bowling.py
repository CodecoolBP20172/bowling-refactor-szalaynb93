def score(game):
    result = 0
    frame = 1
    normal_game_frames = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10  and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i+1])
            elif game[i] == 'X' or game[i] == 'x':
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last = get_value(game[i])
        if not normal_game_frames:
            frame += 1
        if normal_game_frames == True:
            normal_game_frames = False
        else:
            normal_game_frames = True
        if game[i] == 'X' or game[i] == 'x':
            normal_game_frames = True
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
