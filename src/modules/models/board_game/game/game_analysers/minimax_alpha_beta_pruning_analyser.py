from modules.models.tic_tac_toe.tic_tac_toe_game_state import GameState
from modules.models.board_game.components.move import Move
from modules.models.board_game.game.game_outcome import GameOutcomeStatus, GameOutcome
from modules.models.board_game.game.game_analyser import GameAnalyser

class AlphaBetaPruningAnalyser(GameAnalyser):
    """
    A class that implements the alpha-beta pruning version of the minimax algorithm to analyze
    and evaluate possible moves in a Tic-Tac-Toe game. This class extends the abstract GameAnalyser
    class and provides specific logic for calculating minimax scores and determining the best move
    with improved performance using alpha-beta pruning.
    """

    def __init__(self, maxDepth: int, debugOn: bool = False) -> None:
        
        """
        Initializes the AlphaBetaPruningAnalyser instance with the given depth and debugging flag.

        Args:
            maxDepth (int): The maximum depth of the search tree for the alpha-beta algorithm.
            debugOn (bool): Optional flag to enable debugging output (default is False).
        """
        
        super().__init__(maxDepth, debugOn)

    def getMovesScores(self, gameState: GameState) -> dict[Move, int]:
        
        """
        Evaluates all possible moves and returns their corresponding alpha-beta pruning scores.

        Args:
            gameState (TicTacToeGameState): The current state of the game.

        Returns:
            dict[Move, int]: A dictionary mapping each possible move to its alpha-beta pruning score.
        """
        
        self.__nodeExplored__ = 0

        maximizingPlayerIndex = gameState.getPlayerToPlayIndex()
        moveScores = {}

        for moveIndex, move in enumerate(gameState.getPossibleMoves()):
            
            gameOutcome : GameOutcomeStatus = gameState.play(move)

            if(gameOutcome.getGameStatus() != GameOutcomeStatus.UNFINISHED) : 
                
                score : int
                
                if gameOutcome.getGameStatus() == GameOutcomeStatus.DRAW : score = 0                 
                elif gameOutcome.getWinner() == maximizingPlayerIndex : score = self.getWinReward(gameState)
                else : score = - self.getWinReward(gameState)

                gameState.undo(move)
                
            else :

                score, _ = self.__minimax__(gameState, self.__depth__ - 1, maximizingPlayerIndex, float('-inf'), float('inf'))
                gameState.undo(move)

            moveScores[move] = score

            if self.__isDebugOn__:
                print(f"Move {moveIndex}: {move}, Score: {score}")

        if self.__isDebugOn__:
            print("Explored : ", self.__nodeExplored__)

        return moveScores


    def getBestMove(self, gameState: GameState) -> Move:
        
        """
        Determines the best move for the current game state based on the alpha-beta pruning algorithm.

        The method finds the move with the highest score for the maximizing player and returns it.

        Args:
            gameState (TicTacToeGameState): The current state of the Tic-Tac-Toe game.

        Returns:
            Move: The best move determined by the alpha-beta pruning algorithm.
        """
        
        self.__nodeExplored__ = 0
        
        bestScore, bestMove = self.__minimax__(gameState, self.__depth__, gameState.getPlayerToPlayIndex())
        
        if self.__isDebugOn__:
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

        possibleMoves = gameState.getPossibleMoves()
        possibleMoves = self.orderMoves(possibleMoves, gameState.getBoard().getWidth(), gameState.getBoard().getHeight())

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

        if(self.__isDebugOn__): print(f"depth : {depth}, bestScore : {bestScore}, bestMove : {bestMove}")

        return bestScore, bestMove

    def orderMoves(self, moves : list[Move], boardWidth : int, boardHeight : int) -> list[Move] :
        
        """
        Order moves from the nearest from the center to the farther

        Args:
            moves (list[Moves]) : the list of moves
            boardWidth int : the board width
            boardHeight int : the board width

        Returns:
            moves (list[Moves]) : the list of moves ordered
        """

        centerColumn = boardWidth // 2
        centerLine = boardHeight // 2
        
        def euclidianDistanceFromCenter(move: Move) -> int: return abs(centerColumn - move.getCoordinate().getColumn()) + abs(centerLine - move.getCoordinate().getLine())
        sortedMoves = sorted(moves, key=lambda move: (euclidianDistanceFromCenter(move), move.getCoordinate().getColumn(), move.getCoordinate().getLine()))
        
        return sortedMoves

    def getWinReward(self, gameState: GameState) -> int:
        
        """
        Calculates the reward score for a winning state.
        Prioritizes faster wins by providing higher scores.

        Args:
            gameState (TicTacToeGameState): The current game state.

        Returns:
            int: The calculated win reward.
        """
        
        maxMoves : int = gameState.getBoard().getHeight() * gameState.getBoard().getWidth()
        score : int = ((maxMoves + 3) - gameState.getBoard().getPieceCount()) // 2

        return score
