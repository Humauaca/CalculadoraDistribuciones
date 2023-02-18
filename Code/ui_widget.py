# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetR.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(460, 401)
        self.verticalLayout_5 = QVBoxLayout(Widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_distribuciones = QTabWidget(Widget)
        self.widget_distribuciones.setObjectName(u"widget_distribuciones")
        self.widget_distribuciones.setMaximumSize(QSize(442, 121))
        self.tab_normal = QWidget()
        self.tab_normal.setObjectName(u"tab_normal")
        self.widget = QWidget(self.tab_normal)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 126, 56))
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.line_media = QLineEdit(self.widget)
        self.line_media.setObjectName(u"line_media")
        self.line_media.setMinimumSize(QSize(40, 0))
        self.line_media.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_7.addWidget(self.line_media)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.line_d_estandar = QLineEdit(self.widget)
        self.line_d_estandar.setObjectName(u"line_d_estandar")
        self.line_d_estandar.setMinimumSize(QSize(40, 0))
        self.line_d_estandar.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_8.addWidget(self.line_d_estandar)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.widget_distribuciones.addTab(self.tab_normal, "")
        self.tab_binomial = QWidget()
        self.tab_binomial.setObjectName(u"tab_binomial")
        self.widget1 = QWidget(self.tab_binomial)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 10, 119, 56))
        self.verticalLayout_9 = QVBoxLayout(self.widget1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_9.addWidget(self.label_4)

        self.line_pe_b = QLineEdit(self.widget1)
        self.line_pe_b.setObjectName(u"line_pe_b")
        self.line_pe_b.setMinimumSize(QSize(40, 0))
        self.line_pe_b.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_9.addWidget(self.line_pe_b)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_10.addWidget(self.label_5)

        self.line_n_intentos = QLineEdit(self.widget1)
        self.line_n_intentos.setObjectName(u"line_n_intentos")
        self.line_n_intentos.setMinimumSize(QSize(40, 0))
        self.line_n_intentos.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_10.addWidget(self.line_n_intentos)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.widget_distribuciones.addTab(self.tab_binomial, "")
        self.tab_geometrica = QWidget()
        self.tab_geometrica.setObjectName(u"tab_geometrica")
        self.widget2 = QWidget(self.tab_geometrica)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 10, 106, 24))
        self.horizontalLayout_11 = QHBoxLayout(self.widget2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_11.addWidget(self.label_6)

        self.line_pe_g = QLineEdit(self.widget2)
        self.line_pe_g.setObjectName(u"line_pe_g")
        self.line_pe_g.setMinimumSize(QSize(40, 0))
        self.line_pe_g.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_11.addWidget(self.line_pe_g)

        self.widget_distribuciones.addTab(self.tab_geometrica, "")
        self.tab_poisson = QWidget()
        self.tab_poisson.setObjectName(u"tab_poisson")
        self.widget3 = QWidget(self.tab_poisson)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(10, 10, 97, 24))
        self.horizontalLayout_12 = QHBoxLayout(self.widget3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_12.addWidget(self.label_7)

        self.line_lambda = QLineEdit(self.widget3)
        self.line_lambda.setObjectName(u"line_lambda")
        self.line_lambda.setMinimumSize(QSize(40, 0))
        self.line_lambda.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_12.addWidget(self.line_lambda)

        self.widget_distribuciones.addTab(self.tab_poisson, "")

        self.verticalLayout_5.addWidget(self.widget_distribuciones)

        self.frame_calculos = QFrame(Widget)
        self.frame_calculos.setObjectName(u"frame_calculos")
        self.frame_calculos.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_calculos.setFrameShape(QFrame.StyledPanel)
        self.frame_calculos.setFrameShadow(QFrame.Raised)
        self.elecciones_calculos = QGroupBox(self.frame_calculos)
        self.elecciones_calculos.setObjectName(u"elecciones_calculos")
        self.elecciones_calculos.setGeometry(QRect(0, 0, 191, 221))
        self.widget4 = QWidget(self.elecciones_calculos)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(20, 30, 158, 176))
        self.verticalLayout_6 = QVBoxLayout(self.widget4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.eleccion_igual = QRadioButton(self.widget4)
        self.eleccion_igual.setObjectName(u"eleccion_igual")

        self.horizontalLayout.addWidget(self.eleccion_igual)

        self.line_igual = QLineEdit(self.widget4)
        self.line_igual.setObjectName(u"line_igual")
        self.line_igual.setMinimumSize(QSize(40, 0))
        self.line_igual.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.line_igual)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.eleccion_menor = QRadioButton(self.widget4)
        self.eleccion_menor.setObjectName(u"eleccion_menor")

        self.horizontalLayout_2.addWidget(self.eleccion_menor)

        self.line_menor = QLineEdit(self.widget4)
        self.line_menor.setObjectName(u"line_menor")
        self.line_menor.setMinimumSize(QSize(40, 0))
        self.line_menor.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_2.addWidget(self.line_menor)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.eleccion_menor_igual = QRadioButton(self.widget4)
        self.eleccion_menor_igual.setObjectName(u"eleccion_menor_igual")

        self.horizontalLayout_3.addWidget(self.eleccion_menor_igual)

        self.line_menor_igual = QLineEdit(self.widget4)
        self.line_menor_igual.setObjectName(u"line_menor_igual")
        self.line_menor_igual.setMinimumSize(QSize(40, 0))
        self.line_menor_igual.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_3.addWidget(self.line_menor_igual)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.eleccion_mayor = QRadioButton(self.widget4)
        self.eleccion_mayor.setObjectName(u"eleccion_mayor")

        self.horizontalLayout_4.addWidget(self.eleccion_mayor)

        self.line_mayor = QLineEdit(self.widget4)
        self.line_mayor.setObjectName(u"line_mayor")
        self.line_mayor.setMinimumSize(QSize(40, 0))
        self.line_mayor.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_4.addWidget(self.line_mayor)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.eleccion_mayor_igual = QRadioButton(self.widget4)
        self.eleccion_mayor_igual.setObjectName(u"eleccion_mayor_igual")

        self.horizontalLayout_5.addWidget(self.eleccion_mayor_igual)

        self.line_mayor_igual = QLineEdit(self.widget4)
        self.line_mayor_igual.setObjectName(u"line_mayor_igual")
        self.line_mayor_igual.setMinimumSize(QSize(40, 0))
        self.line_mayor_igual.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_5.addWidget(self.line_mayor_igual)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.eleccion_entre = QRadioButton(self.widget4)
        self.eleccion_entre.setObjectName(u"eleccion_entre")

        self.horizontalLayout_6.addWidget(self.eleccion_entre)

        self.line_entre_1 = QLineEdit(self.widget4)
        self.line_entre_1.setObjectName(u"line_entre_1")
        self.line_entre_1.setMinimumSize(QSize(40, 0))
        self.line_entre_1.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_6.addWidget(self.line_entre_1)

        self.label = QLabel(self.widget4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.line_entre_2 = QLineEdit(self.widget4)
        self.line_entre_2.setObjectName(u"line_entre_2")
        self.line_entre_2.setMinimumSize(QSize(40, 0))
        self.line_entre_2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_6.addWidget(self.line_entre_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.widget5 = QWidget(self.frame_calculos)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setGeometry(QRect(207, 150, 201, 68))
        self.verticalLayout_8 = QVBoxLayout(self.widget5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.line_resultado = QLineEdit(self.widget5)
        self.line_resultado.setObjectName(u"line_resultado")
        self.line_resultado.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(12)
        self.line_resultado.setFont(font)

        self.verticalLayout_8.addWidget(self.line_resultado)

        self.button_calcular = QPushButton(self.widget5)
        self.button_calcular.setObjectName(u"button_calcular")
        self.button_calcular.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies([u"Ebrima"])
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.button_calcular.setFont(font1)
        self.button_calcular.setIconSize(QSize(16, 16))
        self.button_calcular.setAutoDefault(False)
        self.button_calcular.setFlat(False)

        self.verticalLayout_8.addWidget(self.button_calcular)


        self.verticalLayout_5.addWidget(self.frame_calculos)


        self.retranslateUi(Widget)

        self.widget_distribuciones.setCurrentIndex(0)
        self.button_calcular.setDefault(False)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Media :", None))
        self.line_media.setPlaceholderText(QCoreApplication.translate("Widget", u"0", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Des. Estandar :", None))
        self.line_d_estandar.setPlaceholderText(QCoreApplication.translate("Widget", u"0", None))
        self.widget_distribuciones.setTabText(self.widget_distribuciones.indexOf(self.tab_normal), QCoreApplication.translate("Widget", u"Normal", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"P de Exito :", None))
        self.line_pe_b.setPlaceholderText(QCoreApplication.translate("Widget", u"0", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"N \u00b0 Intentos :", None))
        self.line_n_intentos.setPlaceholderText(QCoreApplication.translate("Widget", u"0", None))
        self.widget_distribuciones.setTabText(self.widget_distribuciones.indexOf(self.tab_binomial), QCoreApplication.translate("Widget", u"Binomial", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"P de Exito :", None))
        self.line_pe_g.setPlaceholderText(QCoreApplication.translate("Widget", u"0", None))
        self.widget_distribuciones.setTabText(self.widget_distribuciones.indexOf(self.tab_geometrica), QCoreApplication.translate("Widget", u"Geometrica", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Lambda :", None))
        self.line_lambda.setPlaceholderText(QCoreApplication.translate("Widget", u"0", None))
        self.widget_distribuciones.setTabText(self.widget_distribuciones.indexOf(self.tab_poisson), QCoreApplication.translate("Widget", u"Poisson", None))
        self.elecciones_calculos.setTitle(QCoreApplication.translate("Widget", u"Calculos", None))
        self.eleccion_igual.setText(QCoreApplication.translate("Widget", u"Igual", None))
        self.line_igual.setPlaceholderText(QCoreApplication.translate("Widget", u"0", None))
        self.eleccion_menor.setText(QCoreApplication.translate("Widget", u"Menor", None))
        self.line_menor.setPlaceholderText(QCoreApplication.translate("Widget", u"0", None))
        self.eleccion_menor_igual.setText(QCoreApplication.translate("Widget", u"Menor o Igual ", None))
        self.line_menor_igual.setPlaceholderText(QCoreApplication.translate("Widget", u"0", None))
        self.eleccion_mayor.setText(QCoreApplication.translate("Widget", u"Mayor", None))
        self.line_mayor.setPlaceholderText(QCoreApplication.translate("Widget", u"0", None))
        self.eleccion_mayor_igual.setText(QCoreApplication.translate("Widget", u"Mayor o Igual", None))
        self.line_mayor_igual.setPlaceholderText(QCoreApplication.translate("Widget", u"0", None))
        self.eleccion_entre.setText(QCoreApplication.translate("Widget", u"Entre", None))
        self.line_entre_1.setPlaceholderText(QCoreApplication.translate("Widget", u"0", None))
        self.label.setText(QCoreApplication.translate("Widget", u"y", None))
        self.line_entre_2.setPlaceholderText(QCoreApplication.translate("Widget", u"0", None))
        self.line_resultado.setPlaceholderText(QCoreApplication.translate("Widget", u"0", None))
        self.button_calcular.setText(QCoreApplication.translate("Widget", u"Calcular", None))
    # retranslateUi

