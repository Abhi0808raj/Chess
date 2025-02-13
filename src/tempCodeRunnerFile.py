# --- main.py ---
#Main File
import pygame    #main Game Module
import sys       #Used for opening and exiting the application
from board import *
from const import *
from game import Game

class Main:

    def __init__(self):
        #initialize the game
        pygame.init()
        self.screen=pygame.display.set_mode( (WIDTH,HEIGHT) )
        pygame.display.set_caption('Chess')
        self.game=Game()
        print(f"SQSIZE: {SQSIZE}") 

    def mainloop(self):
        screen=self.screen
        game=self.game
        dragger=self.game.dragger
        board=self.game.board

        while True:
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            game.show_move_history(screen) # Call show_move_history here

            if dragger.dragging:
                dragger.update_blit(screen)


            for event in pygame.event.get():

                #click
                if event.type==pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos) #tells the coordinates of mouse

                    clicked_row=dragger.mouseY//SQSIZE
                    clicked_col=dragger.mouseX//SQSIZE

                    #if clicked square has a piece
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece=board.squares[clicked_row][clicked_col].piece
                        board.calc_moves(piece,clicked_row,clicked_col)
                        dragger.save_inital(event.pos)
                        dragger.drag_piece(piece)
                        #show methods
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)

                #Mouse motion
                elif event.type==pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # show methods
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                #Releasing the click
                elif event.type==pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        # dragger.undrag_piece() # DO NOT UNDRAG YET!

                        released_row = dragger.mouseY // SQSIZE # Corrected: mouseY for row!
                        released_col = dragger.mouseX // SQSIZE # Corrected: mouseX for col!

                        #create possible move
                        initial=Square(dragger.initial_row,dragger.initial_col)
                        final=Square(released_row,released_col)
                        move=Move(initial,final)

                        print("Attempted move:")
                        print(f"  Initial Square: Row={move.initial.row}, Col={move.initial.col}")
                        print(f"  Final Square: Row={move.final.row}, Col={move.final.col}")

                        print("Valid moves:")
                        for valid_move in dragger.piece.moves:
                            print("  Valid Move:")
                            print(f"    Initial Square: Row={valid_move.initial.row}, Col={valid_move.initial.col}")
                            print(f"    Final Square: Row={valid_move.final.row}, Col={valid_move.final.col}")

                        #check if move is valid
                        if move in dragger.piece.moves: # Line 75 - This should now work because we haven't undragged yet
                            print("Move is VALID!")
                            board.move(game,dragger.piece,move)
                            game.next_turn()
                        else:
                            print("Move is INVALID!")
                            # If move is invalid, return piece to initial position
                            board.squares[dragger.initial_row][dragger.initial_col].piece = dragger.piece
                            game.show_bg(screen)
                            game.show_pieces(screen) # Redraw pieces at original positions

                        dragger.undrag_piece() # NOW undrag the piece, after checking the move

                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        game.reset_game()
                        board = game.board
                        dragger = game.dragger
                        game.show_bg(screen)
                        game.show_pieces(screen)
                        pygame.display.update()


                # quitting the application
                elif event.type==pygame.QUIT: #checking if user decides to quit the gameand exiting the applicaiton
                    pygame.quit()
                    sys.exit()





            pygame.display.update()


main=Main()
main.mainloop()