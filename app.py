import random
import sys

from PySide6 import QtCore, QtGui, QtWidgets
from pathlib import Path

from ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.input_fields = [self.ui.lineEdit_t0, self.ui.lineEdit_t1,
                             self.ui.lineEdit_v0, self.ui.lineEdit_x0,
                             self.ui.lineEdit_gamma, self.ui.lineEdit_omega0,
                             self.ui.lineEdit_m, self.ui.lineEdit_a0,
                             self.ui.lineEdit_dt1, self.ui.lineEdit_dt2]

        self.ui.pushButton_graph.clicked.connect(self.print_graph)
        self.ui.pushButton_reset.clicked.connect(self.reset)

    def print_graph(self, event=None):
        pass

    def reset(self, event=None):
        styleSheet = f'color: black'
        for line in self.input_fields:
            line.setText("")
            line.setStyleSheet(styleSheet)




if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    # window.resize(800, 600)
    window.show()

    window.setWindowTitle("Гармонический осциллятор v1.0")

    icon = QtGui.QIcon(QtGui.QPixmap(Path("src/logo.ico")))
    window.setWindowIcon(icon)

    sys.exit(app.exec())
