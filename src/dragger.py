import pygame
from const import *


class Dragger:
    def __init__(self):
        self.piece=None
        self.dragging=False
        self.mouseX=0
        self.mouseY=0
        self.initial_row=0
        self.initial_col=0

# this method is updating the position of our piece
# blit method
    def update_blit(self,surface):
        #texture while dragging the piece
        self.piece.set_texture(size=128)
        texture=self.piece.texture

        #img while dragging the piece
        img=pygame.image.load(texture)
        #rectangle
        img_center=(self.mouseX,self.mouseY)
        self.piece.texture_rect=img.get_rect(center=img_center)
        #updated blit
        surface.blit(img,self.piece.texture_rect)
# other method

    def update_mouse(self,pos):
        self.mouseX,self.mouseY=pos   #defining the x and y coordinate of mouse

    def save_inital(self,pos):
        #saves inital position of mouse
        self.initial_row=pos[1]//SQSIZE
        self.initial_col=pos[0]//SQSIZE
    
    def drag_piece(self,piece):
        #to start dragging a piece
        self.piece=piece
        self.dragging=True

    def undrag_piece(self):
        #to stop dragging a piece
        self.piece=None
        self.dragging=False
