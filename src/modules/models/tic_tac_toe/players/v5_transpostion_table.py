from modules.models.tic_tac_toe.player import Player
from modules.models.tic_tac_toe.game_state import GameState
from modules.models.console_displayer import *
from modules.models.tic_tac_toe.move import Move
from modules.models.tic_tac_toe.game_outcome import GameOutcomeStatus
from modules.models.tic_tac_toe.transposition_table import TranspositionTable
import random
import os

class MinimaxTranspositionTablePlayer(Player):
    
    def __init__(self, maxDepth : int, debugOn : bool = False, transpositionTableSize : int = 2_048) -> None:
        
        super().__init__("Minimax AI")
        
        self.__maxDepth__  : int = maxDepth
        self.__debugOn__ : bool = debugOn
        self.__transpositionTable__ = TranspositionTable(size = transpositionTableSize)
    
    def get_choice(self, gameState : GameState) -> Move:
        
        self.__nodeExplored__ = 0
        
        bestScore, bestMove = self.__minimax__(gameState, self.__maxDepth__, gameState.getPlayerToPlayIndex())   

        if(self.__debugOn__):
            
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
        
        cached_entry = self.__transpositionTable__.get(gameState.getBoard().__hash__(), depth)
        if cached_entry != None : return cached_entry.score, cached_entry.move

        if depth == 0 : return gameState.evaluateForPlayer(playerIndex), None

        bestScore = None
        bestMove = None

        possibleMoves = gameState.getPossibleMoves()
        possibleMoves = self.orderMoves(possibleMoves, gameState.getBoard())

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
                        
                        bestScore = nextScore
                        bestMove = currentMove
                        
                    alpha = max(alpha, bestScore)
                    
                else :

                    if bestScore == None or nextScore < bestScore:
                        
                        bestScore = nextScore
                        bestMove = currentMove
                        
                    beta = min(beta, bestScore)

                moveIndex += 1

        self.__transpositionTable__.put(gameState.getBoard().__hash__(), depth, bestScore, bestMove)
        return bestScore, bestMove

    def orderMoves(self, moves : list[Move], board : Board) -> list[Move] :
        
        centerColumn = board.getWidth() // 2
        centerLine = board.getHeight() // 2
        
        def euclidianDistanceFromCenter(move: Move) -> int: return abs(centerColumn - move.getCoordinate().getColumn()) + abs(centerLine - move.getCoordinate().getLine())
        sortedMoves = sorted(moves, key=lambda move: (euclidianDistanceFromCenter(move), move.getCoordinate().getColumn(), move.getCoordinate().getLine()))
        
        return sortedMoves

    def getWinReward(self, gameState : GameState) :
        
        maxMoves : int = gameState.getBoard().getHeight() * gameState.getBoard().getWidth()
        return (maxMoves + 1) - gameState.getGameHistory().getMoveCount()
    
    def getLooseReward(self, gameState : GameState) :
        
        maxMoves : int = gameState.getBoard().getHeight() * gameState.getBoard().getWidth()
        return gameState.getGameHistory().getMoveCount() - (maxMoves + 1)