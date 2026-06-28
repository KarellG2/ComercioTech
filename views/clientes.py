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
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(20)
        
        tabla = construir.tabla(
            headers=['Nombre', 'Correo', 'numero'],
            datos=[['Cliente 1', 'cliente1@example.com', '123456789'], ['Cliente 2', 'cliente2@example.com', '987654321']]
        )
        content_layout.addWidget(tabla)
