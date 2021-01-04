import sys
from PySide6 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.label1 = QtWidgets.QLabel("Tab 1")
        self.label2 = QtWidgets.QLabel("Tab 2")
        self.label3 = QtWidgets.QLabel("Tab 3")

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.tabWigdet = QtWidgets.QTabWidget()
        self.tabWigdet.addTab(self.label1, "APP Handbook")
        self.tabWigdet.addTab(self.label2, "Measures")
        self.tabWigdet.addTab(self.label3, "Settings")

        self.layout.addWidget(self.tabWigdet)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    screen = MainWindow()
    screen.resize(800, 600)
    screen.show()

    sys.exit(app.exec_())
