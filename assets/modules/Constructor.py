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
            input_field.setEchoMode(QLineEdit.EchoMode.Password)
        if comando:
            input_field.returnPressed.connect(comando)
        
        return label, input_field

    def sidebar(self, items, stack, logo, width=210, active_index=0):
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
        

        for item in items:
            icono = item.get('icono', '')
            texto = item.get('texto', '')
            index = item.get('index', 0)

            boton = QPushButton(f'{icono} {texto}'.strip())
            boton.setFixedHeight(48)
            boton.setCursor(Qt.CursorShape.PointingHandCursor)
            boton.setStyleSheet(estilo_activo if index == active_index else estilo_inactivo)
            boton.clicked.connect(lambda checked=False, idx=index, btn=boton: activar(idx, btn))

            botones.append(boton)
            button_layout.addWidget(boton)

        button_layout.addStretch()
        layout.addWidget(button_container)

        
        return frame
    
    def tabla(self, headers=None, datos=None, width=None, height=None, seleccionar=None):

        headers = headers or []
        datos   = datos   or []

        def formatear_valor(valor):
            if isinstance(valor, (list, tuple, set)):
                return "\n".join(str(elemento) for elemento in valor)
            return str(valor)
 
        tablas = QTableWidget(len(datos), len(headers))
        tablas.setHorizontalHeaderLabels(headers)
 
        tablas.setStyleSheet(f"""
            QTableWidget {{
                background-color: {NEGRO};
                color: {BLANCO};
                border: none;
                outline: none;
                font-size: 13px;
                alternate-background-color: rgba(255,255,255,0.04);
                gridline-color: rgba(255,255,255,0.08);
                padding: 45px;
                margin: 25px;
            }}
            QTableWidget::item {{
                padding: 6px 14px;
            }}
            QTableWidget::item:selected {{
                background-color: {COLOR_PRINCIPAL};
                color: {BLANCO};
            }}
            QHeaderView::section {{
                background-color: {COLOR_PRINCIPAL};
                color: {BLANCO};
                font-weight: bold;
                font-size: 13px;
                padding: 8px 14px;
                border: none;
                border-right: 1px solid rgba(255,255,255,0.12);
            }}
            QScrollBar:vertical {{
                background: {NEGRO};
                width: 6px;
                border-radius: 3px;
            }}
            QScrollBar::handle:vertical {{
                background: {COLOR_PRINCIPAL};
                border-radius: 3px;
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0px;
            }}
        """)
 
        tablas.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        tablas.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        tablas.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        tablas.setAlternatingRowColors(True)
        tablas.verticalHeader().setVisible(False)
        tablas.horizontalHeader().setStretchLastSection(True)
        tablas.setShowGrid(True)
        tablas.setWordWrap(True)
        tablas.setFocusPolicy(Qt.FocusPolicy.NoFocus)
 
        if width and height:
            tablas.setFixedSize(width, height)
 
        for r, fila in enumerate(datos):
            for c, valor in enumerate(fila):
                item = QTableWidgetItem(formatear_valor(valor))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                tablas.setItem(r, c, item)
 
        tablas.resizeColumnsToContents()
        tablas.resizeRowsToContents()
        tablas.horizontalHeader().setStretchLastSection(True)
 
        if seleccionar:
            def on_seleccion():
                fila = tablas.currentRow()
                if fila < 0:
                    return
                fila_dict = {
                    headers[c]: tablas.item(fila, c).text()
                    for c in range(len(headers))
                }
                seleccionar(fila_dict)
            tablas.itemSelectionChanged.connect(on_seleccion)
 
        return tablas
