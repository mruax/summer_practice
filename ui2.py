# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win2_design.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form2(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(623, 363)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 629, 375))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(14)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
        self.label.setText(QCoreApplication.translate("Form", u"t_0,t_k \u2013 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u044b\u0439 \u0438 \u043a\u043e\u043d\u0435\u0447\u043d\u044b\u0439 \u043c\u043e\u043c\u0435\u043d\u0442 \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0440\u0430\u0441\u0447\u0435\u0442\u043e\u0432;\n"
"v_0 \u2013 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c;\n"
"x_0 \u2013 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0433\u0440\u0443\u0437\u0430;\n"
"\u03b3 \u2013 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0442\u0440\u0435\u043d\u0438\u044f;\n"
"\u03c9_0 \u2013 \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430 \u043a\u043e\u043b\u0435\u0431\u0430\u043d\u0438\u0439 \u043e\u0441\u0446\u0438\u043b\u043b\u044f\u0442\u043e\u0440\u0430;\n"
"dt_1 \u2013 \u043f\u0435\u0440\u0438\u043e\u0434 \u0440\u0430\u0441\u0447\u0435\u0442\u043e\u0432 (\u0442. \u0435"
                        ". \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u0432\u0440\u0435\u043c\u0435\u043d\u0438,\n"
"\u0447\u0435\u0440\u0435\u0437 \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0432\u044b\u0434\u0430\u0435\u0442\u0441\u044f \u0442\u0435\u043a\u0443\u0449\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445);\n"
"dt_2 (\u2206t) \u2013 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0434\u0438\u0441\u043a\u0440\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u0438;\n"
"\u0413\u0430\u0440\u043c\u043e\u043d\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0432\u044b\u043d\u0443\u0436\u0434\u0430\u044e\u0449\u0430\u044f \u0441\u0438\u043b\u0430, \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u043d\u0430\u044f \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u0435\u043c\n"
"F(t)= A_0 \u2219 cos(\u03a9t), \n"
"\u0433\u0434\u0435 \u03a9 \u2013 \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442"
                        "\u0430 \u0432\u044b\u043d\u0443\u0436\u0434\u0430\u044e\u0449\u0435\u0439 \u0441\u0438\u043b\u044b; A0 \u2013 \u043a\u043e\u043d\u0441\u0442\u0430\u043d\u0442\u0430;\n"
"m \u2013 \u043c\u0430\u0441\u0441\u0430 \u0433\u0440\u0443\u0437\u0430.\n"
"", None))
    # retranslateUi

