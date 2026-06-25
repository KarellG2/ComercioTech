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

class PantallaInicio(QWidget):

    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        content_layout = QVBoxLayout()
        content_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        content_layout.setSpacing(20)

        content_layout.addWidget(construir.header("Login"), alignment=Qt.AlignmentFlag.AlignHCenter)

        centro_layout = QVBoxLayout()
        centro_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        centro_layout.setSpacing(12)

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
        
        content_layout.addLayout(centro_layout)
        content_layout.addLayout(layout_btn)
        layout.addStretch(1)
        layout.addLayout(content_layout)
        layout.addStretch(1)
