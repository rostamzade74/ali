import sys
from PyQt6.QtWidgets import QApplication
try:
    from .ui import MainWindow
except ImportError:  # when executed directly from src directory
    from ui import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
