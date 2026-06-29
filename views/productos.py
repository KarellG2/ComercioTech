import sys
from PyQt6.QtWidgets import QWidget,QVBoxLayout, QStackedWidget

from assets.modules import Constructor
from assets.modules.Constantes import *

construir = Constructor.Construir()

class Productos(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle('productos')
        self.setFixedSize(ANCHO_PANTALLA, ALTO_PANTALLA)
        self.setStyleSheet(f'background-color:{NEGRO}')
        
        self.mainWindow = main_window
        
        self.content_stack = QStackedWidget()
        
        content_layout = QVBoxLayout(self)
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(20)
        
        self.tabla = construir.tabla(
            headers=['Nombre', 'Precio'],
            datos=[['Producto 1', '$10.00'], ['Producto 2', '$20.00']]
        )
        content_layout.addWidget(self.tabla)
