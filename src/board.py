from const import *
from square import Square
from piece import *
from move import Move
class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')
    
    def move(self, game, piece, move): # Accept game as argument
        """
        Moves a piece to a new square and records the move in history.

        Args:
            game (Game): The Game object.
            piece (Piece): The piece to move.
            move (Move): The move to execute.
        """
        initial_sq = move.initial
        final_sq = move.final

        # Enpty the initial square
        self.squares[initial_sq.row][initial_sq.col].piece = None
        # Add piece to new square
        self.squares[final_sq.row][final_sq.col].piece = piece

        # Set piece_moved in the Move object
        move.piece_moved = piece # Store the piece that was moved

        #Piece has moved
        piece.moved=True

        # Add move to history
        game.move_history.append(move) # Append to move history

        # Clear piece moves after move
        piece.moves = []
        

    def calc_moves(self,piece,row,col):
        # to calculate all the possible /valid moves of a specific piece on a specific position
        def pawn_moves():
            if piece.moved:
                steps=1
            else:
                steps=2
            #vertical moves
            start= row+piece.dir
            end=row+(piece.dir*(1+steps))
            for possible_move_row in range(start,end,piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].isempty():
                        #create initia; and final move squares
                        initial=Square(row,col)
                        final=Square(possible_move_row,col)
                        #create a new move
                        move=Move(initial,final)
                        #append new move
                        piece.add_move(move)
                    else:
                        break
                else:
                    break

            #diagonal moves
            possible_move_row=row+piece.dir
            possible_move_cols=[col-1,col+1]   
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row,possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                        #create initial and final move squares
                        initial=Square(row,col)
                        final=Square(possible_move_row,possible_move_col)
                        #create a new move
                        move=Move(initial,final)
                        #append new move
                        piece.add_move(move)



        def knight_moves():
            # defining all possible moves
            possible_moves=[
            (row-2,col+1),
            (row-1,col+2),
            (row+1,col+2),
            (row+2,col-1),
            (row+2,col+1),
            (row+1,col-2),
            (row-1,col-2),
            (row-2,col-1)
        ]

            for possible_move in possible_moves:
                possible_move_row,possible_move_col=possible_move

                if Square.in_range(possible_move_row,possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.color):
                        #create squares of new move
                        initial=Square(row,col)
                        final=Square(possible_move_row,possible_move_col)
                        #create new move
                        move=Move(initial,final)
                        #append new valid move
                        piece.add_move(move)

        def straightline_moves(incrs):
            #Calculates moves for rook bishop and queen along straight line
            for incr in incrs:
                row_incr,col_incr=incr
                possible_move_row=row+row_incr
                possible_move_col=col+col_incr

                while True:
                    if Square.in_range(possible_move_row,possible_move_col):
                        initial=Square(row,col)
                        final=Square(possible_move_row,possible_move_col)
                        move=Move(initial,final)

                        if self.squares[possible_move_row][possible_move_col].isempty():
                            piece.add_move(move)

                        if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                            piece.add_move(move)
                            break

                        if self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break
                           


                    else:break

                    possible_move_row=possible_move_row+row_incr
                    possible_move_col=possible_move_col+col_incr

        def king_moves():
            adjs=[
                (row-1,col+0),
                (row-1,col+1),
                (row+0,col+1),
                (row+1,col+1),
                (row+1,col+0),
                (row+1,col-1),
                (row+0,col-1),
                (row-1,col-1),
            ]
            for possible_move in adjs:
                possible_move_row,possiblie_move_col=possible_move
                if Square.in_range(possible_move_row,[possiblie_move_col]):
                    if self.squares[possible_move_row][possiblie_move_col].isempty_or_enemy(piece.color):
                        initial=Square(row,col)
                        final=Square(possible_move_row,possiblie_move_col)
                        move=Move(initial,final)
                        piece.add_move(move)
                

        if isinstance(piece,Pawn):
            pawn_moves()

        elif isinstance(piece,Knight):
            knight_moves()

        elif isinstance(piece,Rook):
            straightline_moves([
                (-1,0),
                (0,1),
                (1,0),
                (0,-1),
            ])


        elif isinstance(piece,Bishop):
            straightline_moves([
                (-1,1),
                (-1,-1),
                (1,1),
                (1,-1)
            ])

        elif isinstance(piece,Queen):
            straightline_moves([
                (-1,0),
                (0,1),
                (1,0),
                (0,-1),
                (-1,1),
                (-1,-1),
                (1,1),
                (1,-1)
                
            ])
                
        elif isinstance(piece,King):
            king_moves()





    def _create(self):
        #create squares on board
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        # pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))
        
        # rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        # king
        self.squares[row_other][4] = Square(row_other, 4, King(color))