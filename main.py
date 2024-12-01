import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class CoffiesInfo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.shown)

    def shown(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffiesInfo()
    ex.show()
    sys.exit(app.exec())