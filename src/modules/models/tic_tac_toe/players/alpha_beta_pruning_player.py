from modules.models.tic_tac_toe.players.player import Player
from modules.models.tic_tac_toe.game_state import GameState
from modules.models.board_components.coordinate import Coordinate
from modules.models.board_components.case import Case
from modules.models.console_displayer import *
from modules.models.tic_tac_toe.move import Move
from modules.models.tic_tac_toe.game_outcome import GameOutcomeStatus
import random

class AlphaBetaPruningPlayer(Player):
    
    def __init__(self, maxDepth : int) -> None:
        
        super().__init__("Minimax AI")
        self.__maxDepth__  : int = maxDepth
    
    def get_choice(self, gameState : GameState) -> Move:
        
        self.__nodeExplored__ = 0
        
        bestScore, bestMove = self.__minimax__(gameState, self.__maxDepth__, gameState.getPlayerToPlayIndex())   

        print("Explored : ", self.__nodeExplored__)
        print("Best score : ", bestScore)

        return bestMove
    
    def __minimax__(self, gameState: GameState, depth: int, playerIndex: int, alpha: int = float('-inf'), beta: int = float('inf')) -> tuple[int, Move]:
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

        bestScore = None
        bestMove = None
        e = 0

        possibleMoves = gameState.getPossibleMoves()
        moveIndex = 0

        while moveIndex < len(possibleMoves) and alpha < beta:
            
            currentMove = possibleMoves[moveIndex]

            gameOutcome = gameState.play(currentMove)
            
            if(gameOutcome.getGameStatus() != GameOutcomeStatus.UNFINISHED) : 
                
                gameState.undo(currentMove)
                
                if gameOutcome.getGameStatus() == GameOutcomeStatus.DRAW : return 0, currentMove
                elif gameOutcome.getWinner() == playerIndex : return self.getWinReward(gameState), currentMove
                else : return self.getLooseReward(gameState), currentMove

            else :
                
                nextScore, _ = self.__minimax__(gameState, depth - 1, playerIndex, alpha, beta)

                gameState.undo(currentMove)

                if playerIndex == gameState.getPlayerToPlayIndex():

                    if bestScore == None or nextScore > bestScore:
                        
                        if(bestScore is not None) : e += self.getMoveStrengthToAdd(bestScore) 
                        bestScore = nextScore
                        bestMove = currentMove
                        
                    else : 
                        e += self.getMoveStrengthToAdd(nextScore)
                        
                    alpha = max(alpha, bestScore)
                else :

                    if bestScore == None or nextScore < bestScore:
                        
                        if(bestScore is not None) : e += self.getMoveStrengthToAdd(bestScore)
                        bestScore = nextScore
                        bestMove = currentMove
                        
                    else : e += self.getMoveStrengthToAdd(nextScore)
                        
                    beta = min(beta, bestScore)

                moveIndex += 1
                    

        return bestScore + e, bestMove

    def getMoveStrengthToAdd(self, score : int) -> int : 
        return score / 1000

    def getWinReward(self, gameState : GameState) :
        
        maxMoves : int = gameState.getBoard().getHeight() * gameState.getBoard().getWidth()
        
        return (maxMoves + 1) - gameState.getGameHistory().getMoveCount()
    
    def getLooseReward(self, gameState : GameState) :
        
        maxMoves : int = gameState.getBoard().getHeight() * gameState.getBoard().getWidth()
        
        return gameState.getGameHistory().getMoveCount() - (maxMoves + 1)
       