from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout

from assets.modules import Constructor
from assets.modules.Constantes import *


construir = Constructor.Construir()


class Clientes(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.mainWindow = main_window
        self.setStyleSheet(f"background-color:{NEGRO}")

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(12)

        self.mensaje = QLabel("")
        self.mensaje.setStyleSheet(f"color: {BLANCO}; font-size: 13px;")
        self.layout.addWidget(self.mensaje)

        self.tabla = None
        self._actualizar_tabla(
            ["ID", "Nombre", "RUT", "Telefono", "Correo", "Fecha creacion"],
            []
        )

    def cargar_datos(self, texto="", filtro="Todos"):
        clientes = self.mainWindow.bd.ver_clientes()
        filas = []

        for cliente in clientes:
            fila = [
                cliente.get("_id", ""),
                cliente.get("nombre", ""),
                cliente.get("rut", ""),
                cliente.get("telefono", ""),
                cliente.get("correo", ""),
                cliente.get("fecha_creacion", "")
            ]

            if self._coincide(fila, texto, filtro):
                filas.append(fila)

        self._actualizar_tabla(
            ["ID", "Nombre", "RUT", "Telefono", "Correo", "Fecha creacion"],
            filas
        )

    def _coincide(self, fila, texto, filtro):
        if not texto:
            return True

        texto = texto.lower()
        campos = {
            "Todos": fila,
            "Nombre": [fila[1]],
            "Correo": [fila[4]],
            "Numero": [fila[3]]
        }

        valores = campos.get(filtro, fila)
        return any(texto in str(valor).lower() for valor in valores)

    def _actualizar_tabla(self, headers, filas):
        if self.tabla:
            self.layout.removeWidget(self.tabla)
            self.tabla.deleteLater()

        if self.mainWindow.bd.error:
            self.mensaje.setText(self.mainWindow.bd.error)
        else:
            self.mensaje.setText(f"Clientes encontrados: {len(filas)}")

        self.tabla = construir.tabla(headers=headers, datos=filas)
        self.layout.addWidget(self.tabla)
