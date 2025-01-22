from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.displayer.console_displayer import *
from modules.models.board_game.components.move import Move
from modules.models.board_game.game.game_outcome import GameOutcomeStatus
from modules.models.board_game.game.game_analyser import GameAnalyser
import random

# ************************************************
# CLASS MinimaxAnalyser
# ************************************************
# ROLE : This Analyser returns the best move using the minimax algorithm
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 10/01/2025
# ************************************************

class MinimaxAnalyser(GameAnalyser):
    
    """
    A class that implements the minimax algorithm to analyze and evaluate 
    possible moves in a Tic-Tac-Toe game. This class extends the abstract 
    GameAnalyser class and provides specific logic for calculating 
    minimax scores and determining the best move.
    """

    def __init__(self, depth : int, debugOn : bool = False) -> None:

        """
        Initializes the MinimaxAnalyser instance with the given depth and debugging flag.
        
        Parameters:
            depth (int): The depth of the search tree for the minimax algorithm.
            debugOn (bool): Optional flag to enable debugging output (default is False).
            
        Raises:
            TypeError: If the depth is not a positive integer or the debugOn flag is not a boolean value.
            
        Returns:
            None
        """        
        
        # Check if the depth is a positive integer
        if not isinstance(depth, int) or depth <= 0: 
            raise TypeError("depth must be a positive integer")
        
        # Check if the debugOn flag is a boolean value
        if not isinstance(debugOn, bool):
            raise TypeError("debugOn must be a boolean value")

        # Call the parent constructor
        super().__init__(depth, debugOn)
        
        return None
    
    def getMovesScores(self, gameState: TicTacToeGameState) -> dict[Move, int]:
        
        """
        Evaluates all possible moves and returns their corresponding minimax scores.

        Parameters:
            gameState (TicTacToeGameState): The current state of the game.
            
        Raises:
            TypeError: If the gameState is not an instance of TicTacToeGameState.

        Returns:
            dict[Move, int]: A dictionary mapping each possible move to its minimax score.
        """
        
        # Check if the gameState is an instance of TicTacToeGameState
        if not isinstance(gameState, TicTacToeGameState):
            raise TypeError("gameState must be an instance of TicTacToeGameState")
        
        # Initialize the number of nodes explored
        self.__nodeExplored__ = 0
        
        # Get the index of the maximizing player
        maximizingPlayerIndex : int = gameState.getPlayerToPlayIndex()
        moveScores : dict = {}

        # Evaluate all possible moves
        for moveIndex, move in enumerate(gameState.getPossibleMoves()):
            
            # Play the move and get the game outcome
            gameOutcome : GameOutcomeStatus = gameState.play(move)
            
            score : int

            # If the game is finished, calculate the score based on the outcome
            if(gameOutcome.getGameStatus() != GameOutcomeStatus.UNFINISHED) : 
                
                # Calculate the score based on the game outcome
                if gameOutcome.getGameStatus() == GameOutcomeStatus.DRAW : score = 0                 
                elif gameOutcome.getWinner() == maximizingPlayerIndex : score = self.getWinReward(gameState)
                else : score = - self.getWinReward(gameState)

                # Undo the move
                gameState.undo(move)
                
            else :

                # Recursively evaluate the game state
                score, _ = self.__minimax__(gameState, self.__depth__ - 1, maximizingPlayerIndex, float('-inf'), float('inf'))
                gameState.undo(move)
            
            # Store the move and its score
            moveScores[move] = score
            
            if(self.__debugOn__): print(f"Move {moveIndex}: {move}, Score: {score}")
        
        if(self.__debugOn__): print("Explored : ", self.__nodeExplored__)

        return moveScores

    
    def getBestMove(self, gameState : TicTacToeGameState) -> Move:
        
        """
        Determines the best move for the current game state based on the minimax algorithm.

        The method finds the move with the highest score for the maximizing player 
        (i.e., the optimal move) and returns it.

        Parameters:
            gameState (TicTacToeGameState): The current state of the Tic-Tac-Toe game.
            
        Raises:
            TypeError: If the gameState is not an instance of TicTacToeGameState.
        
        Returns:
            Move: The best move determined by the minimax algorithm.
        """
        
        if not isinstance(gameState, TicTacToeGameState):
            raise TypeError("gameState must be an instance of TicTacToeGameState")

        # Initialize the number of nodes explored
        self.__nodeExplored__ = 0
        
        # Get the index of the maximizing player
        bestScore, bestMove = self.__minimax__(gameState, self.__depth__, gameState.getPlayerToPlayIndex())
            
        if(self.__debugOn__):
            
            print("Explored : ", self.__nodeExplored__)
            print("Best score : ", bestScore)

        return bestMove
    
    def __minimax__(self, gameState: TicTacToeGameState, depth: int, playerIndex: int) -> tuple[int, Move | None]:
        
        """
        Recursively evaluates the game state using the Minimax algorithm.

        Parameters : 
            gameState : Current game state.
            depth : Remaining search depth.
            playerIndex : The index of the maximizing player.
            
        Raises :
            TypeError : If the gameState is not an instance of TicTacToeGameState.
            TypeError : If the depth is not a positive integer.
            TypeError : If the playerIndex is not an integer.
            ValueError : If the playerIndex is out of range.
            
        Return : 
            A tuple (score, move), where `score` is the evaluation of the board, and `move` is the best move to play.
        """
        
        # Check if the gameState is an instance of TicTacToeGameState
        if not isinstance(gameState, TicTacToeGameState):
            raise TypeError("gameState must be an instance of TicTacToeGameState")
        
        # Check if the depth is a positive integer
        if not isinstance(depth, int) or depth < 0:
            raise TypeError("depth must be a positive integer")
        
        # Check if the playerIndex is an integer and within the valid range
        if not isinstance(playerIndex, int):
            raise TypeError("playerIndex must be an integer")
        
        if playerIndex < 0 or playerIndex >= gameState.getPlayerCount():
            raise ValueError("playerIndex is out of range")

        # Increment the number of nodes explored
        self.__nodeExplored__ += 1

        # If the depth is 0, return the evaluation of the game state
        if depth == 0 : return gameState.evaluateForPlayer(playerIndex), None

        # Initialize the best score and best move
        bestScore : int = None
        bestMove : int = None
        e : int = 0

        # Evaluate all possible moves
        for move in gameState.getPossibleMoves() :         

            # Play the move and get the game outcome
            gameOutcome = gameState.play(move)
            
            # If the game is finished, calculate the score based on the outcome
            if(gameOutcome.getGameStatus() != GameOutcomeStatus.UNFINISHED) : 
                
                score : int
                
                # Calculate the score based on the game outcome
                if gameOutcome.getGameStatus() == GameOutcomeStatus.DRAW : score = 0                 
                elif gameOutcome.getWinner() == playerIndex : score : int = self.getWinReward(gameState)
                else : score : int = - self.getWinReward(gameState)

                # Undo the move and return the score
                gameState.undo(move)
                
                return score, move

            else :
                
                # Recursively evaluate the game state
                nextScore, _ = self.__minimax__(gameState, depth - 1, playerIndex)

                # Undo the move
                gameState.undo(move)

                # Update the best score and best move based on the player index
                if playerIndex == gameState.getPlayerToPlayIndex():

                    if bestScore == None or nextScore > bestScore:
                        
                        if(bestScore is not None) : e += self.getMoveStrengthToAdd(bestScore) 
                        bestScore = nextScore
                        bestMove = move
                        
                    else : 
                        e += self.getMoveStrengthToAdd(nextScore)
                        
                else :

                    # Update the best score and best move based on the player index
                    if bestScore == None or nextScore < bestScore:
                        
                        if(bestScore is not None) : e += self.getMoveStrengthToAdd(bestScore)
                        bestScore = nextScore
                        bestMove = move
                        
                    else : 
                        e += self.getMoveStrengthToAdd(nextScore)

        return bestScore + e, bestMove

    def getMoveStrengthToAdd(self, score : int) -> int: 

        """
        Give a small value that represent the move potential
        
        Parameters :
            score (int) : the score of the move
            
        Raises :
            TypeError : If the score is not an integer
        
        Returns :
            strength (int) : a small value that represent the move potential
        """        
        
        # Check if the score is an integer
        if not isinstance(score, int):
            raise TypeError("score must be an integer")

        return score / 1000

    def getWinReward(self, gameState : TicTacToeGameState) -> int:
        
        """
        Calculates the reward score for a winning state.
        Prioritizes faster wins by providing higher scores.

        Parameters:
            gameState (GameState): The current game state.
            
        Raises:
            TypeError: If the gameState is not an instance of GameState.
            
        Returns:
            int: The calculated win reward.
        """
        
        # Check if the gameState is an instance of GameState
        if not isinstance(gameState, TicTacToeGameState):
            raise TypeError("gameState must be an instance of GameState")
        
        # Calculate the score based on the number of moves
        maxMoves : int = gameState.getBoard().getHeight() * gameState.getBoard().getWidth()
        score : int = ((maxMoves + 3) - gameState.getBoard().getPieceCount()) // 2

        return score