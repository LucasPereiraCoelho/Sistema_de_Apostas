import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from view.tela_principal import Ui_MainWindow



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
