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
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(20)
        
        # listado de productos
        pedidos = [
            {'nombre': 'Cliente 1', 'productos': ['Producto 1', 'Producto 2'], 'numero': '123456789'},
            {'nombre': 'Cliente 2', 'productos': ['Producto 3'], 'numero': '987654321'}
        ]
        
        self.tabla = construir.tabla(
            headers=['Nombre', 'Productos', 'numero'],
            datos=[['Cliente 1', pedidos[0]['productos'], '123456789'], 
                   ['Cliente 2', pedidos[1]['productos'], '987654321']]
        )
        content_layout.addWidget(self.tabla)
