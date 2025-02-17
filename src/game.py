
import pygame
from board import Board
from const import *
from piece import *
from dragger import Dragger
class Game:

    def __init__(self):
        self.board=Board()
        self.dragger=Dragger()
        self.player_turn = 'white' # Add player_turn attribute
        self.move_history = [] # Initialize move history list
    # blit method
    #Showing Colors and Making Grid on Board

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
               if (row+col)%2==0:
                 color=(234,235,200)   #color code for light green
               else:
                 color=(119,154,88)    #color code for dark green

               rect=(col*SQSIZE,row*SQSIZE,SQSIZE,SQSIZE)
               pygame.draw.rect(surface,color,rect)

    def show_pieces(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                #piece checking
                if self.board.squares[row][col].has_piece():  #checking if a piece is on a square
                    piece= self.board.squares[row][col].piece  #then saving that piece on a Variable

                    # all pieces except dragger piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)

                        img=pygame.image.load(piece.texture)
                        img_center=col*SQSIZE+SQSIZE//2,row*SQSIZE+SQSIZE//2   #centering our image on board square
                        piece.texture_rect=img.get_rect(center=img_center)
                        surface.blit(img,piece.texture_rect)
    def show_moves(self,surface):
        if self.dragger.dragging:
            piece=self.dragger.piece

            #looping all valid moves
            for move in piece.moves:
               #we wanna create a color,rect and then blit
               #color
               color='#C86464' if (move.final.row+move.final.col) %2 ==0 else '#C84646'
               #rect
               rect=(move.final.col*SQSIZE,move.final.row*SQSIZE,SQSIZE,SQSIZE)
               #blit
               pygame.draw.rect(surface,color,rect)

    def next_turn(self):
        #for switching turns
        self.player_turn='black' if self.player_turn=='white' else 'white'

    def reset_game(self):
        #reset the game into inital state
        self.board=Board()
        self.dragger=Dragger()
        self.player_turn='white'
        self.move_history=[]