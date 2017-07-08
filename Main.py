from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MaxNESWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("maxNES")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        title = QLabel("Welcome to maxNES", self)
        title.setAlignment(Qt.AlignCenter)
        gridLayout.addWidget(title, 0, 0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MaxNESWindow()
    mainWin.show()
    sys.exit(app.exec_())