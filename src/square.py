# --- square.py ---
class Square:
    """
    Represents a square on the chessboard.
    """

    def __init__(self,row,col,piece=None):
        self.row=row
        self.col=col
        self.piece=piece

    def has_piece(self):
       return self.piece!=None

    def isempty(self):
       return not self.has_piece()

    def has_team_piece(self,color):
        return self.has_piece() and self.piece.color==color

    def has_enemy_piece(self,color):
        return self.has_piece() and self.piece.color!=color

    def isempty_or_enemy(self,color):
        return self.isempty() or self.has_enemy_piece(color)


    # checking if the piece is inside or outside the board

    @staticmethod   #used to call a class without any object
    def in_range(*args):
        for arg in args:
            if arg<0 or arg>7:
                return False

        return True

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.row == other.row and self.col == other.col
        return False