import sys
from PyQt6.QtWidgets import QApplication
from game_window import GameWindow

def main():
    app = QApplication(sys.argv)
    game_window = GameWindow()
    game_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
