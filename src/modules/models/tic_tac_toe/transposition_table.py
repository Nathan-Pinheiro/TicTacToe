from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class TranspositionTableEntry:

    """
    A final immutable class to represent an entry in the transposition table.
    
    Attributes:
        depth (int) : The depth of the search.
        isEndedBranch (bool) : If the move leads to a finite state, wich does not needs to be recomputed after
        score (int) : The evaluation score of the game state.
        move (any) : The best move found for the state.
    """
    
    depth : int
    score : int
    move : Optional[any] = None

class TranspositionTable:
    
    """
    A Transposition Table for caching game state evaluations.
    Implements efficient storage and retrieval using Python's dictionary.
    """

    def __init__(self, size : int):
        
        """
        Initializes the transposition table.
        """
        self.__size__ : int = size
        self.table = {}

    def put(self, key: int, depth: int, score: int, move: Optional[any] = None) -> None:
        
        """
        Stores an entry in the table.

        Args:
            key (int): The hashed key representing the game state.
            depth (int): The depth of the search.
            score (int): The evaluation score.
            move (Optional[any]): The best move for this state.
        """
        
        entryIndex : int = key % self.__size__
        
        if not self.table.get(entryIndex) : self.table[entryIndex] = TranspositionTableEntry(depth, score, move)

    def get(self, key: int, depth: int) -> Optional[TranspositionTableEntry]:
        
        """
        Retrieves an entry if it matches or exceeds the specified depth.

        Args:
            key (int): The hashed key representing the game state.
            depth (int): The minimum depth required for retrieval.

        Returns:
            Optional[TranspositionTableEntry]: The stored entry or None if not found.
        """
        
        entryIndex : int = key % self.__size__
        
        entry : TranspositionTableEntry = self.table.get(entryIndex)
        
        if entry and entry.depth >= depth: return entry
        return None