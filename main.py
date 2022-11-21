import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.point = self.pushButton.clicked.connect(self.paintEvent())

    def paintEvent(self, event):
        super().paintEvent(event)
        if not self.point:
            return
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 20.0))

        painter.drawPoint(self.point)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())