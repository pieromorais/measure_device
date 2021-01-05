from PySide6 import QtCore, QtGui, QtWidgets 

# Class that will construct the handbook tab
class Handbook(QtWidgets.QWidget):
    """ This class will construct the handbook tab in the mainwindow

        Created by Piero

    """
    def __init__(self, tab):
        super().__init__()
        self.tab = tab
    
    def construction(self):
        # This method construct form from
        # the handbook tab

        self.tab.addTab(HandBookLayoutConstructor(), "APP Handbook")

class HandBookLayoutConstructor(QtWidgets.QWidget):
    """
        This class goal is to constructed the layout for the handbook
        tab for the HandBook class. 
        Don't receive any initial parameters

        Created by Piero
    """
    
    def __init__(self):
        super().__init__()

        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

        # The descriptions available as options as the user press some button
        # Describe some importantt topics about EM
        # Describe the features of the measuring device
        # Describe the project and the authors
        self.available_labels = [
            "You can click in the buttons to know more this project",
            "Classical EM",
            "Measument device",
            "About"
        ]
        self.initial_label = QtWidgets.QLabel(
            self.available_labels[0]
            )
        
        # Classical EM button set up
        self.button_classical_em = QtWidgets.QPushButton("Classical EM")
        self.button_classical_em.clicked.connect(self.classical_em_button_method)

        # Measurement device description button set up
        self.button_measure_device = QtWidgets.QPushButton("Measure Device")
        self.button_measure_device.clicked.connect(self.measure_device_button_method)

        # about button set up
        self.button_about = QtWidgets.QPushButton("About")
        self.button_about.clicked.connect(self.about_button_method)
        
        # Setting the position of the buttons in the grid layout
        # and the spam
        self.grid.addWidget(self.initial_label, 1, 0, 1, 3)
        self.grid.addWidget(self.button_classical_em, 0, 0)
        self.grid.addWidget(self.button_measure_device, 0, 1)
        self.grid.addWidget(self.button_about, 0, 2)
    
    @QtCore.Slot()
    # methods to change the label in the handbook tab
    def classical_em_button_method(self):
        return self.initial_label.setText(self.available_labels[1])

    def measure_device_button_method(self):
        return self.initial_label.setText(self.available_labels[2])

    def about_button_method(self):
        return self.initial_label.setText(self.available_labels[3])
