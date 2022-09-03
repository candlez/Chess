def king_finder(lsquare):
    king_square_list = list()
    for item in lsquare:
        if item.piece_type == "king":
            king_square_list.append(item.notcord)
    return king_square_list


def check_checker(move, king_square_list):
    if len(move[0][0]) == 1:
        if move[1] == king_square_list[0]:
            return True
        elif move[1] == king_square_list[1]:
            return True
        else:
            return False
    elif len(move[0][0]) == 2:
        for item in move:
            if item[1] == king_square_list[0]:
                return True
            elif item[1] == king_square_list[1]:
                return True
            else:
                return False
