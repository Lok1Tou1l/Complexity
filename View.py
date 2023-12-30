from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QComboBox
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QComboBox, QTextEdit
from PyQt5.QtGui import QIcon


class View(QWidget):
    def __init__(self):
        super().__init__()

        self.array_input = QLineEdit()
        self.sort_button = QPushButton("Sort")
        self.algorithm_dropdown = QComboBox()
        self.display_area = QTextEdit()  # Added display area
        self.setWindowTitle("Sorting-GUI")

        layout = QVBoxLayout()
        layout.addWidget(self.array_input)
        layout.addWidget(self.algorithm_dropdown)
        layout.addWidget(self.sort_button)
        layout.addWidget(self.display_area)  # Added display area

        self.setLayout(layout)
        self.setWindowIcon(QIcon('icon.png'))  # Set window icon
        self.setStyleSheet("""
            QWidget {
                background-color: #333333;
                color: #ffffff;
            }
            
            QLineEdit, QTextEdit {
                background-color: #555555;
                color: #ffffff;
                border: 1px solid #ffffff;
            }
            
            QPushButton {
                background-color: #555555;
                color: #blue;
                border: 1px solid #ffffff;
                padding: 5px;
            }
            
            QComboBox {
                background-color: #555555;
                color: #ffffff;
                border: 1px solid #ffffff;
                padding: 5px;
            }
        """)




  