from modules.models.tic_tac_toe.players.ai_player import AIPlayer
from modules.models.tic_tac_toe.tic_tac_toe_player import Player
from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.utils.console_displayer import *
from modules.models.board_game.components.move import Move
from modules.models.board_game.game.game_outcome import GameOutcomeStatus
from modules.models.board_game.board.board import Board

# ************************************************
# CLASS MinimaxBetterMoveOrderingPlayer
# ************************************************
# ROLE : This AI can return the best moove for a given tic tac toe position
# runnning the minimax alpha beta algorithm, by doing middle moves first
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 10/01/2025
# ************************************************

class MinimaxBetterMoveOrderingPlayer(AIPlayer):
    
    def __init__(self, maxDepth : int, debugOn : bool = False) -> None:
        
        super().__init__("Minimax AI")
        
        self.__maxDepth__  : int = maxDepth
        self.__debugOn__ : bool = debugOn
    
    def get_choice(self, gameState : TicTacToeGameState) -> Move:
        
        self.__nodeExplored__ = 0
        
        bestScore, bestMove = self.__minimax__(gameState, self.__maxDepth__, gameState.getPlayerToPlayIndex())   

        if(self.__debugOn__):
            
            print("Explored : ", self.__nodeExplored__)
            print("Best score : ", bestScore)
        
        return bestMove
    
    def __minimax__(self, gameState: TicTacToeGameState, depth: int, playerIndex: int, alpha: int = float('-inf'), beta: int = float('inf')) -> tuple[int, Move]:
        
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

        possibleMoves = gameState.getPossibleMoves()
        possibleMoves = self.orderMoves(possibleMoves, gameState.getBoard())

        moveIndex = 0
        while moveIndex < len(possibleMoves) and alpha < beta:
            
            currentMove = possibleMoves[moveIndex]

            gameOutcome = gameState.play(currentMove)
            
            if(gameOutcome.getGameStatus() != GameOutcomeStatus.UNFINISHED) : 
                
                score : int
                
                if gameOutcome.getGameStatus() == GameOutcomeStatus.DRAW : score = 0                 
                elif gameOutcome.getWinner() == playerIndex : score : int = self.getWinReward(gameState)
                else : score : int = - self.getWinReward(gameState)

                gameState.undo(currentMove)
                
                return score, currentMove

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

        if(self.__debugOn__):
            display_board(gameState.getBoard())
            print(f"depth : {depth}, bestScore : {bestScore}, bestMove : {bestMove}")

        return bestScore, bestMove

    def orderMoves(self, moves : list[Move], board : Board) -> list[Move] :
        
        centerColumn = board.getWidth() // 2
        centerLine = board.getHeight() // 2
        
        def euclidianDistanceFromCenter(move: Move) -> int: return abs(centerColumn - move.getCoordinate().getColumn()) + abs(centerLine - move.getCoordinate().getLine())
        sortedMoves = sorted(moves, key=lambda move: (euclidianDistanceFromCenter(move), move.getCoordinate().getColumn(), move.getCoordinate().getLine()))
        
        return sortedMoves

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
        score : int = (maxMoves + 1) - gameState.getGameHistory().getMoveCount()
        
        return score