import sys
from PySide6 import QtCore, QtGui, QtWidgets
from handbook import Handbook
from measument_device_app import MeasureDevice

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Measure device from LAMMI")

        self.label2 = QtWidgets.QLabel("Tab 2")
        self.label3 = QtWidgets.QLabel("Tab 3")

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.tabWigdet = QtWidgets.QTabWidget()

        # Constructing the Handbook tab
        # The set up of the file can be found in
        # handbook.py file
        handbook_constructor = Handbook(self.tabWigdet)
        handbook_constructor.construction()

        # Constructing the measure tab
        # The set up of the file can be found in
        # measument_device_app file
        measure_constructor = MeasureDevice(self.tabWigdet)
        measure_constructor.construction()

        # Other Stuff
        self.tabWigdet.addTab(self.label3, "Settings")

        self.layout.addWidget(self.tabWigdet)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    screen = MainWindow()
    screen.resize(800, 600)
    screen.show()

    sys.exit(app.exec_())
