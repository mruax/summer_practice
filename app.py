import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from PySide6 import QtGui, QtWidgets
from PySide6.QtGui import QPixmap, Qt

from ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.x = []
        self.v = []
        self.t = []

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
        self.ui.pushButton_print.clicked.connect(self.excel_graph)

    def print_graph(self, event=None):
        if self.check():
            self.reset_colour()

            self.create_plot()
            pixmap = self.plot_to_label(width=800, height=600)
            self.ui.label_graph.setPixmap(pixmap)

    def create_plot(self):
        # Параметры
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
        M = dt1 / dt2

        # Массив времени
        t = np.arange(t0, t1 + dt2, dt2)
        if t[-1] > t1:  # Если с заданным шагом превышает конечное значение времени
            t[-1] = t1

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

        self.x = x
        self.v = v
        self.t = t

        # Построение графика результатов
        sns.set(style="whitegrid")
        plt.figure(figsize=(14, 7))

        plt.plot(t, x, label='Положение $x(t)$')
        plt.plot(t, v, label='Скорость $v(t)$')

        plt.title('Затухающий гармонический осциллятор с внешней силой')
        plt.xlabel('Время $t$')
        plt.ylabel('Положение $x(t)$ и Скорость $v(t)$')
        plt.legend()

        # Сохранение графика в файл
        plt.savefig(Path("src/graph.png"), format='png', bbox_inches='tight')
        plt.close()  # Закрытие графика после сохранения

    def excel_graph(self):
        data = {'t': self.t, 'x': self.x, 'v': self.v}
        df = pd.DataFrame(data)
        excel_filename = Path('src/data.xlsx')
        df.to_excel(excel_filename, index=False)
        os.startfile(excel_filename)

    def plot_to_label(self, width=600, height=400):
        pixmap = QPixmap(Path("src/graph.png"))
        scaled_pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        return scaled_pixmap

    def check(self):
        flag = False
        styleSheet = "color: red"
        temp = []
        for line in self.input_fields:
            line_text = line.text()
            temp.append(line.text())
            if line_text == "":
                line.setText("null")
                line.setStyleSheet(styleSheet)
                flag = True
            else:
                try:  # Только числа
                    _ = float(line_text)
                except ValueError:
                    line.setStyleSheet(styleSheet)
                    flag = True

        # Проверка корректности значений
        try:  # Верный промежуток времени
            if float(temp[0]) >= float(temp[1]) or float(temp[0]) + float(temp[10]) >= float(temp[1]):
                flag = True
                self.input_fields[0].setStyleSheet(styleSheet)
                self.input_fields[1].setStyleSheet(styleSheet)
        except ValueError:
            flag = True
            self.input_fields[0].setStyleSheet(styleSheet)
            self.input_fields[1].setStyleSheet(styleSheet)
        try:  # Корректный период расчета и параметр дискретизации
            if float(temp[9]) <= 0 or float(temp[10]) <= 0:
                flag = True
                self.input_fields[9].setStyleSheet(styleSheet)
                self.input_fields[10].setStyleSheet(styleSheet)
        except ValueError:
            flag = True
            self.input_fields[9].setStyleSheet(styleSheet)
            self.input_fields[10].setStyleSheet(styleSheet)
        try:  # Корректный коэффициент трения
            if float(temp[4]) < 0:
                flag = True
                self.input_fields[4].setStyleSheet(styleSheet)
        except ValueError:
            flag = True
            self.input_fields[4].setStyleSheet(styleSheet)
        try:  # Корректная собственная частота колебаний осциллятора
            if float(temp[5]) < 0:
                flag = True
                self.input_fields[5].setStyleSheet(styleSheet)
        except ValueError:
            flag = True
            self.input_fields[5].setStyleSheet(styleSheet)
        try:  # Корректная масса груза
            if float(temp[6]) <= 0:
                flag = True
                self.input_fields[6].setStyleSheet(styleSheet)
        except ValueError:
            flag = True
            self.input_fields[6].setStyleSheet(styleSheet)
        try:  # Корректная собственная частота вынуждающей силы
            if float(temp[8]) <= 0:
                flag = True
                self.input_fields[8].setStyleSheet(styleSheet)
        except ValueError:
            flag = True
            self.input_fields[8].setStyleSheet(styleSheet)

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
