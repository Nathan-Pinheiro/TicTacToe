import customtkinter as ctk
from typing import Any

from modules.utils.decorator import privatemethod

# ************************************************
# CLASS IntSelector
# ************************************************
# ROLE : This class is used to create a symbol selector
# ************************************************
# VERSION : 1.0
# AUTHOR : Hugo MERY
# DATE : 18/01/2025
# ************************************************

class IntSelector(ctk.CTkFrame):
    
    """
    The integer selector component.
    """
    
    def __init__(self, parent: ctk.CTkFrame, minValue: int = 0, maxValue: int = 100, initialValue: int = 0, **kwargs: dict[str, Any]) -> None:
        
        """
        Initializes the integer selector component.
        
        Parameters:
            parent (ctk.CTkFrame): The parent frame.
            minValue (int): The minimum value.
            maxValue (int): The maximum value.
            initialValue (int): The initial value.
            **kwargs (dict): Additional keyword arguments for the frame.
            
        Raises:
            TypeError: If parent is not a ctk.CTkFrame instance.
            TypeError: If minValue, maxValue, or initialValue is not an integer.
            ValueError: If initialValue is not between minValue and maxValue.

        Returns:
            None
        """
        
        # Check if the parent is a ctk.CTkFrame instance
        if not isinstance(parent, ctk.CTkFrame):
            raise TypeError("parent must be a ctk.CTkFrame instance")
        
        # Call the parent constructor
        super().__init__(parent, **kwargs)
        
        # Check if minValue, maxValue, and initialValue are integers
        if not isinstance(minValue, int) or not isinstance(maxValue, int) or not isinstance(initialValue, int):
            raise TypeError("minValue, maxValue, and initialValue must be integers")
        
        # Check if initialValue is between minValue and maxValue
        if initialValue < minValue or initialValue > maxValue:
            raise ValueError("initialValue must be between minValue and maxValue")
        
        # Define the minValue, maxValue, and initialValue
        self.minValue: int = minValue
        self.maxValue: int = maxValue
        self.value: int = initialValue
        
        # Create the widgets
        self.__createWidgets__()
        
        return None

    @privatemethod
    def __createWidgets__(self) -> bool:
        
        """
        Creates the widgets for the integer selector.
        
        Returns:
            bool: True if the function succeeds, False otherwise
        """
        
        # Create the display of the value
        self.valueDisplay: ctk.CTkLabel = ctk.CTkLabel(self, text=str(self.value), width=30, height=50)
        self.valueDisplay.grid(row=0, column=1, padx=10, pady=10)

        # Create the increment and decrement buttons
        self.incrementButton: ctk.CTkButton = ctk.CTkButton(self, text="+", width=30, command=self.__incrementValue__)
        self.incrementButton.grid(row=0, column=2, padx=10, pady=10)

        self.decrementButton: ctk.CTkButton = ctk.CTkButton(self, text="-", width=30, command=self.__decrementValue__)
        self.decrementButton.grid(row=0, column=0, padx=10, pady=10)
        
        return True

    @privatemethod
    def __incrementValue__(self) -> bool:
        
        """
        Increases the value by 1.
        
        Returns:
            bool: True if the function succeeds, False otherwise.
        """
        
        # Check if the value is less than the maximum value and increment the value
        if self.value < self.maxValue:
            self.value += 1
            self.valueDisplay.configure(text=str(self.value))
            return True
        
        return False

    @privatemethod
    def __decrementValue__(self) -> bool:
        
        """
        Decreases the value by 1.
        
        Returns:
            bool: True if the function succeeds, False otherwise
        """
        
        # Check if the value is greater than the minimum value and decrement the value
        if self.value > self.minValue:
            self.value -= 1
            self.valueDisplay.configure(text=str(self.value))
            return True
        
        return False
    
    def getMinValue(self) -> int:
        
        """
        Gets the minimum value.
        
        Returns:
            int: The minimum value.
        """
        
        return self.minValue
    
    def getMaxValue(self) -> int:
        
        """
        Gets the maximum value.
        
        Returns:
            int: The maximum value.
        """
        
        return self.maxValue
    
    def getRange(self) -> tuple[int, int]:
        
        """
        Gets the range of values.
        
        Returns:
            tuple[int, int]: The range of values.
        """
        
        return (self.minValue, self.maxValue)
    
    def setMinValue(self, minValue: int) -> bool:
        
        """
        Sets the minimum value.
        
        Parameters:
            minValue (int): The minimum value.
            
        Raises:
            TypeError: If minValue is not an integer.

        Returns:
            bool: True if the minimum value is set successfully.
        """
        
        # Check if the minValue is an integer
        if not isinstance(minValue, int):
            raise TypeError("minValue must be an integer")
        
        # Check if the minValue is less than the current value
        if minValue > self.value:
            self.value = minValue
            
        # Check if the minValue is less than the maxValue
        if minValue > self.maxValue:
            self.maxValue = minValue
        
        # Set the minValue
        self.minValue = minValue
        
        return True
    
    def setMaxValue(self, maxValue: int) -> bool:
        
        """
        Sets the maximum value.
        
        Parameters:
            maxValue (int): The maximum value.
            
        Raises:
            TypeError: If maxValue is not an integer.

        Returns:
            bool: True if the maximum value is set successfully.
        """
        
        # Check if the maxValue is an integer
        if not isinstance(maxValue, int):
            raise TypeError("maxValue must be an integer")
        
        # Check if the maxValue is greater than the current value
        if maxValue < self.value:
            self.value = maxValue
            
        # Check if the maxValue is greater than the minValue
        if maxValue < self.minValue:
            self.minValue = maxValue
        
        # Set the maxValue
        self.maxValue = maxValue
        
        return

    def getValue(self) -> int:
        
        """
        Gets the current value.
        
        Returns:
            int: The current value.
        """
        
        return self.value
    
    def setValue(self, value: int) -> bool:
        
        """
        Sets the value of the integer selector.
        
        Parameters:
            value (int): The value to set.
            
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not between minValue and maxValue.

        Returns:
            bool: True if the value is set successfully
        """
        
        # Check if the value is an integer
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        
        # Check if the value is between minValue and maxValue
        if value < self.minValue or value > self.maxValue:
            raise ValueError("value must be between minValue and maxValue")
        
        # Set the value and update the display
        self.value = value
        
        self.valueDisplay.configure(text=str(self.value))
        
        return True