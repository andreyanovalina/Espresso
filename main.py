import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.con = sqlite3.connect("coffee.db")

    def run(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM espresso").fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'title_ofvariety', 'degree_of_roasting',
                                                    'type', 'description_of_taste', 'price', 'volume_of_packaging'])
        i = 0  # Используется для обозначения координаты ячейки при занесении значений
        for elem in result:
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j in range(7):  # Кол-во столбцов: 4
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem[j])))
            i += 1
        self.tableWidget.resizeColumnsToContents()
        self.con.commit()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())