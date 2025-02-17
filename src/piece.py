
import os

class Piece:

    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture=texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size=80):
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')

    def add_move(self, move):
        self.moves.append(move)

    def copy(self):
        """
        Creates a shallow copy of the Piece object.
        Note: Shallow copy is sufficient here as piece attributes are immutable (name, color, value, texture).
        """
        return Piece(self.name, self.color, self.value, self.texture, self.texture_rect)


class Pawn(Piece):

    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        super().__init__('pawn', color, 1.0)

    def copy(self):
        return Pawn(self.color) # Only color is needed for Pawn constructor


class Knight(Piece):

    def __init__(self, color):
        super().__init__('knight', color, 3.0)

    def copy(self):
        return Knight(self.color)


class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop', color, 3.001)

    def copy(self):
        return Bishop(self.color)


class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook', color, 5.0)

    def copy(self):
        return Rook(self.color)


class Queen(Piece):

    def __init__(self, color):
        super().__init__('queen', color, 9.0)

    def copy(self):
        return Queen(self.color)


class King(Piece):

    def __init__(self, color):
        super().__init__('king', color, 10000.0)

    def copy(self):
        return King(self.color)
