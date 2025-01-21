from typing import Callable, Any
import warnings
import functools

def privatemethod(func: Callable) -> Callable:
    
    """
    Decorator to mark a method as private.
    
    Parameters:
        func (function): The method to be marked as private.
        
    Returns:
        function: The wrapped method.
    """
    
    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        
        """
        Verifies if the method is private and raises an error if it is accessed directly.

        Parameters:
            *args (tuple): The arguments of the method.
            **kwargs (dict): The keyword arguments of the method.

        Returns:
            Any: The result of the method.
        """
        
        if not func.__name__.startswith("_"): 
            raise AttributeError(f"Method {func.__name__} is private and cannot be accessed directly.")
        return func(*args, **kwargs)
    
    return wrapper

def deprecated_class(cls: classmethod) -> Callable:
    
    """
    A decorator to warn user that the class is deprecated.
    
    Parameters:
        cls (classmethod): The class to be marked as deprecated.
        
    Returns:
        function: The wrapped class.
    """
    
    @functools.wraps(cls)
    
    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        
        """
        Verifies if the class is deprecated and raises a warning if it is accessed.
        
        Parameters:
            *args (tuple): The arguments of the class.
            **kwargs (dict): The keyword arguments of the class.
        
        Returns:
            Any: The result of the class.
        """
        
        warnings.warn(
            f"{cls.__name__} is deprecated and will be removed in future versions.",
            DeprecationWarning,
            stacklevel=2
        )
        
        return cls(*args, **kwargs)
    
    return wrapper

def override(method: Callable) -> Callable:
    
    """
    A decorator to ensure that a method overrides a method in the superclass.
    
    Parameters:
        method (function): The method to be checked.
        
    Returns:
        function: The wrapped method.
    """
    
    def wrapper(self, *args: tuple, **kwargs: dict) -> Any:
        
        """
        Verifies if the method overrides a method in the superclass.
        
        Parameters:
            self (object): The object that contains the method.
            *args (tuple): The arguments of the method.
            **kwargs (dict): The keyword arguments of the method.
            
        Returns:
            Any: The result of the method.
        """
        
        for base_class in self.__class__.__bases__:
            
            if hasattr(base_class, method.__name__) : return method(self, *args, **kwargs)
            
        raise NotImplementedError(f"Method '{method.__name__}' does not override any method in superclass.")
    
    return wrapper