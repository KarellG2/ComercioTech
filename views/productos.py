import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QVBoxLayout,QHBoxLayout, QStackedWidget, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from qt_material import apply_stylesheet

from assets.modules import Constructor
from assets.modules.Constantes import *
from funciones import Funciones

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
        
        tabla = construir.tabla(
            headers=['Nombre', 'Precio'],
            datos=[['Producto 1', '$10.00'], ['Producto 2', '$20.00']]
        )
        content_layout.addWidget(tabla)
