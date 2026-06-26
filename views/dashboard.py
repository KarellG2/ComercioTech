import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QVBoxLayout,QHBoxLayout, QStackedWidget, QLabel
from PyQt6.QtCore import Qt
from qt_material import apply_stylesheet

from assets.modules import Constructor
from assets.modules.Constantes import *
from funciones import Funciones

construir = Constructor.Construir()

class Dashboard(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle('dashboard')
        self.setFixedSize(ANCHO_PANTALLA, ALTO_PANTALLA)
        self.setStyleSheet(f'background-color:{NEGRO}')

        self.mainWindow = main_window  
        
        self.content_stack = QStackedWidget()
        sidebar_layout = QHBoxLayout(self)
        # Definir el sidebar
        sidebar = construir.sidebar(
            items=[
                {'texto': 'dashboard', 'icono':'a', 'index':0},
                {'texto':'productos','icono':'b','index':1}
            ],
            stack = self.content_stack,
            logo='comerciotech'
        )      
        sidebar_layout.addWidget(sidebar)
        sidebar_layout.addWidget(self.content_stack)