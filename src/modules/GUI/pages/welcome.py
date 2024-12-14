import tkinter as tk
from tkinter import ttk
import sv_ttk

class Welcome(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configuration de la grille principale
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)  # Augmenter la place du texte
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)  # Diminuer la place de la colonne 1

        # Titre "Tic Tac Toe"
        self.title_label = ttk.Label(self, text="Tic Tac Toe", font=("Arial", 48, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(10, 0), sticky="n")

        # Texte Lorem Ipsum
        self.text_label = ttk.Label(self, 
                                    text=("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent rutrum tellus "
                                          "non ante euismod, id blandit massa auctor. Quisque urna tellus, sodales at ante nec," 
                                          " pharetra tincidunt ante."), 
                                    wraplength=400, 
                                    justify="left",
                                    font=("Arial", 12))
        self.text_label.grid(row=1, column=0, pady=(5, 5), padx=10, sticky="nw")  # Réduction des paddings

        # Canvas unique pour la grille et les symboles
        self.grid_canvas = tk.Canvas(self, bg="#333", highlightthickness=0)
        self.grid_canvas.grid(row=1, column=1, pady=0, padx=10, sticky="nsew")  # Réduire l'écart de padding

        # Bouton "Start Game"
        self.start_button = ttk.Button(self, text="Start Game", command=self.start_game)
        self.start_button.grid(row=2, column=0, columnspan=2, pady=20, sticky="s")

        # Redimensionnement dynamique
        self.bind("<Configure>", self.on_resize)

        # Thème sombre
        sv_ttk.set_theme("dark")

    def draw_grid(self, size):
        """Dessine la grille avec les symboles."""
        self.grid_canvas.delete("all")  # Efface le canvas

        # Taille des cellules
        cell_size = size // 3

        # Dessiner le carré gris (fond)
        self.grid_canvas.create_rectangle(0, 0, size, size, fill="#333", outline="")

        # Dessin des lignes blanches (horizontal et vertical)
        for i in range(1, 3):
            # Lignes horizontales
            self.grid_canvas.create_line(0, i * cell_size, size, i * cell_size, fill="white", width=3)
            # Lignes verticales
            self.grid_canvas.create_line(i * cell_size, 0, i * cell_size, size, fill="white", width=3)

        # Dessin des symboles (ici X, O, Triangle dans les cases de la première ligne)
        self.draw_x(0, 0, cell_size)
        self.draw_o(cell_size, 0, cell_size)
        self.draw_triangle(2 * cell_size, 0, cell_size)

    def draw_x(self, x, y, size):
        """Dessine un X centré dans une cellule."""
        margin = size * 0.2
        self.grid_canvas.create_line(x + margin, y + margin, x + size - margin, y + size - margin, fill="white", width=4)
        self.grid_canvas.create_line(x + margin, y + size - margin, x + size - margin, y + margin, fill="white", width=4)

    def draw_o(self, x, y, size):
        """Dessine un O centré dans une cellule."""
        margin = size * 0.2
        self.grid_canvas.create_oval(x + margin, y + margin, x + size - margin, y + size - margin, outline="white", width=4)

    def draw_triangle(self, x, y, size):
        """Dessine un triangle centré dans une cellule."""
        half = size // 2
        margin = size * 0.2
        self.grid_canvas.create_polygon(
            x + half, y + margin,
            x + margin, y + size - margin,
            x + size - margin, y + size - margin,
            outline="white", width=4, fill="")

    def on_resize(self, event):
        """Redessine le morpion de manière responsive."""
        # Calculer la taille du carré en fonction de la fenêtre
        size = min(event.width, event.height) * 0.5  # Taille du canvas (50% de la fenêtre)
        size = int(size) - (int(size) % 3)  # Garantir que la taille est un multiple de 3

        # Mettre à jour la taille du canvas
        self.grid_canvas.config(width=size, height=size)

        # Placer le canvas sur la partie droite de la fenêtre (en haut à droite)
        self.grid_canvas.place(x=event.width - size - 10, y=(event.height - size) // 2)  # Ajuster la marge à droite

        # Redessiner la grille et les symboles
        self.draw_grid(size)

    def start_game(self):
        print("Starting the game...")

# Lancement de l'application
if __name__ == "__main__":
    class App(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("Tic Tac Toe - Welcome")
            self.geometry("800x600")
            self.frame = Welcome(self, self)
            self.frame.pack(fill="both", expand=True)

    app = App()
    app.mainloop()