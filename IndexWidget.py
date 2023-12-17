from PyQt5.QtWidgets import QWidget
from UI.UI_IndexWidget import Ui_IndexWidget

class IndexWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_IndexWidget()
        self.ui.setupUi(self)
