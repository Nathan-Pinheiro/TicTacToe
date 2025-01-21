from dataclasses import dataclass
from typing import Optional

class TranspositionTableEntry:

    """
    A final immutable class to represent an entry in the transposition table.
    """
    
    def __init__(self, depth, score, move = None) -> None:
        
        """
        Initializes the entry.
        
        Parameters:
            depth (int): The depth of the search.
            score (int): The evaluation score.
            move (Optional[any]): The best move for this state.
            
        Returns:
            None
        """
        
        self.depth : int = depth
        self.score : int = score
        self.move : Optional[any] = move
        
        return None

class TranspositionTable:
    
    """
    A Transposition Table for caching game state evaluations.
    Implements efficient storage and retrieval using Python's dictionary.
    """

    def __init__(self, size : int) -> None:
        
        """
        Initializes the transposition table.
        
        Parameters:
            size (int): The size of the table.
            
        Returns:
            None
        """
        
        self.table = {}
        self.size = size
        
        return None

    def put(self, key: int, depth: int, score: int, move: Optional[any] = None) -> None:
        
        """
        Stores an entry in the table.

        Parameters:
            key (int): The hashed key representing the game state.
            depth (int): The depth of the search.
            score (int): The evaluation score.
            move (Optional[any]): The best move for this state.
            
        Returns:
            None
        """
        
        entryIndex : int = key % self.size
        
        existing_entry = self.table.get(entryIndex)
        if existing_entry is None or depth > existing_entry.depth: self.table[entryIndex] = TranspositionTableEntry(depth, score, move)
        
        return None

    def get(self, key: int, depth: int) -> Optional[TranspositionTableEntry]:
        
        """
        Retrieves an entry if it matches or exceeds the specified depth.

        Parameters:
            key (int): The hashed key representing the game state.
            depth (int): The minimum depth required for retrieval.

        Returns:
            Optional[TranspositionTableEntry]: The stored entry or None if not found.
        """
        
        entryIndex : int = key % self.size
        entry : TranspositionTableEntry = self.table.get(entryIndex)
        
        # if entry and ((not (-1 < entry.score < 1)) or entry.depth >= depth): return entry
        if entry and entry.depth >= depth : return entry
        
        return None