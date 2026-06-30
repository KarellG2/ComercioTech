from PyQt6.QtWidgets import  QWidget, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt6.QtCore import Qt

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

        content_layout.addWidget(construir.header(texto="Iniciar Sesión", font_size=35), alignment=Qt.AlignmentFlag.AlignHCenter)

        centro_layout = QVBoxLayout()
        centro_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        centro_layout.setSpacing(12)

        layout_btn = QHBoxLayout()
        layout_btn.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        
        
        # Crear entrada para el usuario
        self.label_user, self.input_user  = construir.entrada(
            label_texto         = 'Usuario',
            placeholder         = 'Ingrese su Usuario',
            width               = 250,
            height              = 40
        )
        # Crear entrada para la contraseña
        self.label_pass, self.input_pass  = construir.entrada(
            label_texto         = 'Contraseña',
            placeholder         = 'Ingrese su Contraseña',
            width               = 250,
            height              = 40,
            password            = True
        )
        # Crear boton de inicio de sesion
        iniciar_sesion = construir.boton(
                            texto   = "Iniciar Sesion", 
                            color   = NEGRO,
                           comando = self.iniciar_sesion,
                            width   = 200, 
                            height  = 50)

        #usuario
        centro_layout.addWidget(self.label_user)
        centro_layout.addWidget(self.input_user)
        
        #contraseña
        centro_layout.addWidget(self.label_pass)
        centro_layout.addWidget(self.input_pass)
        
        centro_layout.addSpacing(40)
        
        # Boton de inicio de sesion
        layout_btn.addWidget(iniciar_sesion)
        layout_btn.addSpacing(40)
                
        content_layout.addLayout(centro_layout)
        content_layout.addLayout(layout_btn)
        layout.addStretch(1)
        layout.addLayout(content_layout)
        layout.addStretch(1)
        
    def iniciar_sesion(self):
            usuario = self.input_user.text().strip()
            password = self.input_pass.text().strip()
            
            if not usuario or not password:
                QMessageBox.warning(self, "Campos vacíos", "Por favor, complete todos los campos.")
                return
            self.input_pass.clear()
            self.main_window.mostrar_vista()  # Cambia al panel principal
