from application.handlers import (
    open_tours,
    open_services,
    open_tours_and_services,
    open_recommend
)

from owlready2 import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Рекомендательная система")

        self.tours_button = QPushButton('Все туры')
        self.services_button = QPushButton('Все услуги')
        self.services_and_tours_button = QPushButton('Туры и сервисы')
        self.process_button = QPushButton("Рекомендовать тур")
        self.tours_button.clicked.connect(open_tours)
        self.services_button.clicked.connect(open_services)
        self.services_and_tours_button.clicked.connect(open_tours_and_services)
        self.process_button.clicked.connect(open_recommend)

        layout = QVBoxLayout()
        layout.addWidget(self.tours_button)
        layout.addWidget(self.services_button)
        layout.addWidget(self.services_and_tours_button)
        layout.addWidget(self.process_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
