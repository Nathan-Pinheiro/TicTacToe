from modules.models.board_game.components.move import Move

# ************************************************
# CLASS GameHistory
# ************************************************
# ROLE : This class is used to store all moves in a game
# ************************************************
# VERSION : 1.0
# AUTHOR : Nathan PINHEIRO
# DATE : 13/01/2025
# ************************************************

class GameHistory:
    
    """
    A class that is used to store all moves in a game
    """

    def __init__(self) -> None:
        
        """
        The constructor of a GameHistory object
        
        Returns:
            None
        """

        # Initialize the moves list and the current move index
        self.__moves__ : list[Move] = []
        self.__currentMoveIndex__ : int = -1
        
        return None

    def getMoveCount(self) -> int:

        """
        Returns the number of move in the game history
        
        Returns:
            moveCount (int) : the number of moves in the game history
        """

        return len(self.__moves__)
    
    def getCurrentMoveIndex(self) -> Move:

        """
        Get the index of the current move.
        
        Returns:
            currentMoveIndex (int) : the index of the current move
        """

        return self.__currentMoveIndex__

    def getMove(self, moveIndex : int) -> Move:

        """
        Get the move at a given index of the game history.
        
        Parameters:
            moveIndex (int) : the current move
            
        Raises:
            ValueError: If moveIndex is not an integer.
            ValueError: If moveIndex is not a valid index.
        
        Returns:
            move (Move) : the current move
        """        
        
        # Check if moveIndex is an integer
        if not isinstance(moveIndex, int):
            raise ValueError("moveIndex must be an integer")
        
        # Check if moveIndex is a valid index
        if moveIndex < 0 or moveIndex >= len(self.__moves__):
            raise ValueError("moveIndex must be a valid index")

        return self.__moves__[moveIndex]
    
    def getMoves(self) -> list[Move]:
        
        """
        Get all the moves in the game history.
        
        Returns:
            moves (list[Move]) : the list of all moves
        """

        return self.__moves__
        
    def getCurrentMove(self) -> Move | None:
        
        """
        Get the current move.
        
        Returns:
            move (Move) : the current move if there is one, None otherwise
        """

        # Check if there is a current move
        if(self.__currentMoveIndex__ == -1) : return None
        
        return self.__moves__[self.__currentMoveIndex__]
    
    def addMove(self, move : Move) -> bool:
        
        """
        Add a move to the game history.
        
        Parameters :
            move (Move) : the move to add
            
        Returns:
            bool: True if the move is added successfully.
        """
        
        # Check if move is a Move instance
        if not isinstance(move, Move):
            raise ValueError("move must be a Move instance")

        # Remove all moves after the current move
        while(len(self.__moves__) > self.__currentMoveIndex__ + 1) : self.removeLastMove()

        # Add the move to the game history
        self.__currentMoveIndex__ += 1
        self.__moves__.append(move)
        
        return True
    
    def removeLastMove(self) -> bool:
        
        """
        Remove the last move of the game history.
        
        Returns:
            bool: True if the move is removed successfully.
        """

        # Remove the last move
        self.removeMove(len(self.__moves__) - 1)
        
        return True
    
    def removeCurrentMove(self) -> bool:
        
        """
        Remove the current move of the game history.
        
        Returns:
            bool: True if the move is removed successfully
        """

        # Remove the current move
        self.removeMove(self.__currentMoveIndex__)
        
        return True
    
    def removeMove(self, moveIndex : int) -> bool:
        
        """
        Remove a move from the game history, given it's id
        
        Parameters :
            int (index) : the index of the move
            
        Raises:
            ValueError: If moveIndex is not an integer.
            ValueError: If moveIndex is not a valid index.
            
        Returns:
            bool: True if the move is removed successfully
        """

        # Check if moveIndex is an integer
        if not isinstance(moveIndex, int):
            raise ValueError("moveIndex must be an integer")
        
        # Check if moveIndex is a valid index
        if moveIndex < 0 or moveIndex >= len(self.__moves__):
            raise ValueError("moveIndex must be a valid index")
        
        # Remove the move
        del self.__moves__[moveIndex]
        
        return True
    
    def undo(self) -> bool :
        
        """
        Allow undoing the last move
        
        Raises:
            Exception: If there is no move to undo
        
        Returns:
            bool: True if the move is undone successfully
        """

        # Check if there is a move to undo
        if(len(self.__moves__) <= 0) :  raise Exception("Can't go back if you are on the first move !")
        
        # Update the current move index
        self.__currentMoveIndex__ -= 1
        
        # Remove the last move
        self.removeLastMove()
        
        return True

    def goBack(self) -> bool :
        
        """
        Allow moving back to the last move
        
        Raises:
            Exception: If there is no move to go back to
        
        Returns:
            bool: True if the move is undone successfully
        """
        
        # Check if there is a move to go back to
        if(self.__currentMoveIndex__ > -1) : self.__currentMoveIndex__ -= 1
        else : raise Exception("Can't go back if you are on the first move !")
        
        return True

    def goNext(self) -> bool :
        
        """
        Allow moving forward to the next move
        
        Raises:
            Exception: If there is no move to go next to
        
        Returns:
            bool: True if the move is undone successfully
        """

        # Check if there is a move to go next to
        if(self.__currentMoveIndex__ + 1 < len(self.__moves__)) : self.__currentMoveIndex__ += 1
        else : raise Exception("Can't go next if you are on the last move !")
        
        return True