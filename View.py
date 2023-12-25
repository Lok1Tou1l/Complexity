from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QComboBox
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QComboBox, QTextEdit

class View(QWidget):
    def __init__(self):
        super().__init__()

        self.array_input = QLineEdit()
        self.sort_button = QPushButton("Sort")
        self.algorithm_dropdown = QComboBox()
        self.display_area = QTextEdit()  # Added display area

        layout = QVBoxLayout()
        layout.addWidget(self.array_input)
        layout.addWidget(self.algorithm_dropdown)
        layout.addWidget(self.sort_button)
        layout.addWidget(self.display_area)  # Added display area

        self.setLayout(layout)



  