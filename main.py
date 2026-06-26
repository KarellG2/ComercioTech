import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from qt_material import apply_stylesheet

from assets.modules import Constructor
from assets.modules.Constantes import *
from funciones import Funciones

# Importar Vistas
from views.login import PantallaInicio
from views.dashboard import Dashboard


comando     = Funciones.Comandos()
construir   = Constructor.Construir()
funciones   = Funciones.Comandos()

class ventanaPrincipal(QMainWindow):    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("MercadoTech")
        self.setFixedSize(ANCHO_PANTALLA,ALTO_PANTALLA)
        self.setStyleSheet(f"background-color:{NEGRO}")
        
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        
        self.pantalla_inicio    = PantallaInicio(self)
        self.pantalla_dashboard = Dashboard(self)
        
        self.stack.addWidget(self.pantalla_inicio)
        self.stack.addWidget(self.pantalla_dashboard)
        

if __name__ =="__main__":

    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    ventana = ventanaPrincipal()
    ventana.show()
    sys.exit(app.exec())