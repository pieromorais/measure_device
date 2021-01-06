# This file make the layout of the settings tab in the
# main layout

from PySide6 import QtCore, QtGui, QtWidgets

class SettingsTab(QtWidgets.QWidget):
    """ This class is responsible to receive the Tab
    parameters from the main.py file and construct the 
    layout in the tab settings

    parameters: tabWidget

    created by Piero
    """
    def __init__(self, tab):
        # Treatment fo the initial parameters
        super().__init__()

        self.tab = tab

    def construction(self):
        self.tab.addTab(SettingsTabConstructor(), "Settings")

class SettingsTabConstructor(QtWidgets.QWidget):
    """ This class is responsible to create the 
    layout in the settings tab 
    """

    def __init__(self):
        super().__init__()

        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

        self.label = QtWidgets.QLabel("Settings")

        self.grid.addWidget(self.label)
