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

        Parameters:
            maxDepth (int): The maximum depth of the search tree for the alpha-beta algorithm.
            debugOn (bool): Optional flag to enable debugging output (default is False).
            
        Raises:
            ValueError: If maxDepth is not a positive integer.
            TypeError: If debugOn is not a boolean value.
            
        Returns:
            None
        """
        
        # Check if maxDepth is a positive integer
        if not isinstance(maxDepth, int) or maxDepth <= 0:
            raise ValueError("maxDepth must be a positive integer")
        
        # Check if debugOn is a boolean value
        if not isinstance(debugOn, bool):
            raise TypeError("debugOn must be a boolean value")
        
        # Call the parent constructor
        super().__init__(maxDepth, debugOn)
        
        return None

    def getMovesScores(self, gameState: GameState) -> dict[Move, int]:
        
        """
        Evaluates all possible moves and returns their corresponding alpha-beta pruning scores.

        Parameters:
            gameState (TicTacToeGameState): The current state of the game.
            
        Raises:
            TypeError: If gameState is not a TicTacToeGameState instance.

        Returns:
            dict[Move, int]: A dictionary mapping each possible move to its alpha-beta pruning score.
        """
        
        # Check if gameState is a TicTacToeGameState instance
        if not isinstance(gameState, GameState):
            raise TypeError("gameState must be a GameState instance")
        
        # Reset the node explored count
        self.__nodeExplored__ = 0

        # Get the index of the maximizing player
        maximizingPlayerIndex = gameState.getPlayerToPlayIndex()
        moveScores = {}

        # Iterate over all possible moves
        for moveIndex, move in enumerate(gameState.getPossibleMoves()):
            
            # Play the move and get the game outcome
            gameOutcome : GameOutcome = gameState.play(move)

            # Check if the game is finished
            if(gameOutcome.getGameStatus() != GameOutcomeStatus.UNFINISHED) : 
                
                score : int
                
                # Calculate the score based on the game outcome
                if gameOutcome.getGameStatus() == GameOutcomeStatus.DRAW : score = 0                 
                elif gameOutcome.getWinner() == maximizingPlayerIndex : score = self.getWinReward(gameState)
                else : score = - self.getWinReward(gameState)

                # Undo the move and return the score
                gameState.undo(move)
                
            else :
                
                # Recursively evaluate the game state
                score, _ = self.__minimax__(gameState, self.__depth__ - 1, maximizingPlayerIndex, float('-inf'), float('inf'))
                gameState.undo(move)

            # Store the move score in the dictionary
            moveScores[move] = score

            # Print the move and score if debugging is enabled
            if self.__isDebugOn__:
                print(f"Move {moveIndex}: {move}, Score: {score}")

        # Print the number of nodes explored if debugging is enabled
        if self.__isDebugOn__:
            print("Explored : ", self.__nodeExplored__)

        return moveScores


    def getBestMove(self, gameState: GameState) -> Move:
        
        """
        Determines the best move for the current game state based on the alpha-beta pruning algorithm.

        The method finds the move with the highest score for the maximizing player and returns it.

        Parameters:
            gameState (TicTacToeGameState): The current state of the Tic-Tac-Toe game.
            
        Raises:
            TypeError: If gameState is not a TicTacToeGameState instance.

        Returns:
            Move: The best move determined by the alpha-beta pruning algorithm.
        """
        
        # Check if gameState is a TicTacToeGameState instance
        if not isinstance(gameState, GameState):
            raise TypeError("gameState must be a GameState instance")
        
        # Reset the node explored count
        self.__nodeExplored__ = 0
        
        # Get the best score and move using the minimax algorithm
        bestScore, bestMove = self.__minimax__(gameState, self.__depth__, gameState.getPlayerToPlayIndex())
        
        # Print the number of nodes explored and the best score if debugging is enabled
        if self.__isDebugOn__:
            print("Explored : ", self.__nodeExplored__)
            print("Best score : ", bestScore)

        return bestMove

    def __minimax__(self, gameState: GameState, depth: int, playerIndex: int, alpha: int | float = float('-inf'), beta: int | float = float('inf')) -> tuple[int, Move | None]:
        
        """
        Recursively evaluates the game state using the Minimax algorithm.

        Parameters : 
            gameState : Current game state.
            depth : Remaining search depth.
            playerIndex : The index of the maximizing player.
            
        Raises :
            TypeError : If gameState is not a TicTacToeGameState instance.
            ValueError : If depth is not a positive integer.
            TypeError : If playerIndex is not an integer.
            ValueError : If playerIndex is out of range.
            TypeError : If alpha is not an integer or float.
            TypeError : If beta is not an integer or float.
            
        Return : 
            A tuple (score, move), where `score` is the evaluation of the board, and `move` is the best move to play.
        """
        
        # Check if gameState is a TicTacToeGameState instance
        if not isinstance(gameState, GameState):
            raise TypeError("gameState must be a GameState instance")
        
        # Check if depth is a positive integer
        if not isinstance(depth, int) or depth < 0:
            raise ValueError("depth must be a positive integer")
        
        # Check if playerIndex is an integer
        if not isinstance(playerIndex, int):
            raise TypeError("playerIndex must be an integer")
        
        # Check if playerIndex is a valid player index
        if playerIndex < 0 or playerIndex >= gameState.getPlayerCount():
            raise ValueError("playerIndex is out of range")
        
        # Check if alpha and beta are integers or floats
        if not isinstance(alpha, int) and not isinstance(alpha, float):
            raise TypeError("alpha must be an integer or float")
        
        if not isinstance(beta, int) and not isinstance(beta, float):
            raise TypeError("beta must be an integer or float")

        # Increment the node explored count
        self.__nodeExplored__ += 1

        # Check if the search depth is 0
        if depth == 0 : return gameState.evaluateForPlayer(playerIndex), None

        # Initialize the best score and move
        bestScore : int = None
        bestMove : Move = None
        e : int = 0

        # Get the possible moves and order them
        possibleMoves : list[int] = gameState.getPossibleMoves()
        possibleMoves = self.orderMoves(possibleMoves, gameState.getBoard().getWidth(), gameState.getBoard().getHeight())

        # Iterate over the possible moves
        moveIndex  : int = 0
        while moveIndex < len(possibleMoves) and alpha < beta:
            
            # Get the current move and play it to get the game outcome
            currentMove = possibleMoves[moveIndex]

            gameOutcome = gameState.play(currentMove)
            
            # Check if the game is finished
            if(gameOutcome.getGameStatus() != GameOutcomeStatus.UNFINISHED) : 
                
                score : int
                
                # Calculate the score based on the game outcome
                if gameOutcome.getGameStatus() == GameOutcomeStatus.DRAW : score = 0                 
                elif gameOutcome.getWinner() == playerIndex : score : int = self.getWinReward(gameState)
                else : score : int = - self.getWinReward(gameState)

                # Undo the move and return the score and move
                gameState.undo(currentMove)
                
                return score, currentMove

            else :
                
                # Recursively evaluate the game state
                nextScore, _ = self.__minimax__(gameState, depth - 1, playerIndex, alpha, beta)

                # Undo the move and update the best score and move
                gameState.undo(currentMove)

                # Update the best score and move based on the player
                if playerIndex == gameState.getPlayerToPlayIndex():

                    # Maximizing player
                    if bestScore == None or nextScore > bestScore:
                        
                        # Update the best score and move
                        if(bestScore is not None) : e += self.getMoveStrengthToAdd(bestScore) 
                        bestScore = nextScore
                        bestMove = currentMove

                    else : e += self.getMoveStrengthToAdd(nextScore)
                        
                    # Update alpha
                    alpha = max(alpha, bestScore)
                    
                else :
                    
                    # Minimizing player
                    if bestScore == None or nextScore < bestScore:
                        
                        # Update the best score and move
                        if(bestScore is not None) : e += self.getMoveStrengthToAdd(bestScore)
                        bestScore = nextScore
                        bestMove = currentMove
                        
                    else : e += self.getMoveStrengthToAdd(nextScore)
                        
                    # Update beta
                    beta = min(beta, bestScore)

                # Increment the move index
                moveIndex += 1

        # Print the depth, best score, and best move if debugging is enabled
        if(self.__isDebugOn__): print(f"depth : {depth}, bestScore : {bestScore}, bestMove : {bestMove}")

        return bestScore + e, bestMove

    def orderMoves(self, moves : list[Move], boardWidth : int, boardHeight : int) -> list[Move] :
        
        """
        Order moves from the nearest from the center to the farther

        Parameters:
            moves (list[Moves]) : the list of moves
            boardWidth int : the board width
            boardHeight int : the board width
            
        Raises:
            TypeError: If moves is not a list of Move objects
            TypeError: If boardWidth or boardHeight is not an integer
            ValueError: If boardWidth or boardHeight is not a positive integer

        Returns:
            moves (list[Moves]) : the list of moves ordered
        """
        
        # Check if moves is a list of Move objects
        if not all(isinstance(move, Move) for move in moves):
            raise TypeError("moves must be a list of Move objects")
        
        # Check if boardWidth and boardHeight are integers and greater than 0
        if not isinstance(boardWidth, int) or not isinstance(boardHeight, int):
            raise TypeError("boardWidth and boardHeight must be integers")
        
        if boardWidth <= 0 or boardHeight <= 0:
            raise ValueError("boardWidth and boardHeight must be positive integers")
        
        # Calculate the center column and line
        centerColumn = boardWidth // 2
        centerLine = boardHeight // 2
        
        def euclidianDistanceFromCenter(move: Move) -> int: 
            
            """
            Calculate the euclidian distance from the center of the board for a move.
            
            Parameters:
                move (Move): The move to calculate the distance from the center.
                
            Raises:
                TypeError: If move is not a Move object.
                
            Returns:
                int: The euclidian distance from the center of the board.
            """
            
            # Check if move is a Move object
            if not isinstance(move, Move):
                raise TypeError("move must be a Move object")
            
            return abs(centerColumn - move.getCoordinate().getColumn()) + abs(centerLine - move.getCoordinate().getLine())
        
        # Sort the moves by the euclidian distance from the center, then by column, and finally by line
        sortedMoves = sorted(moves, key=lambda move: (euclidianDistanceFromCenter(move), move.getCoordinate().getColumn(), move.getCoordinate().getLine()))
        
        return sortedMoves

    def getWinReward(self, gameState: GameState) -> int:
        
        """
        Calculates the reward score for a winning state.
        Prioritizes faster wins by providing higher scores.

        Parameters:
            gameState (TicTacToeGameState): The current game state.
            
        Raises:
            TypeError: If gameState is not a TicTacToeGameState instance.

        Returns:
            int: The calculated win reward.
        """
        
        # Check if gameState is a TicTacToeGameState instance
        if not isinstance(gameState, GameState):
            raise TypeError("gameState must be a GameState instance")
        
        # Calculate the score based on the number of moves left
        maxMoves : int = gameState.getBoard().getHeight() * gameState.getBoard().getWidth()
        score : int = ((maxMoves + 3) - gameState.getBoard().getPieceCount()) // 2

        return score

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
        if not (isinstance(score, int) or isinstance(score, float)): raise TypeError("score must be an integer")

        return score / 100
