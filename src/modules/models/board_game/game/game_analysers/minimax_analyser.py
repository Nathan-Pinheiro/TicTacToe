from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.utils.console_displayer import *
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
        
        Args:
            depth (int): The depth of the search tree for the minimax algorithm.
            debugOn (bool): Optional flag to enable debugging output (default is False).
        """        

        super().__init__(depth, debugOn)
    
    def getMovesScores(self, gameState: TicTacToeGameState) -> dict[Move, int]:
        
        """
        Evaluates all possible moves and returns their corresponding minimax scores.

        Args:
            gameState (TicTacToeGameState): The current state of the game.

        Returns:
            dict[Move, int]: A dictionary mapping each possible move to its minimax score.
        """
        
        self.__nodeExplored__ = 0
        
        maximizingPlayerIndex : int = gameState.getPlayerToPlayIndex()
        moveScores : dict = {}

        for moveIndex, move in enumerate(gameState.getPossibleMoves()):
            
            gameOutcome : GameOutcomeStatus = gameState.play(move)
            
            score : int

            if(gameOutcome.getGameStatus() != GameOutcomeStatus.UNFINISHED) : 
                
                if gameOutcome.getGameStatus() == GameOutcomeStatus.DRAW : score = 0                 
                elif gameOutcome.getWinner() == maximizingPlayerIndex : score = self.getWinReward(gameState)
                else : score = - self.getWinReward(gameState)

                gameState.undo(move)
                
            else :

                score, _ = self.__minimax__(gameState, self.__depth__ - 1, maximizingPlayerIndex, float('-inf'), float('inf'))
                gameState.undo(move)
            
            moveScores[move] = score
            
            if(self.__debugOn__): print(f"Move {moveIndex}: {move}, Score: {score}")
        
        if(self.__debugOn__): print("Explored : ", self.__nodeExplored__)

        return moveScores

    
    def getBestMove(self, gameState : TicTacToeGameState):
        
        """
        Determines the best move for the current game state based on the minimax algorithm.

        The method finds the move with the highest score for the maximizing player 
        (i.e., the optimal move) and returns it.

        Args:
            gameState (TicTacToeGameState): The current state of the Tic-Tac-Toe game.
        
        Returns:
            Move: The best move determined by the minimax algorithm.
        """

        self.__nodeExplored__ = 0
        
        bestScore, bestMove = self.__minimax__(gameState, self.__depth__, gameState.getPlayerToPlayIndex())
            
        if(self.__debugOn__):
            
            print("Explored : ", self.__nodeExplored__)
            print("Best score : ", bestScore)

        return bestMove
    
    def __minimax__(self, gameState: TicTacToeGameState, depth: int, playerIndex: int) -> tuple[int, Move]:
        
        """
        Recursively evaluates the game state using the Minimax algorithm.

        Parameters : 
            - gameState : Current game state.
            - depth : Remaining search depth.
            - playerIndex : The index of the maximizing player.
            
        Return : A tuple (score, move), where `score` is the evaluation of the board, and `move` is the best move to play.
        """

        self.__nodeExplored__ += 1

        if depth == 0 : return gameState.evaluateForPlayer(playerIndex), None

        bestScore : int = None
        bestMove : int = None
        e : int = 0

        for move in gameState.getPossibleMoves() :         

            gameOutcome = gameState.play(move)
            
            if(gameOutcome.getGameStatus() != GameOutcomeStatus.UNFINISHED) : 
                
                score : int
                
                if gameOutcome.getGameStatus() == GameOutcomeStatus.DRAW : score = 0                 
                elif gameOutcome.getWinner() == playerIndex : score : int = self.getWinReward(gameState)
                else : score : int = - self.getWinReward(gameState)

                gameState.undo(move)
                
                return score, move

            else :
                
                nextScore, _ = self.__minimax__(gameState, depth - 1, playerIndex)

                gameState.undo(move)

                if playerIndex == gameState.getPlayerToPlayIndex():

                    if bestScore == None or nextScore > bestScore:
                        
                        if(bestScore is not None) : e += self.getMoveStrengthToAdd(bestScore) 
                        bestScore = nextScore
                        bestMove = move
                        
                    else : 
                        e += self.getMoveStrengthToAdd(nextScore)
                        
                else :

                    if bestScore == None or nextScore < bestScore:
                        
                        if(bestScore is not None) : e += self.getMoveStrengthToAdd(bestScore)
                        bestScore = nextScore
                        bestMove = move
                        
                    else : 
                        e += self.getMoveStrengthToAdd(nextScore)

        return bestScore + e, bestMove

    def getMoveStrengthToAdd(self, score : int) -> int : 

        """
        Give a small value that represent the move potential
        
        Returns :
            strength (int) : a small value that represent the move potential
        """        

        return score / 1000

    def getWinReward(self, gameState : TicTacToeGameState) :
        
        """
        Calculates the reward score for a winning state.
        Prioritizes faster wins by providing higher scores.

        Args:
            gameState (GameState): The current game state.
            
        Returns:
            int: The calculated win reward.
        """
        
        maxMoves : int = gameState.getBoard().getHeight() * gameState.getBoard().getWidth()
        score : int = ((maxMoves + 3) - gameState.getBoard().getPieceCount()) // 2

        return score