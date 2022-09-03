from Square import Square

a1 = Square(1, 1, True, "white", "rook", "a1")
a2 = Square(1, 2, True, "white", "pawn", "a2")
a3 = Square(1, 3, False, "none", "none", "a3")
a4 = Square(1, 4, False, "none", "none", "a4")
a5 = Square(1, 5, False, "none", "none", "a5")
a6 = Square(1, 6, False, "none", "none", "a6")
a7 = Square(1, 7, True, "black", "pawn", "a7")
a8 = Square(1, 8, True, "black", "rook", "a8")

b1 = Square(2, 1, True, "white", "knight", "b1")
b2 = Square(2, 2, True, "white", "pawn", "b2")
b3 = Square(2, 3, False, "none", "none", "b3")
b4 = Square(2, 4, False, "none", "none", "b4")
b5 = Square(2, 5, False, "none", "none", "b5")
b6 = Square(2, 6, False, "none", "none", "b6")
b7 = Square(2, 7, True, "black", "pawn", "b7")
b8 = Square(2, 8, True, "black", "knight", "b8")

c1 = Square(3, 1, True, "white", "bishop", "c1")
c2 = Square(3, 2, True, "white", "pawn", "c2")
c3 = Square(3, 3, False, "none", "none", "c3")
c4 = Square(3, 4, False, "none", "none", "c4")
c5 = Square(3, 5, False, "none", "none", "c5")
c6 = Square(3, 6, False, "none", "none", "c6")
c7 = Square(3, 7, True, "black", "pawn", "c7")
c8 = Square(3, 8, True, "black", "bishop", "c8")

d1 = Square(4, 1, True, "white", "queen", "d1")
d2 = Square(4, 2, True, "white", "pawn", "d2")
d3 = Square(4, 3, False, "none", "none", "d3")
d4 = Square(4, 4, False, "none", "none", "d4")
d5 = Square(4, 5, False, "none", "none", "d5")
d6 = Square(4, 6, False, "none", "none", "d6")
d7 = Square(4, 7, True, "black", "pawn", "d7")
d8 = Square(4, 8, True, "black", "queen", "d8")

e1 = Square(5, 1, True, "white", "king", "e1")
e2 = Square(5, 2, True, "white", "pawn", "e2")
e3 = Square(5, 3, False, "none", "none", "e3")
e4 = Square(5, 4, False, "none", "none", "e4")
e5 = Square(5, 5, False, "none", "none", "e5")
e6 = Square(5, 6, False, "none", "none", "e6")
e7 = Square(5, 7, True, "black", "pawn", "e7")
e8 = Square(5, 8, True, "black", "king", "e8")

f1 = Square(6, 1, True, "white", "bishop", "f1")
f2 = Square(6, 2, True, "white", "pawn", "f2")
f3 = Square(6, 3, False, "none", "none", "f3")
f4 = Square(6, 4, False, "none", "none", "f4")
f5 = Square(6, 5, False, "none", "none", "f5")
f6 = Square(6, 6, False, "none", "none", "f6")
f7 = Square(6, 7, True, "black", "pawn", "f7")
f8 = Square(6, 8, True, "black", "bishop", "f8")

g1 = Square(7, 1, True, "white", "knight", "g1")
g2 = Square(7, 2, True, "white", "pawn", "g2")
g3 = Square(7, 3, False, "none", "none", "g3")
g4 = Square(7, 4, False, "none", "none", "g4")
g5 = Square(7, 5, False, "none", "none", "g5")
g6 = Square(7, 6, False, "none", "none", "g6")
g7 = Square(7, 7, True, "black", "pawn", "g7")
g8 = Square(7, 8, True, "black", "knight", "g8")

h1 = Square(8, 1, True, "white", "rook", "h1")
h2 = Square(8, 2, True, "white", "pawn", "h2")
h3 = Square(8, 3, False, "none", "none", "h3")
h4 = Square(8, 4, False, "none", "none", "h4")
h5 = Square(8, 5, False, "none", "none", "h5")
h6 = Square(8, 6, False, "none", "none", "h6")
h7 = Square(8, 7, True, "black", "pawn", "h7")
h8 = Square(8, 8, True, "black", "rook", "h8")

squares = [
    a1, a2, a3, a4, a5, a6, a7, a8,
    b1, b2, b3, b4, b5, b6, b7, b8,
    c1, c2, c3, c4, c5, c6, c7, c8,
    d1, d2, d3, d4, d5, d6, d7, d8,
    e1, e2, e3, e4, e5, e6, e7, e8,
    f1, f2, f3, f4, f5, f6, f7, f8,
    g1, g2, g3, g4, g5, g6, g7, g8,
    h1, h2, h3, h4, h5, h6, h7, h8,
]

sa1 = Square(1, 1, True, "white", "rook", "a1")
sa2 = Square(1, 2, True, "white", "pawn", "a2")
sa3 = Square(1, 3, False, "none", "none", "a3")
sa4 = Square(1, 4, False, "none", "none", "a4")
sa5 = Square(1, 5, False, "none", "none", "a5")
sa6 = Square(1, 6, False, "none", "none", "a6")
sa7 = Square(1, 7, True, "black", "pawn", "a7")
sa8 = Square(1, 8, True, "black", "rook", "a8")

sb1 = Square(2, 1, True, "white", "knight", "b1")
sb2 = Square(2, 2, True, "white", "pawn", "b2")
sb3 = Square(2, 3, False, "none", "none", "b3")
sb4 = Square(2, 4, False, "none", "none", "b4")
sb5 = Square(2, 5, False, "none", "none", "b5")
sb6 = Square(2, 6, False, "none", "none", "b6")
sb7 = Square(2, 7, True, "black", "pawn", "b7")
sb8 = Square(2, 8, True, "black", "knight", "b8")

