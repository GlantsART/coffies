import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class CoffiesInfo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.tab.setColumnCount(7)
        self.tab.setRowCount(0)
        self.tab.setHorizontalHeaderItem(0, QTableWidgetItem('id'))
        self.tab.setHorizontalHeaderItem(1, QTableWidgetItem('название сорта'))
        self.tab.setHorizontalHeaderItem(2, QTableWidgetItem('степень обжарк'))
        self.tab.setHorizontalHeaderItem(3, QTableWidgetItem('молотый/в зернах'))
        self.tab.setHorizontalHeaderItem(4, QTableWidgetItem('описание вкуса'))
        self.tab.setHorizontalHeaderItem(5, QTableWidgetItem('цена'))
        self.tab.setHorizontalHeaderItem(6, QTableWidgetItem('объем упаковки'))
        self.pushButton.clicked.connect(self.shown)

    def shown(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute('''SELECT * FROM coffies''').fetchall()
        for i, row in enumerate(result):
            self.tab.setRowCount(self.tab.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tab.setItem(i, j, QTableWidgetItem(str(elem)))
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffiesInfo()
    ex.show()
    sys.exit(app.exec())