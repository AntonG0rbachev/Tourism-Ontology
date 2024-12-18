from PyQt5.QtWidgets import (
    QDialog,
    QLabel,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QMessageBox
)

from application.result import ResultDialog


class RecommendDialog(QDialog):
    def __init__(self, ontology, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Рекомендовать")
        self.ontology = ontology

        self.label = QLabel('Введите желаемую услугу')
        self.wish_input = QLineEdit()
        self.process_button = QPushButton("Рекомендовать тур")

        self.process_button.clicked.connect(self.open_result)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.wish_input)
        layout.addWidget(self.process_button)
        self.setLayout(layout)

    def open_result(self):
        wish = self.wish_input.text().strip()

        if not wish:
            QMessageBox.critical(self, "Ошибка", "Поле пустое")
            return

        services = self.ontology.get_all_services()

        services_names = list()
        for service in services:
            services_names.append(service.name)

        if wish not in services_names:
            result = f'Услуга {wish} не найдена в базе'
            QMessageBox.critical(self, "Ошибка", result)
            return

        result = self.ontology.get_tours_by_service(wish)
        print(result)
        dialog = ResultDialog(result)
        dialog.exec_()
