from modules.models.tic_tac_toe.players.ai_player import AIPlayer
from modules.models.tic_tac_toe.tic_tac_toe_player import Player
from modules.models.tic_tac_toe.tic_tac_toe_game_state import TicTacToeGameState
from modules.models.utils.console_displayer import *
from modules.models.board_game.components.move import Move
from modules.models.board_game.game.game_outcome import GameOutcomeStatus
from modules.models.board_game.board.board import Board
from modules.models.board_game.components.transposition_table import TranspositionTable

# ************************************************
# CLASS MinimaxTranspositionTablePlayer
# ************************************************
# ROLE : This AI can return the best moove for a given tic tac toe position
# runnning the minimax alpha beta algorithm, by doing middle moves first and using a transposition table mechanism
# ************************************************
# VERSION : 0.0 (in progress)
# AUTHOR : Nathan PINHEIRO
# DATE : 10/01/2025
# ************************************************

class MinimaxTranspositionTablePlayer(AIPlayer):
    
    def __init__(self, maxDepth : int, debugOn : bool = False, transpositionTableSize : int = 4_009_600) -> None:
        
        super().__init__("Minimax AI")
        
        self.__maxDepth__  : int = maxDepth
        self.__debugOn__ : bool = debugOn
        self.__transpositionTable__ = TranspositionTable(size = transpositionTableSize)
    
    def get_choice(self, gameState : TicTacToeGameState) -> Move:
        
        self.__nodeExplored__ = 0

        bestScore, bestMove = self.__minimax__(gameState, self.__maxDepth__, gameState.getPlayerToPlayIndex())   

        if(self.__debugOn__):
            
            print("Explored : ", self.__nodeExplored__)
            print("Best score : ", bestScore)
        
        return bestMove
    
    def __minimax__(self, gameState: TicTacToeGameState, depth: int, playerIndex: int, alpha: int = float('-inf'), beta: int = float('inf'), debugOn = False) -> tuple[int, Move]:
        
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
        if(gameState.getBoard().isFull()) : return 0, None

        maxPossibleScore : int = self.getWinReward(gameState)
        
        # cached_entry = self.__transpositionTable__.get(hash(gameState.getBoard()), depth)
        # if cached_entry != None : return cached_entry.score, cached_entry.move

        bestScore : int = None
        bestMove : int = None

        possibleMoves = gameState.getPossibleMoves()
        possibleMoves = self.orderMoves(possibleMoves, gameState.getBoard())

        if(beta > maxPossibleScore) :
            
            beta = maxPossibleScore
            if(alpha >= beta) : return beta, None

        moveIndex = 0
        while moveIndex < len(possibleMoves):

            currentMove : Move = possibleMoves[moveIndex]
            gameOutcome : GameOutcome = gameState.play(currentMove)

            if(gameOutcome.getGameStatus() == GameOutcomeStatus.VICTORY) : 

                score : int
                
                if gameOutcome.getWinner() == playerIndex : score  = self.getWinReward(gameState)
                else : score = - self.getWinReward(gameState)

                display_board(gameState.getBoard())
                print(f"alpha : {alpha}, beta : {beta}")
                print(f"bestScore : {score}, bestMove : {currentMove}")

                gameState.undo(currentMove)

                return score, currentMove

            elif(gameOutcome.getGameStatus() == GameOutcomeStatus.DRAW) : 
                gameState.undo(currentMove)
                return 0, currentMove
            
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

                if(bestScore >= beta) : return bestScore, bestMove
                moveIndex += 1

        self.__transpositionTable__.put(hash(gameState.getBoard()), depth, bestScore, bestMove)
        return bestScore, bestMove

    def orderMoves(self, moves : list[Move], board : Board) -> list[Move] :
        
        centerColumn = board.getWidth() // 2
        centerLine = board.getHeight() // 2
        
        def euclidianDistanceFromCenter(move: Move) -> int: return abs(centerColumn - move.getCoordinate().getColumn()) + abs(centerLine - move.getCoordinate().getLine())
        sortedMoves = sorted(moves, key=lambda move: (euclidianDistanceFromCenter(move), move.getCoordinate().getColumn(), move.getCoordinate().getLine()))
        
        return sortedMoves

    def getWinReward(self, gameState : TicTacToeGameState) :

        maxMoves : int = gameState.getBoard().getHeight() * gameState.getBoard().getWidth()
        score : int = ((maxMoves + 3) - gameState.getBoard().getPieceCount()) // 2

        return score