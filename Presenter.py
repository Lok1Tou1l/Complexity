from PyQt5.QtCore import QObject, pyqtSlot 
from View import View as view 
from Model import Model as model
from PyQt5.QtCore import QObject, pyqtSlot

class Presenter(QObject):
    def __init__(self, view):
        super().__init__()

        self.view = view 
        self.view.sort_button.clicked.connect(self.sort_array)
        algorithmes = ["Bubble Sort","Merge Sort","Insertion Sort","Quick Sort","Bogo Sort"]
        self.view.algorithm_dropdown.addItems(algorithmes)

    @pyqtSlot()
    def sort_array(self):
        algorithm_dropdown = self.view.algorithm_dropdown.currentText()
        arr = self.view.array_input.text().split(",")
        arr = [int(x) for x in arr]

        if algorithm_dropdown == "Bubble Sort":
            sorted_arr,execution_time = model.bubble_sort(arr)
            self.view.display_area.setText("\n".join(str(x) for x in sorted_arr))
            self.view.execution_time.setText(str(execution_time))
        if algorithm_dropdown == "Merge Sort":
            sorted_arr,execution_time = model.merge_sort(arr)
            self.view.display_area.setText("\n".join(str(x) for x in sorted_arr))
            self.view.execution_time.setText(str(execution_time))
        if algorithm_dropdown == "Insertion Sort":
            sorted_arr,execution_time = model.insertion_sort(arr)
            self.view.display_area.setText("\n".join(str(x) for x in sorted_arr))
            self.view.execution_time.setText(str(execution_time))
        if algorithm_dropdown == "Quick Sort":
            sorted_arr,execution_time = model.quick_sort(arr)
            self.view.display_area.setText("\n".join(str(x) for x in sorted_arr))
            self.view.execution_time.setText(str(execution_time))
        if algorithm_dropdown == "Bogo Sort":
            sorted_arr,execution_time = model.bogo_sort(arr)
            self.view.display_area.setText("\n".join(str(x) for x in sorted_arr))
            self.view.execution_time.setText(str(execution_time))
     