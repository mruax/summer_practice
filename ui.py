# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design_v4.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 704)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_header = QVBoxLayout()
        self.verticalLayout_header.setObjectName(u"verticalLayout_header")
        self.verticalLayout_header.setSizeConstraint(QLayout.SetFixedSize)
        self.label_program_name = QLabel(self.centralwidget)
        self.label_program_name.setObjectName(u"label_program_name")
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(14)
        font.setBold(False)
        self.label_program_name.setFont(font)
        self.label_program_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_header.addWidget(self.label_program_name)


        self.gridLayout.addLayout(self.verticalLayout_header, 0, 0, 1, 2)

        self.verticalLayout_graph = QVBoxLayout()
        self.verticalLayout_graph.setObjectName(u"verticalLayout_graph")
        self.label_graph = QLabel(self.centralwidget)
        self.label_graph.setObjectName(u"label_graph")
        self.label_graph.setAlignment(Qt.AlignCenter)

        self.verticalLayout_graph.addWidget(self.label_graph)


        self.gridLayout.addLayout(self.verticalLayout_graph, 1, 1, 1, 1)

        self.horizontalLayout_buttons = QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName(u"horizontalLayout_buttons")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_buttons.addItem(self.horizontalSpacer_2)

        self.pushButton_print = QPushButton(self.centralwidget)
        self.pushButton_print.setObjectName(u"pushButton_print")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_print.sizePolicy().hasHeightForWidth())
        self.pushButton_print.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(12)
        self.pushButton_print.setFont(font1)

        self.horizontalLayout_buttons.addWidget(self.pushButton_print)

        self.pushButton_reset = QPushButton(self.centralwidget)
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_reset.sizePolicy().hasHeightForWidth())
        self.pushButton_reset.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.pushButton_reset.setFont(font2)

        self.horizontalLayout_buttons.addWidget(self.pushButton_reset)

        self.pushButton_graph = QPushButton(self.centralwidget)
        self.pushButton_graph.setObjectName(u"pushButton_graph")
        sizePolicy1.setHeightForWidth(self.pushButton_graph.sizePolicy().hasHeightForWidth())
        self.pushButton_graph.setSizePolicy(sizePolicy1)
        self.pushButton_graph.setFont(font2)

        self.horizontalLayout_buttons.addWidget(self.pushButton_graph)


        self.gridLayout.addLayout(self.horizontalLayout_buttons, 2, 1, 1, 1)

        self.verticalLayout_input_fields = QVBoxLayout()
        self.verticalLayout_input_fields.setSpacing(0)
        self.verticalLayout_input_fields.setObjectName(u"verticalLayout_input_fields")
        self.verticalLayout_t0 = QVBoxLayout()
        self.verticalLayout_t0.setSpacing(0)
        self.verticalLayout_t0.setObjectName(u"verticalLayout_t0")
        self.verticalLayout_t0.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_t0 = QLabel(self.centralwidget)
        self.label_t0.setObjectName(u"label_t0")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_t0.sizePolicy().hasHeightForWidth())
        self.label_t0.setSizePolicy(sizePolicy2)
        self.label_t0.setFont(font1)

        self.verticalLayout_t0.addWidget(self.label_t0)

        self.lineEdit_t0 = QLineEdit(self.centralwidget)
        self.lineEdit_t0.setObjectName(u"lineEdit_t0")

        self.verticalLayout_t0.addWidget(self.lineEdit_t0)


        self.verticalLayout_input_fields.addLayout(self.verticalLayout_t0)

        self.verticalLayout_t1 = QVBoxLayout()
        self.verticalLayout_t1.setSpacing(0)
        self.verticalLayout_t1.setObjectName(u"verticalLayout_t1")
        self.label_t1 = QLabel(self.centralwidget)
        self.label_t1.setObjectName(u"label_t1")
        sizePolicy2.setHeightForWidth(self.label_t1.sizePolicy().hasHeightForWidth())
        self.label_t1.setSizePolicy(sizePolicy2)
        self.label_t1.setFont(font1)

        self.verticalLayout_t1.addWidget(self.label_t1)

        self.lineEdit_t1 = QLineEdit(self.centralwidget)
        self.lineEdit_t1.setObjectName(u"lineEdit_t1")

        self.verticalLayout_t1.addWidget(self.lineEdit_t1)


        self.verticalLayout_input_fields.addLayout(self.verticalLayout_t1)

        self.verticalLayout_v0 = QVBoxLayout()
        self.verticalLayout_v0.setSpacing(0)
        self.verticalLayout_v0.setObjectName(u"verticalLayout_v0")
        self.label_v0 = QLabel(self.centralwidget)
        self.label_v0.setObjectName(u"label_v0")
        sizePolicy2.setHeightForWidth(self.label_v0.sizePolicy().hasHeightForWidth())
        self.label_v0.setSizePolicy(sizePolicy2)
        self.label_v0.setFont(font1)

        self.verticalLayout_v0.addWidget(self.label_v0)

        self.lineEdit_v0 = QLineEdit(self.centralwidget)
        self.lineEdit_v0.setObjectName(u"lineEdit_v0")

        self.verticalLayout_v0.addWidget(self.lineEdit_v0)


        self.verticalLayout_input_fields.addLayout(self.verticalLayout_v0)

        self.verticalLayout_x0 = QVBoxLayout()
        self.verticalLayout_x0.setSpacing(0)
        self.verticalLayout_x0.setObjectName(u"verticalLayout_x0")
        self.label_x0 = QLabel(self.centralwidget)
        self.label_x0.setObjectName(u"label_x0")
        sizePolicy2.setHeightForWidth(self.label_x0.sizePolicy().hasHeightForWidth())
        self.label_x0.setSizePolicy(sizePolicy2)
        self.label_x0.setFont(font1)

        self.verticalLayout_x0.addWidget(self.label_x0)

        self.label_x0_2 = QLabel(self.centralwidget)
        self.label_x0_2.setObjectName(u"label_x0_2")
        sizePolicy2.setHeightForWidth(self.label_x0_2.sizePolicy().hasHeightForWidth())
        self.label_x0_2.setSizePolicy(sizePolicy2)
        self.label_x0_2.setFont(font1)

        self.verticalLayout_x0.addWidget(self.label_x0_2)

        self.lineEdit_x0 = QLineEdit(self.centralwidget)
        self.lineEdit_x0.setObjectName(u"lineEdit_x0")

        self.verticalLayout_x0.addWidget(self.lineEdit_x0)


        self.verticalLayout_input_fields.addLayout(self.verticalLayout_x0)

        self.verticalLayout_gamma = QVBoxLayout()
        self.verticalLayout_gamma.setSpacing(0)
        self.verticalLayout_gamma.setObjectName(u"verticalLayout_gamma")
        self.label_gamma = QLabel(self.centralwidget)
        self.label_gamma.setObjectName(u"label_gamma")
        sizePolicy2.setHeightForWidth(self.label_gamma.sizePolicy().hasHeightForWidth())
        self.label_gamma.setSizePolicy(sizePolicy2)
        self.label_gamma.setFont(font1)

        self.verticalLayout_gamma.addWidget(self.label_gamma)

        self.lineEdit_gamma = QLineEdit(self.centralwidget)
        self.lineEdit_gamma.setObjectName(u"lineEdit_gamma")

        self.verticalLayout_gamma.addWidget(self.lineEdit_gamma)


        self.verticalLayout_input_fields.addLayout(self.verticalLayout_gamma)

        self.verticalLayout_omega0 = QVBoxLayout()
        self.verticalLayout_omega0.setSpacing(0)
        self.verticalLayout_omega0.setObjectName(u"verticalLayout_omega0")
        self.label_omega0 = QLabel(self.centralwidget)
        self.label_omega0.setObjectName(u"label_omega0")
        sizePolicy2.setHeightForWidth(self.label_omega0.sizePolicy().hasHeightForWidth())
        self.label_omega0.setSizePolicy(sizePolicy2)
        self.label_omega0.setFont(font1)

        self.verticalLayout_omega0.addWidget(self.label_omega0)

        self.label_omega0_2 = QLabel(self.centralwidget)
        self.label_omega0_2.setObjectName(u"label_omega0_2")
        sizePolicy2.setHeightForWidth(self.label_omega0_2.sizePolicy().hasHeightForWidth())
        self.label_omega0_2.setSizePolicy(sizePolicy2)
        self.label_omega0_2.setFont(font1)

        self.verticalLayout_omega0.addWidget(self.label_omega0_2)

        self.lineEdit_omega0 = QLineEdit(self.centralwidget)
        self.lineEdit_omega0.setObjectName(u"lineEdit_omega0")

        self.verticalLayout_omega0.addWidget(self.lineEdit_omega0)


        self.verticalLayout_input_fields.addLayout(self.verticalLayout_omega0)

        self.verticalLayout_m = QVBoxLayout()
        self.verticalLayout_m.setObjectName(u"verticalLayout_m")
        self.label_m = QLabel(self.centralwidget)
        self.label_m.setObjectName(u"label_m")
        sizePolicy2.setHeightForWidth(self.label_m.sizePolicy().hasHeightForWidth())
        self.label_m.setSizePolicy(sizePolicy2)
        self.label_m.setFont(font1)

        self.verticalLayout_m.addWidget(self.label_m)

        self.lineEdit_m = QLineEdit(self.centralwidget)
        self.lineEdit_m.setObjectName(u"lineEdit_m")

        self.verticalLayout_m.addWidget(self.lineEdit_m)


        self.verticalLayout_input_fields.addLayout(self.verticalLayout_m)

        self.verticalLayout_a0 = QVBoxLayout()
        self.verticalLayout_a0.setSpacing(0)
        self.verticalLayout_a0.setObjectName(u"verticalLayout_a0")
        self.label_a0 = QLabel(self.centralwidget)
        self.label_a0.setObjectName(u"label_a0")
        sizePolicy2.setHeightForWidth(self.label_a0.sizePolicy().hasHeightForWidth())
        self.label_a0.setSizePolicy(sizePolicy2)
        self.label_a0.setFont(font1)

        self.verticalLayout_a0.addWidget(self.label_a0)

        self.lineEdit_a0 = QLineEdit(self.centralwidget)
        self.lineEdit_a0.setObjectName(u"lineEdit_a0")

        self.verticalLayout_a0.addWidget(self.lineEdit_a0)


        self.verticalLayout_input_fields.addLayout(self.verticalLayout_a0)

        self.verticalLayout_OMEGA = QVBoxLayout()
        self.verticalLayout_OMEGA.setSpacing(0)
        self.verticalLayout_OMEGA.setObjectName(u"verticalLayout_OMEGA")
        self.label_OMEGA = QLabel(self.centralwidget)
        self.label_OMEGA.setObjectName(u"label_OMEGA")
        sizePolicy2.setHeightForWidth(self.label_OMEGA.sizePolicy().hasHeightForWidth())
        self.label_OMEGA.setSizePolicy(sizePolicy2)
        self.label_OMEGA.setFont(font1)

        self.verticalLayout_OMEGA.addWidget(self.label_OMEGA)

        self.label_OMEGA_2 = QLabel(self.centralwidget)
        self.label_OMEGA_2.setObjectName(u"label_OMEGA_2")
        sizePolicy2.setHeightForWidth(self.label_OMEGA_2.sizePolicy().hasHeightForWidth())
        self.label_OMEGA_2.setSizePolicy(sizePolicy2)
        self.label_OMEGA_2.setFont(font1)

        self.verticalLayout_OMEGA.addWidget(self.label_OMEGA_2)

        self.lineEdit_OMEGA = QLineEdit(self.centralwidget)
        self.lineEdit_OMEGA.setObjectName(u"lineEdit_OMEGA")

        self.verticalLayout_OMEGA.addWidget(self.lineEdit_OMEGA)


        self.verticalLayout_input_fields.addLayout(self.verticalLayout_OMEGA)

        self.verticalLayout_dt1 = QVBoxLayout()
        self.verticalLayout_dt1.setSpacing(0)
        self.verticalLayout_dt1.setObjectName(u"verticalLayout_dt1")
        self.label_dt1 = QLabel(self.centralwidget)
        self.label_dt1.setObjectName(u"label_dt1")
        sizePolicy2.setHeightForWidth(self.label_dt1.sizePolicy().hasHeightForWidth())
        self.label_dt1.setSizePolicy(sizePolicy2)
        self.label_dt1.setFont(font1)

        self.verticalLayout_dt1.addWidget(self.label_dt1)

        self.lineEdit_dt1 = QLineEdit(self.centralwidget)
        self.lineEdit_dt1.setObjectName(u"lineEdit_dt1")

        self.verticalLayout_dt1.addWidget(self.lineEdit_dt1)


        self.verticalLayout_input_fields.addLayout(self.verticalLayout_dt1)

        self.verticalLayout_dt2 = QVBoxLayout()
        self.verticalLayout_dt2.setSpacing(0)
        self.verticalLayout_dt2.setObjectName(u"verticalLayout_dt2")
        self.label_dt2 = QLabel(self.centralwidget)
        self.label_dt2.setObjectName(u"label_dt2")
        sizePolicy2.setHeightForWidth(self.label_dt2.sizePolicy().hasHeightForWidth())
        self.label_dt2.setSizePolicy(sizePolicy2)
        self.label_dt2.setFont(font1)

        self.verticalLayout_dt2.addWidget(self.label_dt2)

        self.lineEdit_dt2 = QLineEdit(self.centralwidget)
        self.lineEdit_dt2.setObjectName(u"lineEdit_dt2")

        self.verticalLayout_dt2.addWidget(self.lineEdit_dt2)


        self.verticalLayout_input_fields.addLayout(self.verticalLayout_dt2)


        self.gridLayout.addLayout(self.verticalLayout_input_fields, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_program_name.setText(QCoreApplication.translate("MainWindow", u"\u041c\u041e\u0414\u0415\u041b\u0418\u0420\u041e\u0412\u0410\u041d\u0418\u0415 \u0413\u0410\u0420\u041c\u041e\u041d\u0418\u0427\u0415\u0421\u041a\u041e\u0413\u041e \u041e\u0421\u0426\u0418\u041b\u041b\u042f\u0422\u041e\u0420\u0410", None))
        self.label_graph.setText("")
        self.pushButton_print.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0410\u0421\u041f\u0415\u0427\u0410\u0422\u0410\u0422\u042c \u0422\u0410\u0411\u041b\u0418\u0426\u0423", None))
        self.pushButton_reset.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0411\u0420\u041e\u0421", None))
        self.pushButton_graph.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041e\u0421\u0422\u0410\u0412\u0418\u0422\u042c \u0413\u0420\u0410\u0424\u0418\u041a", None))
        self.label_t0.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f t0:", None))
        self.label_t1.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0447\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f t1:", None))
        self.label_v0.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c v0:", None))
        self.label_x0.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.label_x0_2.setText(QCoreApplication.translate("MainWindow", u"\u0433\u0440\u0443\u0437\u0430 x0:", None))
        self.label_gamma.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0442\u0440\u0435\u043d\u0438\u044f \u03b3:", None))
        self.label_omega0.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430", None))
        self.label_omega0_2.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u043b\u0435\u0431\u0430\u043d\u0438\u0439 \u043e\u0441\u0446\u0438\u043b\u043b\u044f\u0442\u043e\u0440\u0430 \u03c90:", None))
        self.label_m.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0441\u0430 \u0433\u0440\u0443\u0437\u0430 m:", None))
        self.label_a0.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0441\u0442\u0430\u043d\u0442\u0430 A0:", None))
        self.label_OMEGA.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430", None))
        self.label_OMEGA_2.setText(QCoreApplication.translate("MainWindow", u"\u0432\u044b\u043d\u0443\u0436\u0434\u0430\u044e\u0449\u0435\u0439 \u0441\u0438\u043b\u044b \u03a9:", None))
        self.label_dt1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0440\u0430\u0441\u0447\u0435\u0442\u043e\u0432 dt1:", None))
        self.label_dt2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0434\u0438\u0441\u043a\u0440\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u0438 dt2:", None))
    # retranslateUi

