from modules.models.board_game.components.move import Move
from typing import Optional

class TranspositionTableEntry:

    """
    A final immutable class to represent an entry in the transposition table.
    """
    
    def __init__(self, depth: int, score: int, move: Optional[Move] = None) -> None:
        
        """
        Initializes the entry.
        
        Parameters:
            depth (int): The depth of the search.
            score (int): The evaluation score.
            move (Optional[Move]): The best move for this state.
            
        Raises:
            TypeError: If depth or score is not an integer.
            ValueError: If depth or score is less than 0.
            TypeError: If move is not a Move object.
        
        Returns:
            None
        """
        
        # Check if depth and score are integers and greater than or equal to 0
        if not isinstance(depth, int) or not isinstance(score, int):
            raise TypeError("depth and score must be integers")
        
        if depth < 0 or score < 0:
            raise ValueError("depth and score must be greater than or equal to 0")
        
        # Check if move is a Move object
        if move is not None and not isinstance(move, Move):
            raise TypeError("move must be a Move object")
        
        # Initialize the attributes
        self.depth: int = depth
        self.score: int = score
        self.move: Optional[Move] = move
        
        return None

class TranspositionTable:
    
    """
    A Transposition Table for caching game state evaluations.
    Implements efficient storage and retrieval using Python's dictionary.
    """

    def __init__(self, size: int) -> None:
        
        """
        Initializes the transposition table.
        
        Parameters:
            size (int): The size of the table.
            
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        
        Returns:
            None
        """
        
        # Check if size is an integer and greater than 0
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        
        if size <= 0:
            raise ValueError("size must be greater than 0")
        
        # Initialize the table and size
        self.table = {}
        self.size = size
        
        return None

    def put(self, key: int, depth: int, score: int, move: Optional[Move] = None) -> bool:
        
        """
        Stores an entry in the table.

        Parameters:
            key (int): The hashed key representing the game state.
            depth (int): The depth of the search.
            score (int): The evaluation score.
            move (Optional[Move]): The best move for this state.
            
        Raises:
            TypeError: If key, depth, or score is not an integer.
            ValueError: If depth or score is less than 0.
            TypeError: If move is not a Move object.

        Returns:
            bool: True if the entry is stored successfully.
        """
        
        # Check if key, depth, and score are integers and greater than or equal to 0
        if not isinstance(key, int) or not isinstance(depth, int) or not isinstance(score, int):
            raise TypeError("key, depth, and score must be integers")
        
        if depth < 0 or score < 0:
            raise ValueError("depth and score must be greater than or equal to 0")
        
        # Check if move is a Move object
        if move is not None and not isinstance(move, Move):
            raise TypeError("move must be a Move object")
        
        # Calculate the entry index
        entryIndex: int = key % self.size
        
        # Store the entry if it does not exist or if the new depth is greater
        existing_entry = self.table.get(entryIndex)
        if existing_entry is None or depth > existing_entry.depth:
            self.table[entryIndex] = TranspositionTableEntry(depth, score, move)
        
        return True

    def get(self, key: int, depth: int) -> Optional[TranspositionTableEntry]:
        
        """
        Retrieves an entry if it matches or exceeds the specified depth.

        Parameters:
            key (int): The hashed key representing the game state.
            depth (int): The minimum depth required for retrieval.
            
        Raises:
            TypeError: If key or depth is not an integer.
            ValueError: If depth is less than 0.

        Returns:
            Optional[TranspositionTableEntry]: The stored entry or None if not found.
        """
        
        # Check if key and depth are integers and greater than or equal to 0
        if not isinstance(key, int) or not isinstance(depth, int):
            raise TypeError("key and depth must be integers")
        
        if depth < 0:
            raise ValueError("depth must be greater than or equal to 0")
        
        # Calculate the entry index
        entryIndex: int = key % self.size
        
        # Retrieve the entry if it matches or exceeds the specified depth
        entry: TranspositionTableEntry = self.table.get(entryIndex)
        if entry and entry.depth >= depth:
            return entry
        
        return None