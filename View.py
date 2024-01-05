from PyQt5.QtWidgets import QApplication,QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton, QComboBox, QTextEdit
from PyQt5.QtGui import QIcon



class View(QWidget):
    def __init__(self):
        super().__init__()

        self.array_input = QLineEdit()
        self.sort_button = QPushButton("Sort")
        self.algorithm_dropdown = QComboBox()
        self.display_area = QTextEdit()  # Added display area
        sorted_array_label = QLabel("Sorted Array")
        execution_time_label = QLabel("Execution Time")
        self.execution_time = QTextEdit()  # Added execution time display area
        self.setWindowTitle("Sorting-GUI")

        layout = QVBoxLayout()
        layout.addWidget(self.array_input)
        layout.addWidget(self.algorithm_dropdown)
        layout.addWidget(self.sort_button)
        layout.addWidget(sorted_array_label)
        layout.addWidget(self.display_area)  # Added display area
        layout.addWidget(execution_time_label) 
        layout.addWidget(self.execution_time)  # Added execution time display area

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
