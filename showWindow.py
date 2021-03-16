from main_window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)


