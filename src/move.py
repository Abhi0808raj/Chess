class Move:

    def __init__(self,initial,final, piece_moved=None): # Add piece_moved parameter
        #initial and final are squares
        self.initial=initial
        self.final=final
        self.piece_moved = piece_moved # Store the piece that moved

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.initial == other.initial and self.final == other.final
        return False