sc1 = Square(3, 1, True, "white", "bishop", "c1")
sc2 = Square(3, 2, True, "white", "pawn", "c2")
sc3 = Square(3, 3, False, "none", "none", "c3")
sc4 = Square(3, 4, False, "none", "none", "c4")
sc5 = Square(3, 5, False, "none", "none", "c5")
sc6 = Square(3, 6, False, "none", "none", "c6")
sc7 = Square(3, 7, True, "black", "pawn", "c7")
sc8 = Square(3, 8, True, "black", "bishop", "c8")

sd1 = Square(4, 1, True, "white", "queen", "d1")
sd2 = Square(4, 2, True, "white", "pawn", "d2")
sd3 = Square(4, 3, False, "none", "none", "d3")
sd4 = Square(4, 4, False, "none", "none", "d4")
sd5 = Square(4, 5, False, "none", "none", "d5")
sd6 = Square(4, 6, False, "none", "none", "d6")
sd7 = Square(4, 7, True, "black", "pawn", "d7")
sd8 = Square(4, 8, True, "black", "queen", "d8")

se1 = Square(5, 1, True, "white", "king", "e1")
se2 = Square(5, 2, True, "white", "pawn", "e2")
se3 = Square(5, 3, False, "none", "none", "e3")
se4 = Square(5, 4, False, "none", "none", "e4")
se5 = Square(5, 5, False, "none", "none", "e5")
se6 = Square(5, 6, False, "none", "none", "e6")
se7 = Square(5, 7, True, "black", "pawn", "e7")
se8 = Square(5, 8, True, "black", "king", "e8")

sf1 = Square(6, 1, True, "white", "bishop", "f1")
sf2 = Square(6, 2, True, "white", "pawn", "f2")
sf3 = Square(6, 3, False, "none", "none", "f3")
sf4 = Square(6, 4, False, "none", "none", "f4")
sf5 = Square(6, 5, False, "none", "none", "f5")
sf6 = Square(6, 6, False, "none", "none", "f6")
sf7 = Square(6, 7, True, "black", "pawn", "f7")
sf8 = Square(6, 8, True, "black", "bishop", "f8")

sg1 = Square(7, 1, True, "white", "knight", "g1")
sg2 = Square(7, 2, True, "white", "pawn", "g2")
sg3 = Square(7, 3, False, "none", "none", "g3")
sg4 = Square(7, 4, False, "none", "none", "g4")
sg5 = Square(7, 5, False, "none", "none", "g5")
sg6 = Square(7, 6, False, "none", "none", "g6")
sg7 = Square(7, 7, True, "black", "pawn", "g7")
sg8 = Square(7, 8, True, "black", "knight", "g8")

sh1 = Square(8, 1, True, "white", "rook", "h1")
sh2 = Square(8, 2, True, "white", "pawn", "h2")
sh3 = Square(8, 3, False, "none", "none", "h3")
sh4 = Square(8, 4, False, "none", "none", "h4")
sh5 = Square(8, 5, False, "none", "none", "h5")
sh6 = Square(8, 6, False, "none", "none", "h6")
sh7 = Square(8, 7, True, "black", "pawn", "h7")
sh8 = Square(8, 8, True, "black", "rook", "h8")

ssquares = [
    sa1, sa2, sa3, sa4, sa5, sa6, sa7, sa8,
    sb1, sb2, sb3, sb4, sb5, sb6, sb7, sb8,
    sc1, sc2, sc3, sc4, sc5, sc6, sc7, sc8,
    sd1, sd2, sd3, sd4, sd5, sd6, sd7, sd8,
    se1, se2, se3, se4, se5, se6, se7, se8,
    sf1, sf2, sf3, sf4, sf5, sf6, sf7, sf8,
    sg1, sg2, sg3, sg4, sg5, sg6, sg7, sg8,
    sh1, sh2, sh3, sh4, sh5, sh6, sh7, sh8
]

not_to_num = {
    "a1": 0, "a2": 1, "a3": 2, "a4": 3, "a5": 4, "a6": 5, "a7": 6, "a8": 7,
    "b1": 8, "b2": 9, "b3": 10, "b4": 11, "b5": 12, "b6": 13, "b7": 14, "b8": 15,
    "c1": 16, "c2": 17, "c3": 18, "c4": 19, "c5": 20, "c6": 21, "c7": 22, "c8": 23,
    "d1": 24, "d2": 25, "d3": 26, "d4": 27, "d5": 28, "d6": 29, "d7": 30, "d8": 31,
    "e1": 32, "e2": 33, "e3": 34, "e4": 35, "e5": 36, "e6": 37, "e7": 38, "e8": 39,
    "f1": 40, "f2": 41, "f3": 42, "f4": 43, "f5": 44, "f6": 45, "f7": 46, "f8": 47,
    "g1": 48, "g2": 49, "g3": 50, "g4": 51, "g5": 52, "g6": 53, "g7": 54, "g8": 55,
    "h1": 56, "h2": 57, "h3": 58, "h4": 59, "h5": 60, "h6": 61, "h7": 62,  "h8": 63
}

xcord_to_not = {
    1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h"
}


def what_turn(game_log, move):
    if game_log.index(move) % 2 == 0:
        return "white"
    elif game_log.index(move) % 2 == 1:
        return "black"
    else:
        print("error")
