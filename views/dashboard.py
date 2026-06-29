from PyQt6.QtWidgets import QWidget,QVBoxLayout, QStackedWidget

from assets.modules import Constructor
from assets.modules.Constantes import *

construir = Constructor.Construir()

class Dashboard(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle('dashboard')
        self.setFixedSize(ANCHO_PANTALLA, ALTO_PANTALLA)
        self.setStyleSheet(f'background-color:{NEGRO}')

        self.mainWindow = main_window  
        
        self.content_stack = QStackedWidget()
        
        content_layout = QVBoxLayout(self)
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(20)
        
        self.tabla = construir.tabla(
            headers=['Nombre', 'Correo', 'numero'],
            datos=[['Cliente 1', 'cliente1@example.com', '123456789'], ['Cliente 2', 'cliente2@example.com', '987654321']]
        )
        content_layout.addWidget(self.tabla)
