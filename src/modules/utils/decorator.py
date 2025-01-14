from typing import Callable, Any
import warnings
import functools

def privatemethod(func: Callable) -> Callable:
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

def deprecated_class(cls):
    
    """
    A decorator to warn user that the class is deprecated.
    """
    
    @functools.wraps(cls)
    
    def wrapper(*args, **kwargs):
        
        warnings.warn(
            f"{cls.__name__} is deprecated and will be removed in future versions.",
            DeprecationWarning,
            stacklevel=2
        )
        
        return cls(*args, **kwargs)
    
    return wrapper

def override(method):
    
    """
    A decorator to ensure that a method overrides a method in the superclass.
    """
    
    def wrapper(self, *args, **kwargs):
        
        for base_class in self.__class__.__bases__:
            
            if hasattr(base_class, method.__name__) : return method(self, *args, **kwargs)
            
        raise NotImplementedError(f"Method '{method.__name__}' does not override any method in superclass.")
    
    return wrapper