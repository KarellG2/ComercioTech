import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QVBoxLayout,QHBoxLayout, QStackedWidget, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from qt_material import apply_stylesheet

from assets.modules import Constructor
from assets.modules.Constantes import *
from funciones import Funciones

construir = Constructor.Construir()

class Pedidos(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle('Pedidos')
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
                {'texto':'productos','icono':'b','index':1},
                {'texto':'pedidos','icono':'c','index':2}
            ],
            stack = self.content_stack,
            logo='Comercio Tech'
        )      
        sidebar_layout.addWidget(sidebar)
        sidebar_layout.addWidget(self.content_stack)
        
        central_layout = QVBoxLayout()
        central_layout.addLayout(sidebar_layout)
        self.setLayout(central_layout)
        
        # listado de productos
        pedidos = [
            {'nombre': 'Cliente 1', 'productos': ['Producto 1', 'Producto 2'], 'numero': '123456789'},
            {'nombre': 'Cliente 2', 'productos': ['Producto 3'], 'numero': '987654321'}
        ]
        
        tabla = construir.tabla(
            headers=['Nombre', 'Productos', 'numero'],
            datos=[['Cliente 1', pedidos[0]['productos'], '123456789'], 
                   ['Cliente 2', pedidos[1]['productos'], '987654321']]
        )
        central_layout.addWidget(tabla)
        
        content_layout.addLayout(central_layout)
        content_layout.addLayout(sidebar_layout)