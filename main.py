import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from qt_material import apply_stylesheet

from assets.modules import Constructor
from assets.modules.Constantes import *
from Funciones import Funciones

comando     = Funciones.Comandos()
construir   = Constructor.Construir()

class ventanaPrincipal(QMainWindow):    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("MercadoTech")
        self.setFixedSize(850,600)
        self.setStyleSheet(f"background-color:{NEGRO}")
        
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        
        self.pantalla_inicio = pantallaInicio(self)
        
        self.stack.addWidget(self.pantalla_inicio)
        
class pantallaInicio(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(construir.header("MercadoTech"))

        # Contenedor central
        centro_layout = QVBoxLayout()
        centro_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout_btn =    QVBoxLayout()
        layout_btn.setAlignment(Qt.AlignmentFlag.AlignBottom)

        titulo = QLabel("Venta de Articulos Tecnologicos")
        titulo.setStyleSheet(f"color: {BLANCO}; font-size: 26px; font-weight: bold;")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        boton = construir.boton(
                            texto   = "hola", 
                            color   = ROJO,
                            comando = comando.mostrar_error,
                            width   = 200, 
                            height  = 50)
        
        centro_layout.addWidget(titulo)
        centro_layout.addWidget(boton)
        centro_layout.addSpacing(40)
        
                
        
        layout.addLayout(centro_layout)
if __name__ =="__main__":

    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    ventana = ventanaPrincipal()
    ventana.show()
    sys.exit(app.exec())