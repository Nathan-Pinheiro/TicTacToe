import sys

sys.dont_write_bytecode = True

from modules.GUI.render import App

if __name__ == "__main__":
    app = App("TicTacToe")
    app.mainloop()