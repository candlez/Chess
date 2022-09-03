class Square:

    def __init__(self, x, y, occupied, piece_color, piece_type, notcord):
        self.x = x
        self.y = y
        self.occupied = occupied
        self.piece_color = piece_color
        self.piece_type = piece_type
        self.notcord = notcord


class Position:

    def __init__(self, lsquare):
        position = list()
        for square in lsquare:
            if square.occupied:
                position.append([square.piece_type, square.piece_color, square.notcord])
        self.position = position
