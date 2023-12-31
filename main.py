import sys
from random import randint

from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.qp = QPainter()
        self.do_paint = False

    def initUI(self):
        self.pushButton = QPushButton('Кнопка', self)
        self.pushButton.resize(100, 50)
        self.pushButton.move(50, 50)
        self.setGeometry(0, 0, 800, 800)
        self.pushButton.clicked.connect(self.draw_prep)

    def paintEvent(self, event):
        if not self.do_paint:
            return
        self.qp.begin(self)
        self.draw_circl()
        self.qp.end()

    def draw_circl(self):
        radius = randint(10, 100)
        self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        self.qp.drawEllipse(400 - radius, 400 - radius, radius * 2, radius * 2)
        self.qp.end()

    def draw_prep(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
