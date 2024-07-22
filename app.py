import random
import sys

from PySide6 import QtCore, QtGui, QtWidgets
from pathlib import Path

from ui import Ui_MainWindow

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PySide6.QtGui import QPixmap, Qt
from io import BytesIO


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.input_fields = [self.ui.lineEdit_t0, self.ui.lineEdit_t1,
                             self.ui.lineEdit_v0, self.ui.lineEdit_x0,
                             self.ui.lineEdit_gamma, self.ui.lineEdit_omega0,
                             self.ui.lineEdit_m, self.ui.lineEdit_a0, self.ui.lineEdit_OMEGA,
                             self.ui.lineEdit_dt1, self.ui.lineEdit_dt2]

        for field in self.input_fields:
            field.textEdited.connect(lambda _, f=field: self.reset_style(f))

        self.ui.pushButton_graph.clicked.connect(self.print_graph)
        self.ui.pushButton_reset.clicked.connect(self.reset)

    def print_graph(self, event=None):
        if not self.check():
            # TODO: check if t_min >= t_max or t_max > t_min + dt

            self.reset_colour()

            buf = self.create_plot()
            pixmap = self.plot_to_label(buf, width=800, height=600)
            self.ui.label_graph.setPixmap(pixmap)

    def create_plot(self):
        # Параметры
        # omega0 = 1.0  # Собственная частота
        # gamma = 0.1  # Коэффициент демпфирования
        # A0 = 1.0  # Амплитуда внешней силы
        # Omega = 1.0  # Частота внешней силы
        # m = 1.0  # Масса
        # dt = 0.01  # Шаг времени
        # t_max = 10  # Общее время
        t0 = float(self.input_fields[0].text())      # Начальное время
        t1 = float(self.input_fields[1].text())      # Конечное время
        v0 = float(self.input_fields[2].text())      # Начальная скорость
        x0 = float(self.input_fields[3].text())      # Начальное положение груза
        gamma = float(self.input_fields[4].text())   # Коэффициент трения
        omega0 = float(self.input_fields[5].text())  # Собственная частота колебаний осциллятора
        m = float(self.input_fields[6].text())       # Масса груза
        A0 = float(self.input_fields[7].text())      # Константа гармонической вынуждающей силы
        OMEGA = float(self.input_fields[8].text())   # Собственная частота вынуждающей силы
        dt1 = float(self.input_fields[9].text())     # Период расчетов
        dt2 = float(self.input_fields[10].text())    # Параметр дискретизации

        t_max = t1 - t0
        M = dt1/dt2

        # Массив времени
        t = np.arange(t0, t1, dt2)

        # Инициализация массивов для скорости и положения
        v = np.zeros_like(t)
        x = np.zeros_like(t)

        # Начальные условия
        v[0] = v0
        x[0] = x0

        # Итеративное вычисление v и x
        for i in range(1, len(t)):
            v[i] = v[i - 1] + (-omega0 ** 2 * x[i - 1] - gamma * v[i - 1] + A0 * np.cos(OMEGA * t[i]) / m) * dt2
            x[i] = x[i - 1] + v[i] * dt2

        # Построение графика результатов
        sns.set(style="whitegrid")
        plt.figure(figsize=(14, 7))

        plt.plot(t, x, label='Положение $x(t)$')
        plt.plot(t, v, label='Скорость $v(t)$')

        plt.title('Затухающий гармонический осциллятор с внешней силой')
        plt.xlabel('Время $t$')
        plt.ylabel('Положение $x(t)$ и Скорость $v(t)$')
        plt.legend()

        # Сохранение графика в буфер
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        return buf

    def plot_to_label(self, buf, width=600, height=400):
        pixmap = QPixmap()
        pixmap.loadFromData(buf.getvalue())
        scaled_pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        return scaled_pixmap

    def check(self):
        flag = False
        styleSheet = "color: red"
        for line in self.input_fields:
            line_text = line.text()
            if line_text == "":
                line.setText("null")
                line.setStyleSheet(styleSheet)
                flag = True
            else:
                try:
                    if int(line_text) < 0:
                        line.setStyleSheet(styleSheet)
                        flag = True
                except ValueError:
                    line.setStyleSheet(styleSheet)
                    flag = True
        return not flag

    def reset(self, event=None):
        self.reset_text()
        self.reset_colour()
        self.ui.label_graph.setPixmap(QPixmap())

    def reset_text(self):
        for line in self.input_fields:
            line.setText("")

    def reset_colour(self):
        styleSheet = "color: black"
        for line in self.input_fields:
            line.setStyleSheet(styleSheet)

    def reset_style(self, line):
        styleSheet = "color: black"
        line.setStyleSheet(styleSheet)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.resize(1000, 600)
    window.show()

    window.setWindowTitle("Гармонический осциллятор v1.0")

    icon = QtGui.QIcon(QtGui.QPixmap(Path("src/logo.ico")))
    window.setWindowIcon(icon)

    sys.exit(app.exec())
