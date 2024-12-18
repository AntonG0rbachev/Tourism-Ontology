from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout


class ResultDialog(QDialog):
    def __init__(self, result, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Result")

        result_label = QLabel(f"Result: {result}")
        layout = QVBoxLayout()
        layout.addWidget(result_label)
        self.setLayout(layout)
