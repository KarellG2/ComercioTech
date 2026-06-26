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

    def sidebar(self, items, stack, logo, width=210):
        frame = QFrame()
        frame.setFixedWidth(width)
        frame.setStyleSheet(f'background-color: {NEGRO}; border: none;')
        
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        
        logo = QLabel(logo)
        logo.setFixedHeight(80)
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo.setStyleSheet(f'color: {BLANCO}; font-size:16px; font-weight:bold; background-color:{NEGRO}; border:none;')
        layout.addWidget(logo)
        
        button_container = QFrame()
        button_container.setStyleSheet('background-color: transparent')
        button_layout = QVBoxLayout(button_container)
        button_layout.setContentsMargins(12,16,12,16)
        button_layout.setSpacing(6)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        botones = []
        
        estilo_activo = f"""
            QPushButton {{
                background-color: {COLOR_PRINCIPAL};
                color: {BLANCO};
                text-align: left;
                padding-left: 16px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
                border: none;
            }}
        """
        estilo_inactivo = f"""
            QPushButton {{
                background-color: transparent;
                color: {BLANCO};
                text-align: left;
                padding-left: 16px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
                border: none;
            }}
            QPushButton:hover {{
                background-color: rgba(134, 65, 148, 80);
            }}
        """

        def activar(index, activo):
            stack.setCurrentIndex(index)
            for boton in botones:
                boton.setStyleSheet(estilo_inactivo)
            activo.setStyleSheet(estilo_activo)
        
        for i, item in enumerate(items):
            texto = f'{item.get('icono', '')} {item['texto']}'
            boton = QPushButton(texto)
            boton.setFixedHeight(48)
            boton.setStyleSheet(estilo_activo if i == 0 else estilo_inactivo)
            boton.clicked.connect(lambda checked, idx=item['index'], btn=boton: activar(idx,btn))
            botones.append(boton)
            
            button_layout.addWidget(boton)
            
        button_layout.addStretch()
        layout.addWidget(button_container)
        
        return frame