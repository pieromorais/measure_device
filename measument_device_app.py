# This measure device tab has basically two parts
# 1 - Entry fields and some buttons to receive the 
# properties of the magnectic core, and other fields
# and buttons to set some parameters on the microcontroller
# 2 - Some canvas to show the caracteristic curve from the 
# magnectic core

from PySide6 import QtCore, QtGui, QtWidgets

class MeasureDevice(QtWidgets.QWidget):
    """ Class to receive and set some informations
        about the tab measure device 


        initial parameters:
        tab from the main window widget.
        create by Piero
    """
    def __init__(self, tab):
        super().__init__()
        self.tab = tab
    
    def construction(self):
        # this method call the class that will construct
        # the design for the second tab
        self.tab.addTab(MeasureDeviceConstructor(), "Measure Tab")


class MeasureDeviceConstructor(QtWidgets.QWidget):
    """ Class that will construct the design of the tab
        measure device

        create by Piero
    """
    def __init__(self):
        # Method that will construct the measure device tab
        # layout
        super().__init__()

        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

        self.label1 = QtWidgets.QLabel("Buttons and entry fields")
        self.label2 = QtWidgets.QLabel("canvas")

        self.grid.addWidget(self.label1, 0, 0)
        self.grid.addWidget(self.label2, 0, 1)