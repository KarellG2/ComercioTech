import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QVBoxLayout, QStackedWidget, QLabel
from PyQt6.QtCore import Qt
from qt_material import apply_stylesheet

from assets.modules import Constructor
from assets.modules.Constantes import *
from funciones import Funciones

construir = Constructor.Construir()

class dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('dashboard')
        self.setFixedSize(ANCHO_PANTALLA, ALTO_PANTALLA)
        self.setStyleSheet(f'background-color:{NEGRO}')
        