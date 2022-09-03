from ChessVariables import xcord_to_not
from ChessVariables import not_to_num
import math
from ChessVariables import what_turn


def white_moves(lsquares, game_log):
    wmoves = list()
    for item in lsquares:
        if item.piece_color == "white":
            # Pawn Moves
            if item.piece_type == "pawn":
                if item.y < 7:
                    if not lsquares[not_to_num[xcord_to_not[item.x] + str(item.y + 1)]].occupied:
                        wmoves.append(item.notcord + "-" + xcord_to_not[item.x] + str(item.y + 1))
                        if item.y == 2 and not lsquares[not_to_num[xcord_to_not[item.x] + str(item.y + 2)]].occupied:
                            wmoves.append(item.notcord + "-" + xcord_to_not[item.x] + str(item.y + 2))
                    if item.x < 8:
                        if lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y + 1)]].occupied and\
                                lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y + 1)]].piece_color\
                                != item.piece_color:
                            wmoves.append(item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y + 1))
                    if item.x > 1:
                        if lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y + 1)]].occupied and\
                                lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y + 1)]].piece_color\
                                != item.piece_color:
                            wmoves.append(item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y + 1))
                    if item.y == 5:
                        if item.x > 1:
                            if game_log[-1] == str(xcord_to_not[item.x - 1] + "7-" + xcord_to_not[item.x - 1] + "5"):
                                wmoves.append(item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y + 1) + " ep")
                        if item.x < 8:
                            if game_log[-1] == str(xcord_to_not[item.x + 1] + "7-" + xcord_to_not[item.x + 1] + "5"):
                                wmoves.append(item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y + 1) + " ep")
                else:
                    if not lsquares[not_to_num[xcord_to_not[item.x] + str(item.y + 1)]].occupied:
                        wmoves.append(item.notcord + "-" + xcord_to_not[item.x] + str(item.y + 1) + "=Q")
                        wmoves.append(item.notcord + "-" + xcord_to_not[item.x] + str(item.y + 1) + "=R")
                        wmoves.append(item.notcord + "-" + xcord_to_not[item.x] + str(item.y + 1) + "=B")
                        wmoves.append(item.notcord + "-" + xcord_to_not[item.x] + str(item.y + 1) + "=N")
                    if item.x < 8:
                        if lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y + 1)]].occupied and\
                                lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y + 1)]].piece_color\
                                != item.piece_color:
                            wmoves.append(item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y + 1) + "=Q")
                            wmoves.append(item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y + 1) + "=R")
                            wmoves.append(item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y + 1) + "=B")
                            wmoves.append(item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y + 1) + "=N")
                    if item.x > 1:
                        if lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y + 1)]].occupied and\
                                lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y + 1)]].piece_color\
                                != item.piece_color:
                            wmoves.append(item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y + 1) + "=Q")
                            wmoves.append(item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y + 1) + "=R")
                            wmoves.append(item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y + 1) + "=B")
                            wmoves.append(item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y + 1) + "=N")
            # Knight Moves
            if item.piece_type == "knight":
                if item.y <= 6:
                    if item.x <= 7:
                        if not lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y + 2)]].occupied:
                            wmoves.append("N" + item.notcord + "-" + xcord_to_not[item.x + 1] + str(item.y + 2))
                        elif lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y + 2)]].piece_color\
                                != item.piece_color:
                            wmoves.append("N" + item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y + 2))
                    if item.x >= 2:
                        if not lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y + 2)]].occupied:
                            wmoves.append("N" + item.notcord + "-" + xcord_to_not[item.x - 1] + str(item.y + 2))
                        elif lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y + 2)]].piece_color\
                                != item.piece_color:
                            wmoves.append("N" + item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y + 2))
                if item.y >= 3:
                    if item.x <= 7:
                        if not lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y - 2)]].occupied:
                            wmoves.append("N" + item.notcord + "-" + xcord_to_not[item.x + 1] + str(item.y - 2))
                        elif lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y - 2)]].piece_color\
                                != item.piece_color:
                            wmoves.append("N" + item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y - 2))
                    if item.x >= 2:
                        if not lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y - 2)]].occupied:
                            wmoves.append("N" + item.notcord + "-" + xcord_to_not[item.x - 1] + str(item.y - 2))
                        elif lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y - 2)]].piece_color\
                                != item.piece_color:
                            wmoves.append("N" + item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y - 2))
                if item.x <= 6:
                    if item.y <= 7:
                        if not lsquares[not_to_num[xcord_to_not[item.x + 2] + str(item.y + 1)]].occupied:
                            wmoves.append("N" + item.notcord + "-" + xcord_to_not[item.x + 2] + str(item.y + 1))
                        elif lsquares[not_to_num[xcord_to_not[item.x + 2] + str(item.y + 1)]].piece_color\
                                != item.piece_color:
                            wmoves.append("N" + item.notcord + "x" + xcord_to_not[item.x + 2] + str(item.y + 1))
                    if item.y >= 2:
                        if not lsquares[not_to_num[xcord_to_not[item.x + 2] + str(item.y - 1)]].occupied:
                            wmoves.append("N" + item.notcord + "-" + xcord_to_not[item.x + 2] + str(item.y - 1))
                        elif lsquares[not_to_num[xcord_to_not[item.x + 2] + str(item.y - 1)]].piece_color\
                                != item.piece_color:
                            wmoves.append("N" + item.notcord + "x" + xcord_to_not[item.x + 2] + str(item.y - 1))
                if item.x >= 3:
                    if item.y <= 7:
                        if not lsquares[not_to_num[xcord_to_not[item.x - 2] + str(item.y + 1)]].occupied:
                            wmoves.append("N" + item.notcord + "-" + xcord_to_not[item.x - 2] + str(item.y + 1))
                        elif lsquares[not_to_num[xcord_to_not[item.x - 2] + str(item.y + 1)]].piece_color\
                                != item.piece_color:
                            wmoves.append("N" + item.notcord + "x" + xcord_to_not[item.x - 2] + str(item.y + 1))
                    if item.y >= 2:
                        if not lsquares[not_to_num[xcord_to_not[item.x - 2] + str(item.y - 1)]].occupied:
                            wmoves.append("N" + item.notcord + "-" + xcord_to_not[item.x - 2] + str(item.y - 1))
                        elif lsquares[not_to_num[xcord_to_not[item.x - 2] + str(item.y - 1)]].piece_color\
                                != item.piece_color:
                            wmoves.append("N" + item.notcord + "x" + xcord_to_not[item.x - 2] + str(item.y - 1))
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
                                wmoves.append("B" + item.notcord + "-" + xcord_to_not[x + xmod] + str(y + ymod))
                                x = x + xmod
                                y = y + ymod
                            else:
                                if lsquares[not_to_num[xcord_to_not[x + xmod] + str(y + ymod)]].piece_color\
                                        != item.piece_color:
                                    wmoves.append("B" + item.notcord + "x" + xcord_to_not[x + xmod] + str(y + ymod))
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
                                wmoves.append("R" + item.notcord + "-" + xcord_to_not[x + xmod] + str(y + ymod))
                                x = x + xmod
                                y = y + ymod
                            else:
                                if lsquares[not_to_num[xcord_to_not[x + xmod] + str(y + ymod)]].piece_color\
                                        != item.piece_color:
                                    wmoves.append("R" + item.notcord + "x" + xcord_to_not[x + xmod] + str(y + ymod))
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
                                wmoves.append("Q" + item.notcord + "-" + xcord_to_not[x + xmod] + str(y + ymod))
                                x = x + xmod
                                y = y + ymod
                            else:
                                if lsquares[not_to_num[xcord_to_not[x + xmod] + str(y + ymod)]].piece_color \
                                        != item.piece_color:
                                    wmoves.append("Q" + item.notcord + "x" + xcord_to_not[x + xmod] + str(y + ymod))
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
                                wmoves.append("Q" + item.notcord + "-" + xcord_to_not[x + xmod] + str(y + ymod))
                                x = x + xmod
                                y = y + ymod
                            else:
                                if lsquares[not_to_num[xcord_to_not[x + xmod] + str(y + ymod)]].piece_color \
                                        != item.piece_color:
                                    wmoves.append("Q" + item.notcord + "x" + xcord_to_not[x + xmod] + str(y + ymod))
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
                            wmoves.append("K" + item.notcord + "-" + xcord_to_not[item.x + 1] + str(item.y + 1))
                        elif lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y + 1)]].piece_color\
                                != item.piece_color:
                            wmoves.append("K" + item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y + 1))
                    if not lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y)]].occupied:
                        wmoves.append("K" + item.notcord + "-" + xcord_to_not[item.x + 1] + str(item.y))
                    elif lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y)]].piece_color != item.piece_color:
                        wmoves.append("K" + item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y))
                    if item.y > 1:
                        if not lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y - 1)]].occupied:
                            wmoves.append("K" + item.notcord + "-" + xcord_to_not[item.x + 1] + str(item.y - 1))
                        elif lsquares[not_to_num[xcord_to_not[item.x + 1] + str(item.y - 1)]].piece_color\
                                != item.piece_color:
                            wmoves.append("K" + item.notcord + "x" + xcord_to_not[item.x + 1] + str(item.y - 1))
                if item.y < 8:
                    if not lsquares[not_to_num[xcord_to_not[item.x] + str(item.y + 1)]].occupied:
                        wmoves.append("K" + item.notcord + "-" + xcord_to_not[item.x] + str(item.y + 1))
                    elif lsquares[not_to_num[xcord_to_not[item.x] + str(item.y + 1)]].piece_color != item.piece_color:
                        wmoves.append("K" + item.notcord + "x" + xcord_to_not[item.x] + str(item.y + 1))
                if item.y > 1:
                    if not lsquares[not_to_num[xcord_to_not[item.x] + str(item.y - 1)]].occupied:
                        wmoves.append("K" + item.notcord + "-" + xcord_to_not[item.x] + str(item.y - 1))
                    elif lsquares[not_to_num[xcord_to_not[item.x] + str(item.y - 1)]].piece_color != item.piece_color:
                        wmoves.append("K" + item.notcord + "x" + xcord_to_not[item.x] + str(item.y - 1))
                if item.x > 1:
                    if item.y < 8:
                        if not lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y + 1)]].occupied:
                            wmoves.append("K" + item.notcord + "-" + xcord_to_not[item.x - 1] + str(item.y + 1))
                        elif lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y + 1)]].piece_color\
                                != item.piece_color:
                            wmoves.append("K" + item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y + 1))
                    if not lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y)]].occupied:
                        wmoves.append("K" + item.notcord + "-" + xcord_to_not[item.x - 1] + str(item.y))
                    elif lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y)]].piece_color != item.piece_color:
                        wmoves.append("K" + item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y))
                    if item.y > 1:
                        if not lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y - 1)]].occupied:
                            wmoves.append("K" + item.notcord + "-" + xcord_to_not[item.x - 1] + str(item.y - 1))
                        elif lsquares[not_to_num[xcord_to_not[item.x - 1] + str(item.y - 1)]].piece_color\
                                != item.piece_color:
                            wmoves.append("K" + item.notcord + "x" + xcord_to_not[item.x - 1] + str(item.y - 1))
                if not lsquares[not_to_num["f1"]].occupied and not lsquares[not_to_num["g1"]].occupied:
                    counter = 0
                    for move in game_log:
                        if move.find("Ke1") != -1:
                            break
                        elif move.find("Rh1") != -1:
                            break
                        elif move.find("O-O") != -1 and what_turn(game_log, move) == "white":
                            break
                        elif move.find("O-O-O") != -1 and what_turn(game_log, move) == "white":
                            break
                        else:
                            counter += 1
                    if counter == len(game_log):
                        wmoves.append("O-O")
                if not lsquares[not_to_num["d1"]].occupied and not lsquares[not_to_num["c1"]].occupied\
                        and not lsquares[not_to_num["b1"]].occupied:
                    counter = 0
                    for move in game_log:
                        if move.find("Ke1") != -1:
                            break
                        elif move.find("Ra1") != -1:
                            break
                        elif move.find("O-O") != -1 and what_turn(game_log, move) == "white":
                            break
                        elif move.find("O-O-O") != -1 and what_turn(game_log, move) == "white":
                            break
                        else:
                            counter += 1
                    if counter == len(game_log):
                        wmoves.append("O-O-O")
    return wmoves
