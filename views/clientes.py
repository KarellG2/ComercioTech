import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QVBoxLayout,QHBoxLayout, QStackedWidget, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from qt_material import apply_stylesheet

from assets.modules import Constructor
from assets.modules.Constantes import *
from funciones import Funciones

construir = Constructor.Construir()

class Clientes(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle('Clientes')
        self.setFixedSize(ANCHO_PANTALLA, ALTO_PANTALLA)
        self.setStyleSheet(f'background-color:{NEGRO}')

        self.mainWindow = main_window  
        
        self.content_stack = QStackedWidget()
        
        content_layout = QVBoxLayout(self)
        content_layout.setContentsMargins(0,0,0,0)
        content_layout.setSpacing(20)

        sidebar_layout = QHBoxLayout(self)
        # Definir el sidebar
        sidebar = construir.sidebar(
            items=[
                {'texto': 'dashboard', 'icono':'a', 'index':0},
                {'texto':'productos','icono':'b','index':1}
            ],
            stack = self.content_stack,
            logo='Comercio Tech'
        )      
        sidebar_layout.addWidget(sidebar)
        sidebar_layout.addWidget(self.content_stack)
        
        central_layout = QVBoxLayout()
        central_layout.addLayout(sidebar_layout)
        self.setLayout(central_layout)
        
        tabla = construir.tabla(
            headers=['Nombre', 'Correo', 'numero'],
            datos=[['Cliente 1', 'cliente1@example.com', '123456789'], ['Cliente 2', 'cliente2@example.com', '987654321']]
        )
        central_layout.addWidget(tabla)
        
        content_layout.addLayout(central_layout)
        content_layout.addLayout(sidebar_layout)