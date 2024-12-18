import sys

from application.result import ResultDialog

from owlready2 import *
from PyQt5.QtWidgets import *

onto = get_ontology("../resources/OntoOctavius.owl").load()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Рекомендательная сеть")

        self.label1 = QLabel("Задача + характеристика:")
        self.entry1 = QLineEdit()
        self.entry2 = QLineEdit()

        self.process_button = QPushButton("Рекомендовать")
        self.process_button.clicked.connect(self.process_data)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.entry1)
        layout.addWidget(self.entry2)
        layout.addWidget(self.process_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def process_data(self):
        input1 = self.entry1.text().strip()
        input2 = self.entry2.text().strip()
        f1 = 0
        f2 = 0
        result = 'Не найдено в базе'

        if not input1 or not input2:
            QMessageBox.critical(self, "Ошибка", "Поля пустые")
            return

        # Проверка наличия задачи и характеристики
        for el in onto.Задача.instances():
            if onto.Задача(el.name).Название_задачи == input1:
                f1 = 1
        for t1 in onto.Характеристика.instances():
            if onto.Характеристика(t1.name).Название_характеристики[0] == input2:
                f2 = 1

        if f1 * f2:
            sp = set()
            for el in onto.Задача.instances():
                for im in onto.Задача(el.name).Решается:
                    for il in onto.Метод(im.name).Имеет_достоинство:
                        if onto.Преимущества(il.name).Название_преимущества == input2:
                            sp.add(onto.Метод(im.name).Название_метода)
                            break
            result = list(sp)

        result_dialog = ResultDialog(result)
        result_dialog.exec_()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
