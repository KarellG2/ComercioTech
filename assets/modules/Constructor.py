# Generador de Botones  
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from assets.modules.Constantes import *

class Construir:
    def header(self, texto, font_size=30):
        header = QFrame()
        header.setStyleSheet(f"background-color: {NEGRO}; border-color: {NEGRO};")
        header.setFixedHeight(195)

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
    
    def entrada(self, comando=None, color=None, fg=None, width=210, height=40, label_texto = 'campo', placeholder='', password=False):
        label=QLabel(label_texto)
        label.setStyleSheet(f'color: {BLANCO}; font-size:13px; font-weight:bold;')
        input_field = QLineEdit()
        input_field.setPlaceholderText(placeholder)
        input_field.setFixedSize(width, height)
        color_fondo = color if color else 'transparent'
        color_texto = fg if fg else BLANCO
        
        input_field.setStyleSheet(f"""
            QLineEdit {{
                background-color: {color_fondo};
                color: {color_texto};
                border: 2px solid {COLOR_PRINCIPAL};
                border-radius: {height // 2}px;
                padding: 0 12px;
                font-size: 13px;
            }}
            QLineEdit:focus {{
                border: 2px solid {HOVER_COLOR};
            }}
        """)

        if password:
            input_field.setEchoMode(QLineEdit.echoMode.Password)
        if comando:
            input_field.returnPressed.connect(comando)
        
        return label, input_field
