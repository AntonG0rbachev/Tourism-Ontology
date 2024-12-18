from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout


class ToursDialog(QDialog):
    def __init__(self, result, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Все доступные туры")

        result_label = QLabel(f"{result}")
        layout = QVBoxLayout()
        layout.addWidget(result_label)
        self.setLayout(layout)
