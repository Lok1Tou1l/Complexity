from PyQt5.QtWidgets import QApplication
from View import View 
from Presenter import Presenter 



if __name__ == '__main__':
    app = QApplication([])

    # Create instances of View and Presenter
    view = View()
    presenter = Presenter(view)
    # Show the view
    view.show()
    app.exec_()
