from CullIllegalMoves import cull_illegal_moves
from CullIllegalMoves import move_interpreter
from CullIllegalMoves import shucker
from CheckChecker import check_checker
from CheckChecker import king_finder
from BlackMoves import black_moves
from WhiteMoves import white_moves
from ChessVariables import squares
from ChessVariables import ssquares
from Square import Position


def threefold_checker(positions):
    positions.append(squares)
    if not len(positions) < 8:
        for position in positions:
            for pposition in positions:
                counter = 0
                while counter != 63:
                    if position[counter].occupied != pposition[counter].occupied\
                            or position[counter].piece_type != pposition[counter].piece_type\
                            or position[counter].piece_color != pposition[counter].piece_color:
                        break
                    counter += 1
    else:
        return False


def position_updater(move, positions):
    if move.find("K") == -1 and move.find("Q") == -1 and move.find("B") == -1 and move.find("N") == -1\
            and move.find("R") == -1 and move.find("O-O") == -1:
        positions = []
    else:
        positions.append(squares)


def game_over_checker(lmoves):
    if len(lmoves) == 0:
        return True
    else:
        return False


def move_asker(pmoves, message, game_log, ccolor):
    given_move = input(message)
    counter = 0
    for move in pmoves:
        if move == given_move:
            move_interpreter(shucker(move, ccolor, squares), squares)
            move_interpreter(shucker(move, ccolor, ssquares), ssquares)
            game_log.append(move)
            break
        else:
            counter += 1
    if counter == len(pmoves):
        move_asker(pmoves, "Invalid Move, Try Again: ", game_log, ccolor)


def play_chess():
    game_log = list()
    positions = list()
    game_on = True
    turn_color = "white"
    while game_on:
        if turn_color == "white":
            moves = cull_illegal_moves(white_moves(squares, game_log), turn_color, game_log)
            if game_over_checker(moves):
                king_squares = king_finder(squares)
                in_check = False
                for move in black_moves(squares, game_log):
                    if check_checker(move, king_squares):
                        in_check = True
                        break
                if in_check:
                    print("Checkmate!")
                    print(game_log)
                    break
                else:
                    print("Draw")
                    print(game_log)
                    break
            print(moves)
            move_asker(moves, "White To Move: ", game_log, turn_color)
            turn_color = "black"
        else:
            moves = cull_illegal_moves(black_moves(squares, game_log), turn_color, game_log)
            if game_over_checker(moves):
                king_squares = king_finder(squares)
                in_check = False
                for move in white_moves(squares, game_log):
                    if check_checker(move, king_squares):
                        in_check = True
                        break
                if in_check:
                    print("Checkmate!")
                    print(game_log)
                    break
                else:
                    print("Draw")
                    print(game_log)
                    break
            print(moves)
            move_asker(moves, "Black To Move: ", game_log, turn_color)
            turn_color = "white"


play_chess()
p1 = Position(squares)
