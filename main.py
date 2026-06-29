import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QStackedWidget, QPushButton, QVBoxLayout, QFrame, QLabel, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from qt_material import apply_stylesheet

from assets.modules import Constructor
from assets.modules.Constantes import *
from funciones import Funciones

# Importar Vistas
from views.login import PantallaInicio
from views.dashboard import Dashboard
from views.pedidos import Pedidos
from views.productos import Productos
from views.clientes import Clientes


comando     = Funciones.Comandos()
construir   = Constructor.Construir()
funciones   = Funciones.Comandos()

class ventanaPrincipal(QMainWindow):    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("ComercioTech")
        self.setFixedSize(ANCHO_PANTALLA,ALTO_PANTALLA)
        self.setStyleSheet(f"background-color:{NEGRO}")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowIcon(QIcon("assets/images/icon.ico")) 

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        
        self.pantalla_inicio    = PantallaInicio(self)
        # Vistas
        
        self.stack.addWidget(self.pantalla_inicio)
        self.stack.addWidget(self.panel())
        self.stack.setCurrentIndex(0)

        # Widgets persistentes
        self.boton_cerrar = QPushButton("X", self) 
        self.boton_cerrar.setFixedSize(40, 40)
        self.boton_cerrar.setStyleSheet(
            "font-weight: bold; font-size: 10px;"
        )
        self.boton_cerrar.clicked.connect(self.close)
        self.boton_cerrar.move(ANCHO_PANTALLA - self.boton_cerrar.width() - 10, 10)
        self.boton_cerrar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.boton_cerrar.raise_()
        
        self.arrastrable = False
        self.alturaArrastrable = 45
        
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            posicion_local = event.position().toPoint()
            
            if posicion_local.y() <= self.alturaArrastrable:
                self.arrastrable = True
                self.posicion_inicial = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
                event.accept()
                
    def mouseMoveEvent(self, event):#mover
        if self.arrastrable and event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.posicion_inicial)
            event.accept()

    def mouseReleaseEvent(self, event):#reset click
        self.arrastrable = False

    def panel(self):
        panel = QWidget()
        panel.setStyleSheet(f'background-color: {NEGRO};')
        
        layout = QHBoxLayout(panel)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        
        self.content_stack = QStackedWidget()
        
        self.vistaDashboard = Dashboard(self)
        self.vistaProductos = Productos(self)
        self.vistaClientes = Clientes(self)
        self.vistaPedidos = Pedidos(self)
        
        self.content_stack.addWidget(self.vistaDashboard)
        self.content_stack.addWidget(self.vistaProductos)
        self.content_stack.addWidget(self.vistaClientes)
        self.content_stack.addWidget(self.vistaPedidos)
        
        self.label_busqueda, self.input_busqueda = construir.entrada(
            label_texto         = '',
            placeholder         = 'Ingrese su búsqueda',
            width               = 250,
            height              = 40
        )

        self.combo_filtro = QComboBox()
        self.combo_filtro.addItems([
            'Todos',
            'Nombre',
            'Correo',
            'Numero',
            'Categoria',
            'Precio',
            'Estado'
        ])
        self.combo_filtro.setFixedSize(180, 40)
        self.combo_filtro.setStyleSheet(f'''
            QComboBox {{
                background-color: transparent;
                color: {BLANCO};
                border: 2px solid {COLOR_PRINCIPAL};
                border-radius: 20px;
                padding: 0 12px;
                font-size: 13px;
            }}
            QComboBox::drop-down {{
                border: none;
                width: 28px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {NEGRO};
                color: {BLANCO};
                selection-background-color: {COLOR_PRINCIPAL};
                border: 1px solid {COLOR_PRINCIPAL};
            }}
        ''')

        self.boton_limpiar_filtro = construir.boton(
            texto='Limpiar',
            comando=None,
            color=NEGRO,
            fg=BLANCO,
            width=120,
            height=40
        )

        buscador = QFrame()
        buscador.setStyleSheet(f'''
            QFrame {{
                background-color: {NEGRO};
                border: {NEGRO};
            }}
        ''')

        buscador_layout = QVBoxLayout(buscador)
        buscador_layout.setContentsMargins(18, 16, 18, 16)
        buscador_layout.setSpacing(12)

        titulo_busqueda = QLabel('Busqueda')
        titulo_busqueda.setStyleSheet(f'color: {BLANCO}; font-size: 16px; font-weight: bold;')

        fila_busqueda = QHBoxLayout()
        fila_busqueda.setSpacing(12)
        fila_busqueda.addWidget(self.label_busqueda)
        fila_busqueda.addWidget(self.input_busqueda)
        fila_busqueda.addWidget(self.combo_filtro)
        fila_busqueda.addWidget(self.boton_limpiar_filtro)
        fila_busqueda.addStretch()

        buscador_layout.addWidget(titulo_busqueda)
        buscador_layout.addLayout(fila_busqueda)

        contenedor_contenido = QWidget()
        contenido_layout = QVBoxLayout(contenedor_contenido)
        contenido_layout.setContentsMargins(20, 20, 20, 20)
        contenido_layout.setSpacing(16)
        contenido_layout.addWidget(buscador)
        contenido_layout.addWidget(self.content_stack)
        
        #sidebar
        sidebar = construir.sidebar(
            items=[
                {'texto': 'Dashboard', 'index': 0},
                {'texto': 'Productos', 'index': 1},
                {'texto': 'Clientes', 'index': 2},
                {'texto': 'Pedidos', 'index': 3}
            ],
            stack = self.content_stack,
            logo= 'ComercioTech',
            active_index=0
        )
        
        layout.addWidget(sidebar) 
        layout.addWidget(contenedor_contenido) 
        return panel
    
    def mostrar_vista(self):
        self.stack.setCurrentIndex(1)
        self.content_stack.setCurrentIndex(0)

if __name__ =="__main__":

    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    ventana = ventanaPrincipal()
    ventana.show()
    sys.exit(app.exec())