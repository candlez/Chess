from ChessVariables import xcord_to_not
from ChessVariables import not_to_num
import math
from ChessVariables import what_turn


def black_moves(lsquares, game_log):
    bmoves = list()
    for item in lsquares:
        if item.piece_color == "black":
            # Pawn Moves
            if item.piece_type == "pawn":
                if item.y > 2:
                    if not lsquares[not_to_num[xcord_to_not[item.x] + str(item.y - 1)]].occupied:
                        bmoves.append(item.notcord + "-" + xcord_to_not[item.x] + str(item.y - 1))
                        if item.y == 7 and not lsquares[not_to_num[xcord_to_not[item.x] + str(item.y - 2)]].occupied:
                            bmoves.append(item.notcord + "-" + xcord_to_not[item.x] + str(item.y - 2))
                    if item.x < 8:
                        if lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y - 1)]].occupied and\
                                lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y - 1)]].piece_color\
                                != item.piece_color:
                            bmoves.append(item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y - 1))
                    if item.x > 1:
                        if lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y - 1)]].occupied and\
                                lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y - 1)]].piece_color\
                                != item.piece_color:
                            bmoves.append(item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y - 1))
                    if item.y == 4:
                        if item.x > 1:
                            if game_log[-1] == str(xcord_to_not[item.x - 1] + "2-" + xcord_to_not[item.x - 1] + "4"):
                                bmoves.append(item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y - 1) + " ep")
                        if item.x < 8:
                            if game_log[-1] == str(xcord_to_not[item.x + 1] + "2-" + xcord_to_not[item.x + 1] + "4"):
                                bmoves.append(item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y - 1) + " ep")
                else:
                    if not lsquares[not_to_num[xcord_to_not[item.x] + str(item.y - 1)]].occupied:
                        bmoves.append(item.notcord + "-" + xcord_to_not[item.x] + str(item.y - 1) + "=Q")
                        bmoves.append(item.notcord + "-" + xcord_to_not[item.x] + str(item.y - 1) + "=R")
                        bmoves.append(item.notcord + "-" + xcord_to_not[item.x] + str(item.y - 1) + "=B")
                        bmoves.append(item.notcord + "-" + xcord_to_not[item.x] + str(item.y - 1) + "=N")
                    if item.x < 8:
                        if lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y - 1)]].occupied and\
                                lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y - 1)]].piece_color\
                                != item.piece_color:
                            bmoves.append(item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y - 1) + "=Q")
                            bmoves.append(item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y - 1) + "=R")
                            bmoves.append(item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y - 1) + "=B")
                            bmoves.append(item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y - 1) + "=N")
                    if item.x > 1:
                        if lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y - 1)]].occupied and\
                                lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y - 1)]].piece_color\
                                != item.piece_color:
                            bmoves.append(item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y - 1) + "=Q")
                            bmoves.append(item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y - 1) + "=R")
                            bmoves.append(item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y - 1) + "=B")
                            bmoves.append(item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y - 1) + "=N")
            # Knight Moves
            if item.piece_type == "knight":
                if item.y <= 6:
                    if item.x <= 7:
                        if not lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y + 2)]].occupied:
                            bmoves.append("N" + item.notcord + "-" + xcord_to_not[item.x + 1] + str(item.y + 2))
                        elif lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y + 2)]].piece_color\
                                != item.piece_color:
                            bmoves.append("N" + item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y + 2))
                    if item.x >= 2:
                        if not lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y + 2)]].occupied:
                            bmoves.append("N" + item.notcord + "-" + xcord_to_not[item.x - 1] + str(item.y + 2))
                        elif lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y + 2)]].piece_color\
                                != item.piece_color:
                            bmoves.append("N" + item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y + 2))
                if item.y >= 3:
                    if item.x <= 7:
                        if not lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y - 2)]].occupied:
                            bmoves.append("N" + item.notcord + "-" + xcord_to_not[item.x + 1] + str(item.y - 2))
                        elif lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y - 2)]].piece_color\
                                != item.piece_color:
                            bmoves.append("N" + item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y - 2))
                    if item.x >= 2:
                        if not lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y - 2)]].occupied:
                            bmoves.append("N" + item.notcord + "-" + xcord_to_not[item.x - 1] + str(item.y - 2))
                        elif lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y - 2)]].piece_color\
                                != item.piece_color:
                            bmoves.append("N" + item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y - 2))
                if item.x <= 6:
                    if item.y <= 7:
                        if not lsquares[not_to_num[xcord_to_not[item.x + 2] + str(item.y + 1)]].occupied:
                            bmoves.append("N" + item.notcord + "-" + xcord_to_not[item.x + 2] + str(item.y + 1))
                        elif lsquares[not_to_num[xcord_to_not[item.x + 2] + str(item.y + 1)]].piece_color\
                                != item.piece_color:
                            bmoves.append("N" + item.notcord + "x" + xcord_to_not[item.x + 2] + str(item.y + 1))
                    if item.y >= 2:
                        if not lsquares[not_to_num[xcord_to_not[item.x + 2] + str(item.y - 1)]].occupied:
                            bmoves.append("N" + item.notcord + "-" + xcord_to_not[item.x + 2] + str(item.y - 1))
                        elif lsquares[not_to_num[xcord_to_not[item.x + 2] + str(item.y - 1)]].piece_color\
                                != item.piece_color:
                            bmoves.append("N" + item.notcord + "x" + xcord_to_not[item.x + 2] + str(item.y - 1))
                if item.x >= 3:
                    if item.y <= 7:
                        if not lsquares[not_to_num[xcord_to_not[item.x - 2] + str(item.y + 1)]].occupied:
                            bmoves.append("N" + item.notcord + "-" + xcord_to_not[item.x - 2] + str(item.y + 1))
                        elif lsquares[not_to_num[xcord_to_not[item.x - 2] + str(item.y + 1)]].piece_color\
                                != item.piece_color:
                            bmoves.append("N" + item.notcord + "x" + xcord_to_not[item.x - 2] + str(item.y + 1))
                    if item.y >= 2:
                        if not lsquares[not_to_num[xcord_to_not[item.x - 2] + str(item.y - 1)]].occupied:
                            bmoves.append("N" + item.notcord + "-" + xcord_to_not[item.x - 2] + str(item.y - 1))
                        elif lsquares[not_to_num[xcord_to_not[item.x - 2] + str(item.y - 1)]].piece_color\
                                != item.piece_color:
                            bmoves.append("N" + item.notcord + "x" + xcord_to_not[item.x - 2] + str(item.y - 1))
            # Bishop Moves
            if item.piece_type == "bishop":
                xmod = 1
                ymod = 1
                counter = 0
                while counter < 4:
                    x = item.x
                    y = item.y
                    not_blocked = True
                    while not_blocked:
                        if y != (4.5 + (3.5 * ymod)) and x != (4.5 + (3.5 * xmod)):
                            if not lsquares[not_to_num[xcord_to_not[x + xmod] + str(y + ymod)]].occupied:
                                bmoves.append("B" + item.notcord + "-" + xcord_to_not[x + xmod] + str(y + ymod))
                                x = x + xmod
                                y = y + ymod
                            else:
                                if lsquares[not_to_num[xcord_to_not[x + xmod] + str(y + ymod)]].piece_color\
                                        != item.piece_color:
                                    bmoves.append("B" + item.notcord + "x" + xcord_to_not[x + xmod] + str(y + ymod))
                                not_blocked = False
                        else:
                            not_blocked = False
                    counter = counter + 1
                    xmod = complex(0, 1) ** (2 * counter)
                    xmod = int(xmod.real)
                    ymod = -1 * (ymod * xmod)
            # Rook Moves
            if item.piece_type == "rook":
                xmod = 1
                ymod = 0
                counter = 0
                while counter < 4:
                    x = item.x
                    y = item.y
                    not_blocked = True
                    while not_blocked:
                        if y != (4.5 + (3.5 * ymod)) and x != (4.5 + (3.5 * xmod)):
                            if not lsquares[not_to_num[xcord_to_not[x + xmod] + str(y + ymod)]].occupied:
                                bmoves.append("R" + item.notcord + "-" + xcord_to_not[x + xmod] + str(y + ymod))
                                x = x + xmod
                                y = y + ymod
                            else:
                                if lsquares[not_to_num[xcord_to_not[x + xmod] + str(y + ymod)]].piece_color\
                                        != item.piece_color:
                                    bmoves.append("R" + item.notcord + "x" + xcord_to_not[x + xmod] + str(y + ymod))
                                not_blocked = False
                        else:
                            not_blocked = False
                    counter = counter + 1
                    xmod = int(math.cos(.5 * (math.pi * counter)))
                    ymod = int(math.sin(.5 * (math.pi * counter)))
            # Queen Moves: Diagonal
            if item.piece_type == "queen":
                xmod = 1
                ymod = 1
                counter = 0
                while counter < 4:
                    x = item.x
                    y = item.y
                    not_blocked = True
                    while not_blocked:
                        if y != (4.5 + (3.5 * ymod)) and x != (4.5 + (3.5 * xmod)):
                            if not lsquares[not_to_num[xcord_to_not[x + xmod] + str(y + ymod)]].occupied:
                                bmoves.append("Q" + item.notcord + "-" + xcord_to_not[x + xmod] + str(y + ymod))
                                x = x + xmod
                                y = y + ymod
                            else:
                                if lsquares[not_to_num[xcord_to_not[x + xmod] + str(y + ymod)]].piece_color \
                                        != item.piece_color:
                                    bmoves.append("Q" + item.notcord + "x" + xcord_to_not[x + xmod] + str(y + ymod))
                                not_blocked = False
                        else:
                            not_blocked = False
                    counter = counter + 1
                    xmod = complex(0, 1) ** (2 * counter)
                    xmod = int(xmod.real)
                    ymod = -1 * (ymod * xmod)
                # Queen Moves: Straight
                xmod = 1
                ymod = 0
                counter = 0
                while counter < 4:
                    x = item.x
                    y = item.y
                    not_blocked = True
                    while not_blocked:
                        if y != (4.5 + (3.5 * ymod)) and x != (4.5 + (3.5 * xmod)):
                            if not lsquares[not_to_num[xcord_to_not[x + xmod] + str(y + ymod)]].occupied:
                                bmoves.append("Q" + item.notcord + "-" + xcord_to_not[x + xmod] + str(y + ymod))
                                x = x + xmod
                                y = y + ymod
                            else:
                                if lsquares[not_to_num[xcord_to_not[x + xmod] + str(y + ymod)]].piece_color \
                                        != item.piece_color:
                                    bmoves.append("Q" + item.notcord + "x" + xcord_to_not[x + xmod] + str(y + ymod))
                                not_blocked = False
                        else:
                            not_blocked = False
                    counter = counter + 1
                    xmod = int(math.cos(.5 * (math.pi * counter)))
                    ymod = int(math.sin(.5 * (math.pi * counter)))
            # King Moves
            if item.piece_type == "king":
                if item.x < 8:
                    if item.y < 8:
                        if not lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y + 1)]].occupied:
                            bmoves.append("K" + item.notcord + "-" + xcord_to_not[item.x + 1] + str(item.y + 1))
                        elif lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y + 1)]].piece_color\
                                != item.piece_color:
                            bmoves.append("K" + item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y + 1))
                    if not lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y)]].occupied:
                        bmoves.append("K" + item.notcord + "-" + xcord_to_not[item.x + 1] + str(item.y))
                    elif lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y)]].piece_color != item.piece_color:
                        bmoves.append("K" + item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y))
                    if item.y > 1:
                        if not lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y - 1)]].occupied:
                            bmoves.append("K" + item.notcord + "-" + xcord_to_not[item.x + 1] + str(item.y - 1))
                        elif lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y - 1)]].piece_color\
                                != item.piece_color:
                            bmoves.append("K" + item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y - 1))
                if item.y < 8:
                    if not lsquares[not_to_num[xcord_to_not[item.x] + str(item.y + 1)]].occupied:
                        bmoves.append("K" + item.notcord + "-" + xcord_to_not[item.x] + str(item.y + 1))
                    elif lsquares[not_to_num[xcord_to_not[item.x] + str(item.y + 1)]].piece_color != item.piece_color:
                        bmoves.append("K" + item.notcord + "x" + xcord_to_not[item.x] + str(item.y + 1))
                if item.y > 1:
                    if not lsquares[not_to_num[xcord_to_not[item.x] + str(item.y - 1)]].occupied:
                        bmoves.append("K" + item.notcord + "-" + xcord_to_not[item.x] + str(item.y - 1))
                    elif lsquares[not_to_num[xcord_to_not[item.x] + str(item.y - 1)]].piece_color != item.piece_color:
                        bmoves.append("K" + item.notcord + "x" + xcord_to_not[item.x] + str(item.y - 1))
                if item.x > 1:
                    if item.y < 8:
                        if not lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y + 1)]].occupied:
                            bmoves.append("K" + item.notcord + "-" + xcord_to_not[item.x - 1] + str(item.y + 1))
                        elif lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y + 1)]].piece_color\
                                != item.piece_color:
                            bmoves.append("K" + item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y + 1))
                    if not lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y)]].occupied:
                        bmoves.append("K" + item.notcord + "-" + xcord_to_not[item.x - 1] + str(item.y))
                    elif lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y)]].piece_color != item.piece_color:
                        bmoves.append("K" + item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y))
                    if item.y > 1:
                        if not lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y - 1)]].occupied:
                            bmoves.append("K" + item.notcord + "-" + xcord_to_not[item.x - 1] + str(item.y - 1))
                        elif lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y - 1)]].piece_color\
                                != item.piece_color:
                            bmoves.append("K" + item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y - 1))
                if not lsquares[not_to_num["f8"]].occupied and not lsquares[not_to_num["g8"]].occupied:
                    counter = 0
                    for move in game_log:
                        if move.find("Ke8") != -1:
                            break
                        elif move.find("Rh8") != -1:
                            break
                        elif move.find("O-O") != -1 and what_turn(game_log, move) == "black":
                            break
                        elif move.find("O-O-O") != -1 and what_turn(game_log, move) == "black":
                            break
                        else:
                            counter += 1
                    if counter == len(game_log):
                        bmoves.append("O-O")
                if not lsquares[not_to_num["d8"]].occupied and not lsquares[not_to_num["c8"]].occupied\
                        and not lsquares[not_to_num["b8"]].occupied:
                    counter = 0
                    for move in game_log:
                        if move.find("Ke8") != -1:
                            break
                        elif move.find("Ra8") != -1:
                            break
                        elif move.find("O-O") != -1 and what_turn(game_log, move) == "black":
                            break
                        elif move.find("O-O-O") != -1 and what_turn(game_log, move) == "black":
                            break
                        else:
                            counter += 1
                    if counter == len(game_log):
                        bmoves.append("O-O-O")
    return bmoves
