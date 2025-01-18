import customtkinter as ctk

from modules.utils.decorator import privatemethod

class IntSelector(ctk.CTkFrame):
    
    """
    The integer selector component.
    """
    
    def __init__(self, parent: ctk.CTkFrame, minValue: int = 0, maxValue: int = 100, initialValue: int = 0, **kwargs) -> None:
        
        """
        Initializes the integer selector component.
        
        Parameters:
            parent (ctk.CTkFrame): The parent frame.
            minValue (int): The minimum value.
            maxValue (int): The maximum value.
            initialValue (int): The initial value.

        Returns:
            None
        """
        
        super().__init__(parent, **kwargs)
        self.minValue: int = minValue
        self.maxValue: int = maxValue
        self.value: int = initialValue
        self.__createWidgets__()
        
        return None

    @privatemethod
    def __createWidgets__(self) -> bool:
        
        """
        Creates the widgets for the integer selector.
        
        Returns:
            bool: True if the function succeeds, False otherwise
        """
        
        self.valueDisplay: ctk.CTkLabel = ctk.CTkLabel(self, text=str(self.value), width=30, height=50)
        self.valueDisplay.grid(row=0, column=1, padx=10, pady=10)

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
        
        if self.value > self.minValue:
            self.value -= 1
            self.valueDisplay.configure(text=str(self.value))
            return True
        return False

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

        Returns:
            bool: True if the value is set successfully
        """
        
        self.value = value
        self.valueDisplay.configure(text=str(self.value))
        return True