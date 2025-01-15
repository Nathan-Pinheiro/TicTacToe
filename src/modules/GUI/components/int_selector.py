import customtkinter as ctk

class IntSelector(ctk.CTkFrame):
    def __init__(self, parent, min_value=0, max_value=100, initial_value=0, **kwargs):
        super().__init__(parent, **kwargs)
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value
        self.__createWidgets__()

    def __createWidgets__(self):
        self.value_display = ctk.CTkLabel(self, text=str(self.value), width=30, height=50)
        self.value_display.grid(row=0, column=1, padx=10, pady=10)

        self.increment_button = ctk.CTkButton(self, text="+", width=30, command=self.increment_value)
        self.increment_button.grid(row=0, column=2, padx=10, pady=10)

        self.decrement_button = ctk.CTkButton(self, text="-", width=30, command=self.decrement_value)
        self.decrement_button.grid(row=0, column=0, padx=10, pady=10)

    def increment_value(self):
        if self.value < self.max_value:
            self.value += 1
            self.value_display.configure(text=str(self.value))

    def decrement_value(self):
        if self.value > self.min_value:
            self.value -= 1
            self.value_display.configure(text=str(self.value))

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
        self.value_display.configure(text=str(self.value))