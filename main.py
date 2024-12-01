import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class CoffiesInfo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.tab.setHorizontalHeaderItem(0, QTableWidgetItem('id'))
        self.tab.setHorizontalHeaderItem(1, QTableWidgetItem('название сорта'))
        self.tab.setHorizontalHeaderItem(2, QTableWidgetItem('степень обжарк'))
        self.tab.setHorizontalHeaderItem(3, QTableWidgetItem('молотый/в зернах'))
        self.tab.setHorizontalHeaderItem(4, QTableWidgetItem('описание вкуса'))
        self.tab.setHorizontalHeaderItem(5, QTableWidgetItem('цена'))
        self.tab.setHorizontalHeaderItem(6, QTableWidgetItem('объем упаковки'))
        self.showANDupdate.clicked.connect(self.shown)
        self.change.clicked.connect(self.newWindow)

    def shown(self):
        self.tab.setColumnCount(7)
        self.tab.setRowCount(0)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute('''SELECT * FROM coffies''').fetchall()
        for i, row in enumerate(result):
            self.tab.setRowCount(self.tab.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tab.setItem(i, j, QTableWidgetItem(str(elem)))
        con.close()

    def newWindow(self):
        self.wind = ChangeWindow()
        self.wind.show()


class ChangeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.showTab()
        self.closeButton.clicked.connect(self.closeWindow)
        self.add.clicked.connect(self.addCoffee)
        self.save.clicked.connect(self.changeDB)

    def closeWindow(self):
        self.close()

    def addCoffee(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        cur.execute('''INSERT INTO coffies (id, varierties_name, roasting_degree, state, taste_discription, price, volume) 
            VALUES (?, ?, ?, ?, ?, ?, ?)''', (self.table.rowCount() + 1, self.lineEdit.text(), self.lineEdit_4.text(), self.lineEdit_3.text(),
             self.lineEdit_2.text(), self.lineEdit_5.text(), self.lineEdit_6.text()))
        con.commit()
        self.showTab()
        con.close()

    def showTab(self):
        self.table.setColumnCount(7)
        self.table.setRowCount(0)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute('''SELECT * FROM coffies''').fetchall()
        for i, row in enumerate(result):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(elem)))
        con.close()

    def changeDB(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        for i in range(self.table.rowCount()):
            id_row = self.table.item(i, 0).text()
            for j in range(7):
                if j == 0:
                    cur.execute(f'''UPDATE coffies SET id = {id_row} WHERE id = {id_row}''')
                elif j == 1:
                    cur.execute(f'''UPDATE coffies SET varierties_name = '{self.table.item(i, j).text()}' WHERE id = {id_row}''')
                elif j == 2:
                    cur.execute(f'''UPDATE coffies SET roasting_degree = '{self.table.item(i, j).text()}' WHERE id = {id_row}''')
                elif j == 3:
                    cur.execute(f'''UPDATE coffies SET state = '{self.table.item(i, j).text()}' WHERE id = {id_row}''')
                elif j == 4:
                    cur.execute(f'''UPDATE coffies SET taste_discription = '{self.table.item(i, j).text()}' WHERE id = {id_row}''')
                elif j == 5:
                    cur.execute(f'''UPDATE coffies SET price = '{self.table.item(i, j).text()}' WHERE id = {id_row}''')
                elif j == 6:
                    cur.execute(f'''UPDATE coffies SET volume = '{self.table.item(i, j).text()}' WHERE id = {id_row}''')
        con.commit()
        self.showTab()
        con.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffiesInfo()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
