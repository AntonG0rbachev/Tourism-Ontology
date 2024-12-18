import sys

from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(762, 564)
    w.move(200, 100)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())
