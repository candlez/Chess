from CheckChecker import check_checker
from CheckChecker import king_finder
from BlackMoves import black_moves
from WhiteMoves import white_moves
from ChessVariables import squares
from ChessVariables import ssquares
from ChessVariables import not_to_num


def castle_culler(cmove, ccolor, game_log):
    if cmove == "O-O":
        if ccolor == "white":
            bmoves = black_moves(squares, game_log)
            for move in bmoves:
                if move.find("f1") == 4 or move.find("xf1") == 2:
                    return True
                elif move.find("e1") == 4 or move.find("xe1") == 2:
                    return True
            return False
        else:
            wmoves = white_moves(squares, game_log)
            for move in wmoves:
                if move.find("f8") == 4 or move.find("xf8") == 2:
                    return True
                elif move.find("e8") == 4 or move.find("xe8") == 2:
                    return True
            return False
    elif cmove == "O-O-O":
        if ccolor == "white":
            bmoves = black_moves(squares, game_log)
            for move in bmoves:
                if move.find("d1") == 4 or move.find("xd1") == 2:
                    return True
                elif move.find("e1") == 4 or move.find("xe1") == 2:
                    return True
            return False
        else:
            wmoves = white_moves(squares, game_log)
            for move in wmoves:
                if move.find("d8") == 4 or move.find("xd8") == 2:
                    return True
                elif move.find("e8") == 4 or move.find("xe8") == 2:
                    return True
            return False
    else:
        return False


def promotion(start_square, new_piece_type, lsquare):
    if new_piece_type == "Q":
        lsquare[not_to_num[start_square]].piece_type = "queen"
    elif new_piece_type == "R":
        lsquare[not_to_num[start_square]].piece_type = "rook"
    elif new_piece_type == "B":
        lsquare[not_to_num[start_square]].piece_type = "bishop"
    elif new_piece_type == "N":
        lsquare[not_to_num[start_square]].piece_type = "knight"


def shucker(move, ccolor, lsquare):
    if ccolor == "white":
        if move == "O-O-O":
            return [["e1", "c1"], ["a1", "d1"]]
        if move == "O-O":
            return [["e1", "g1"], ["h1", "f1"]]
    else:
        if move == "O-O-O":
            return [["e8", "c8"], ["a8", "d8"]]
        if move == "O-O":
            return [["e8", "g8"], ["h8", "f8"]]
    if move.find("-") != -1:
        move = move.split("-")
    elif move.find("x") != -1:
        move = move.split("x")
    if len(move[0]) == 3:
        move[0] = move[0].lstrip("KQRBN")
    if move[1].find("ep") != -1:
        move[1] = move[1].rstrip("12345678 ep")
        if ccolor == "white":
            return [[move[0], str(move[1] + "5")], [str(move[1]) + "5", str(move[1] + "6")]]
        else:
            return [[move[0], str(move[1] + "4")], [str(move[1] + "4"), str(move[1] + "3")]]
    if move[1].find("=") != -1:
        move[1] = move[1].split("=")
        promotion(move[0], move[1][1], lsquare)
        move[1] = move[1][0]
    return move


def move_interpreter(move, lsquare):
    # print(move)
    if len(move[0][0]) == 1:
        lsquare[not_to_num[move[1]]].occupied = lsquare[not_to_num[move[0]]].occupied
        lsquare[not_to_num[move[1]]].piece_color = lsquare[not_to_num[move[0]]].piece_color
        lsquare[not_to_num[move[1]]].piece_type = lsquare[not_to_num[move[0]]].piece_type
        lsquare[not_to_num[move[0]]].occupied = False
        lsquare[not_to_num[move[0]]].piece_color = "none"
        lsquare[not_to_num[move[0]]].piece_type = "none"
    elif len(move[0][0]) == 2:
        for item in move:
            lsquare[not_to_num[item[1]]].occupied = lsquare[not_to_num[item[0]]].occupied
            lsquare[not_to_num[item[1]]].piece_color = lsquare[not_to_num[item[0]]].piece_color
            lsquare[not_to_num[item[1]]].piece_type = lsquare[not_to_num[item[0]]].piece_type
            lsquare[not_to_num[item[0]]].occupied = False
            lsquare[not_to_num[item[0]]].piece_color = "none"
            lsquare[not_to_num[item[0]]].piece_type = "none"


def cull_illegal_moves(moves, ccolor, game_log):
    lmoves = moves
    rmoves = list()
    for cmove in lmoves:
        if ccolor == "white":
            if castle_culler(cmove, ccolor, game_log):
                rmoves.append(cmove)
            else:
                move_interpreter(shucker(cmove, "white", ssquares), ssquares)
                king_squares = king_finder(ssquares)
                bmoves = black_moves(ssquares, game_log)
                for mmove in bmoves:
                    if check_checker(shucker(mmove, "black", ssquares), king_squares):
                        rmoves.append(cmove)
                        break
        else:
            if castle_culler(cmove, ccolor, game_log):
                rmoves.append(cmove)
            else:
                move_interpreter(shucker(cmove, "black", ssquares), ssquares)
                king_squares = king_finder(ssquares)
                wmoves = white_moves(ssquares, game_log)
                for mmove in wmoves:
                    if check_checker(shucker(mmove, "white", ssquares), king_squares):
                        rmoves.append(cmove)
                        break
        for item in ssquares:
            item.occupied = squares[not_to_num[item.notcord]].occupied
            item.piece_color = squares[not_to_num[item.notcord]].piece_color
            item.piece_type = squares[not_to_num[item.notcord]].piece_type
    for rmove in rmoves:
        lmoves.remove(rmove)
    return lmoves
