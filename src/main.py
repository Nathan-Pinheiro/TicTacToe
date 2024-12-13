from modules.GUI.render import App

if(__name__ == "__main__") :
             
    app = App("TicTacToe")
    app.mainloop()
    
# from modules.models.board.board import Board
# from modules.models.board.board_builder import BoardBuilder
# from modules.models.board.board_shapes.pyramidal_shape import PyramidalShape
# from modules.models.tic_tac_toe.game_state import TicTacToeGameState
# from modules.models.coordinate_encoder import *
# from modules.models.console_displayer import display_board
# from modules.models.coordinate import *

# if(__name__ == "__main__"):
    
#     width : int = 5
#     height : int = 5
    
#     player_count : int = 2
#     board : Board = BoardBuilder().setHeight(3).setWidth(3).setShape(PyramidalShape()).setRandomlyBlockedCaseAmount(9).build()

#     game_state : TicTacToeGameState = TicTacToeGameState(board, player_count)
   
#     display_board(game_state.getBoard())
