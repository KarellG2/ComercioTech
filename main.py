import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from qt_material import apply_stylesheet

from assets.modules import Constructor
from assets.modules.Constantes import *
from funciones import Funciones

comando     = Funciones.Comandos()
construir   = Constructor.Construir()
funciones   = Funciones.Comandos()

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
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout.addWidget(construir.header("Login"))

        # Contenedor central
        centro_layout = QVBoxLayout()
        centro_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout_btn = QHBoxLayout()
        layout_btn.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        
        
        # Crear entrada para el usuario
        label_user, input_user  = construir.entrada(
            label_texto         = 'Usuario',
            placeholder         = 'Ingrese su Usuario',
            width               = 250,
            height              = 40
        )
        # Crear entrada para la contraseña
        label_pass, input_pass  = construir.entrada(
            label_texto         = 'Contraseña',
            placeholder         = 'Ingrese su Contraseña',
            width               = 250,
            height              = 40
        )
        # Crear boton de inicio de sesion
        iniciar_sesion = construir.boton(
                            texto   = "Iniciar Sesion", 
                            color   = NEGRO,
                           comando = comando.mostrar_error,
                            width   = 200, 
                            height  = 50)

        #usuario
        centro_layout.addWidget(label_user)
        centro_layout.addWidget(input_user)
        #contraseña
        centro_layout.addWidget(label_pass)
        centro_layout.addWidget(input_pass)
        
        centro_layout.addSpacing(40)
        
        layout_btn.addWidget(iniciar_sesion)
        layout_btn.addSpacing(40)
        
        layout.addLayout(centro_layout)
        layout.addLayout(layout_btn)

class pantallaPrincipal(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

if __name__ =="__main__":

    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    ventana = ventanaPrincipal()
    ventana.show()
    sys.exit(app.exec())