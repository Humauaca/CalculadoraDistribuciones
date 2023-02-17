from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
from distribuciones import Distribuciones

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.D = Distribuciones()
        self.setupUi(self)
        self.setWindowTitle("Calculadora de Distribuciones")
        self.button_calcular.clicked.connect(self.calcular)
        
        

    def validate_input(self, distribucion):
        if distribucion == "normal":
            try:
                media = float(self.line_media.text())
                destandar = float(self.line_d_estandar.text())
                return media, destandar
            except ValueError:
                self.line_resultado.setText("TypeError")
                return None, None
        elif distribucion == "binomial":
            try:
                n_intentos = int(self.line_n_intentos.text())
                pdeExitos = float(self.line_pe_b.text())
                return n_intentos, pdeExitos
            except ValueError:
                self.line_resultado.setText("TypeError")
                return None, None
        elif distribucion == "geometrica":
            try:
                p = float(self.line_pe_g.text())
                return p
            except ValueError:
                self.line_resultado.setText("TypeError")
                return None
        elif distribucion == "poisson":
            try:
                lam = float(self.line_lambda.text())
                return lam
            except ValueError:
                self.line_resultado .setText("TypeError")
                return None



    def calcular(self):
        # Distribucion Normal
        if self.widget_distribuciones.tabText(self.widget_distribuciones.currentIndex()) == "Normal":
            media, destandar = self.validate_input("normal")
            if media is not None and destandar is not None:
                if self.eleccion_igual.isChecked():
                    try:
                        x = float(self.line_igual.text())
                        self.line_resultado.setText(str(round(self.D.calcular_igual("normal", x, media, destandar), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_menor.isChecked():
                    try:
                        x = float(self.line_menor.text())
                        self.line_resultado.setText(str(round(self.D.calcular_menor("normal", x, media, destandar), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_menor_igual.isChecked():
                    try:
                        x = float(self.line_menor_igual.text())
                        self.line_resultado.setText(str(round(self.D.calcular_menor_igual("normal", x, media, destandar), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_mayor.isChecked():
                    try:
                        x = float(self.line_mayor.text())
                        self.line_resultado.setText(str(round(self.D.calcular_mayor("normal", x, media, destandar), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_mayor_igual.isChecked():
                    try:
                        x = float(self.line_mayor_igual.text())
                        self.line_resultado.setText(str(round(self.D.calcular_mayor_igual("normal", x, media, destandar), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_entre.isChecked():
                    try:
                        x1 = float(self.line_entre_1.text())
                        x2 = float(self.line_entre_2.text())
                        self.line_resultado.setText(str(round(self.D.calcular_entre( "normal", x1, x2, media, destandar), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
        # Distribucion Binomial    
        elif self.widget_distribuciones.tabText(self.widget_distribuciones.currentIndex()) == "Binomial":
            n, p = self.validate_input("binomial")
            if n is not None and p is not None:
                if self.eleccion_igual.isChecked():
                    try:
                        x = float(self.line_igual.text())
                        self.line_resultado.setText(str(round(self.D.calcular_igual("binomial", x, n, p), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_menor.isChecked():
                    try:
                        x = float(self.line_menor.text())
                        self.line_resultado.setText(str(round(self.D.calcular_menor("binomial", x, n, p), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_menor_igual.isChecked():
                    try:
                        x = float(self.line_menor_igual.text())
                        self.line_resultado.setText(str(round(self.D.calcular_menor_igual("binomial", x, n, p), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_mayor.isChecked():
                    try:
                        x = float(self.line_mayor.text())
                        self.line_resultado.setText(str(round(self.D.calcular_mayor("binomial", x, n, p), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_mayor_igual.isChecked():
                    try:
                        x = float(self.line_mayor_igual.text())
                        self.line_resultado.setText(str(round(self.D.calcular_mayor_igual("binomial", x, n, p), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_entre.isChecked():
                    try:
                        x1 = float(self.line_entre_1.text())
                        x2 = float(self.line_entre_2.text())
                        self.line_resultado.setText(str(round(self.D.calcular_entre( "binomial", x1, x2, n, p), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
        # Distribucion Geometrica
        elif self.widget_distribuciones.tabText(self.widget_distribuciones.currentIndex()) == "Geometrica":
            p = self.validate_input("geometrica")
            if p is not None:
                if self.eleccion_igual.isChecked():
                    try:
                        x = float(self.line_igual.text())
                        self.line_resultado.setText(str(round(self.D.calcular_igual("geometrica", x, p), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_menor.isChecked():
                    try:
                        x = float(self.line_menor.text())
                        self.line_resultado.setText(str(round(self.D.calcular_menor("geometrica", x, p), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_menor_igual.isChecked():
                    try:
                        x = float(self.line_menor_igual.text())
                        self.line_resultado.setText(str(round(self.D.calcular_menor_igual("geometrica", x, p), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_mayor.isChecked():
                    try:
                        x = float(self.line_mayor.text())
                        self.line_resultado.setText(str(round(self.D.calcular_mayor("geometrica", x, p), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_mayor_igual.isChecked():
                    try:
                        x = float(self.line_mayor_igual.text())
                        self.line_resultado.setText(str(round(self.D.calcular_mayor_igual("geometrica", x, p), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_entre.isChecked():
                    try:
                        x1 = float(self.line_entre_1.text())
                        x2 = float(self.line_entre_2.text())
                        self.line_resultado.setText(str(round(self.D.calcular_entre("geometrica", x, p), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
        # Distribucion Poisson
        elif self.widget_distribuciones.tabText(self.widget_distribuciones.currentIndex()) == "Poisson":
            lam = self.validate_input("poisson")
            if lam is not None:
                if self.eleccion_igual.isChecked():
                    try:
                        x = float(self.line_igual.text())
                        self.line_resultado.setText(str(round(self.D.calcular_igual("poisson", x, lam), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_menor.isChecked():
                    try:
                        x = float(self.line_menor.text())
                        self.line_resultado.setText(str(round(self.D.calcular_menor("poisson", x, lam), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_menor_igual.isChecked():
                    try:
                        x = float(self.line_menor_igual.text())
                        self.line_resultado.setText(str(round(self.D.calcular_menor_igual("poisson", x, lam), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_mayor.isChecked():
                    try:
                        x = float(self.line_mayor.text())
                        self.line_resultado.setText(str(round(self.D.calcular_mayor("poisson", x, lam), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_mayor_igual.isChecked():
                    try:
                        x = float(self.line_mayor_igual.text())
                        self.line_resultado.setText(str(round(self.D.calcular_mayor_igual("poisson", x, lam), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")
                elif self.eleccion_entre.isChecked():
                    try:
                        x1 = float(self.line_entre_1.text())
                        x2 = float(self.line_entre_2.text())
                        self.line_resultado.setText(str(round(self.D.calcular_entre("poisson", x, lam), 3)))
                    except ValueError:
                        self.line_resultado.setText("TypeError")

     


        