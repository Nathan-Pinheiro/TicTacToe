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
        
        Returns:
            move (Move) : the current move
        """        

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

        if(self.__currentMoveIndex__ == -1) : return None
        
        return self.__moves__[self.__currentMoveIndex__]
    
    def addMove(self, move : Move) -> None:
        
        """
        Add a move to the game history.
        
        Parameters :
            move (Move) : the move to add
            
        Returns:
            None
        """

        while(len(self.__moves__) > self.__currentMoveIndex__ + 1) : self.removeLastMove()

        self.__currentMoveIndex__ += 1
        self.__moves__.append(move)
        
        return None
    
    def removeLastMove(self) -> None:
        
        """
        Remove the last move of the game history.
        
        Returns:
            None
        """

        self.removeMove(len(self.__moves__) - 1)
        
        return None
    
    def removeCurrentMove(self) -> None:
        
        """
        Remove the current move of the game history.
        
        Returns:
            None
        """

        self.removeMove(self.__currentMoveIndex__)
        
        return None
    
    def removeMove(self, moveIndex : int) -> None:
        
        """
        Remove a move from the game history, given it's id
        
        Parameters :
            int (index) : the index of the move
            
        Returns:
            None
        """

        del self.__moves__[moveIndex]
        
        return None
    
    def undo(self) -> None :
        
        """
        Allow undoing the last move
        
        Returns:
            None
        """

        if(len(self.__moves__) <= 0) :  raise Exception("Can't go back if you are on the first move !")
        
        self.__currentMoveIndex__ -= 1
        self.removeLastMove()
        
        return None

    def goBack(self) -> None :
        
        """
        Allow moving back to the last move
        
        Returns:
            None
        """
        
        if(self.__currentMoveIndex__ > -1) : self.__currentMoveIndex__ -= 1
        else : raise Exception("Can't go back if you are on the first move !")
        
        return None

    def goNext(self) -> None :
        
        """
        Allow moving forward to the next move
        
        Returns:
            None
        """

        if(self.__currentMoveIndex__ + 1 < len(self.__moves__)) : self.__currentMoveIndex__ += 1
        else : raise Exception("Can't go next if you are on the last move !")
        
        return None