from typing import Callable, Any

def private_method(func: Callable) -> Callable:
    """Decorator to mark a method as private.
    
    Args:
        func (function): The method to be marked as private.
        
    Returns:
        function: The wrapped method.
        
    """
    
    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        """Verifies if the method is private and raises an error if it is accessed directly.

        Raises:
            AttributeError: Method %name% is private and cannot be accessed directly.

        Returns:
            Any: The result of the method.
        """
        
        if not func.__name__.startswith("_"): 
            raise AttributeError(f"Method {func.__name__} is private and cannot be accessed directly.")
        return func(*args, **kwargs)
    
    return wrapper