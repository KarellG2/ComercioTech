# Generador de Botones  
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from assets.modules.Constantes import *

class Construir:
    def header(self, texto, font_size=30):
        header = QFrame()
        header.setStyleSheet(f"background-color: {COLOR_PRINCIPAL};")
        header.setFixedHeight(75)

        text_config = QVBoxLayout(header)
        label = QLabel(texto)
        
        label.setStyleSheet(
            f"color: {BLANCO}; font-weight: bold; font-size: {font_size}px;"
        )
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        text_config.addWidget(label)

        return header
    
    def boton(self, texto, comando=None, color =None, fg = None, width= 210, height=50):
        btn = QPushButton(texto)

        color_texto = fg if fg else (BLANCO if color in (ROJO, NEGRO, COLOR_PRINCIPAL) else NEGRO)
        btn.setStyleSheet(f"""
                          QPushButton{{
                              background-color:{color};
                              color:{color_texto};
                              font-family: Arial;
                              font-weight:bold;
                              font-size:15px;
                              border-radius:{height // 2}px;
                          }}
                          QPushButton:hover{{
                              background-color: {HOVER_COLOR};
                          }}""")
        btn.setFixedSize(width, height)
        if comando:
            btn.clicked.connect(comando)
        return btn
    
    # TODO: TABLAS | Mensajes de Error | 