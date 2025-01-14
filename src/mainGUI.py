import sys
from modules.GUI.render import App

# Check Python version
required_version = (3, 12, 0)
if sys.version_info < required_version:
    print(f"Python {required_version[0]}.{required_version[1]}.{required_version[2]} or higher is required.")
    sys.exit(1)

if __name__ == "__main__":
    app = App("TicTacToe")
    app.mainloop()