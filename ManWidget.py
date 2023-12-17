from PyQt5.QtWidgets import QWidget,QApplication,QHBoxLayout
from UI.UI_MAN import Ui_ManWidget
from PyQt5 import QtWidgets
import sys


class ManWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.indexWidget = QWidget()
        Ui_ManWidget().setupUi(self.indexWidget)
        self.showArea = QtWidgets.QScrollArea(self)
        self.showArea.setWidgetResizable(True)
        self.showArea.setWidget(self.indexWidget)
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.showArea)
        self.setLayout(self.layout)

if __name__ == "__main__":
    mainApp = QApplication(sys.argv)
    mainWindow = ManWidget()
    mainWindow.showFullScreen()
    sys.exit(mainApp.exec_())