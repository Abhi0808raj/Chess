                if board.squares[clicked_row][clicked_col].has_piece():
                    piece=board.squares[clicked_row][clicked_col].piece
                    if piece.color == game.player_turn: # Check if piece color matches player turn
                        board.calc_moves(piece,clicked_row,clicked_col)
                        dragger.save_inital(event.pos)
                        dragger.drag_piece(piece)
                        #show methods
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)