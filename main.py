import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QLabel, QLineEdit, QMessageBox, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from qt_material import apply_stylesheet

from assets.modules import Constructor
from assets.modules.Constantes import *
from funciones import Funciones

# Importar Vistas
from views.login import PantallaInicio
from views.dashboard import Dashboard


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

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        
        self.pantalla_inicio    = PantallaInicio(self)
        self.pantalla_dashboard = Dashboard(self)
        
        # Vistas
        self.stack.addWidget(self.pantalla_dashboard)
        self.stack.addWidget(self.pantalla_inicio)
        
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



if __name__ =="__main__":

    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    ventana = ventanaPrincipal()
    ventana.show()
    sys.exit(app.exec())