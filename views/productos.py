from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout

from assets.modules import Constructor
from assets.modules.Constantes import *


construir = Constructor.Construir()


class Productos(QWidget):
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
            ["ID", "Nombre", "Descripcion", "Precio", "Categoria", "Stock"],
            []
        )

    def cargar_datos(self, texto="", filtro="Todos"):
        if texto and filtro == "Categoria":
            productos = self.mainWindow.bd.buscar_categoria(texto)
        else:
            productos = self.mainWindow.bd.ver_productos()

        filas = []

        for producto in productos:
            fila = [
                producto.get("_id", ""),
                producto.get("nombre", ""),
                self._formatear_descripcion(producto.get("descripcion", "")),
                producto.get("precio", ""),
                producto.get("categoria", ""),
                producto.get("stock", "")
            ]

            if self._coincide(fila, texto, filtro):
                filas.append(fila)

        self._actualizar_tabla(
            ["ID", "Nombre", "Descripcion", "Precio", "Categoria", "Stock"],
            filas
        )

    def _formatear_descripcion(self, descripcion):
        if isinstance(descripcion, list):
            partes = []
            for item in descripcion:
                if isinstance(item, dict):
                    partes.extend(f"{clave}: {valor}" for clave, valor in item.items())
                else:
                    partes.append(str(item))
            return " | ".join(partes)

        return descripcion

    def _coincide(self, fila, texto, filtro):
        if not texto:
            return True

        texto = texto.lower()
        campos = {
            "Todos": fila,
            "Nombre": [fila[1]],
            "Categoria": [fila[4]],
            "Precio": [fila[3]]
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
            self.mensaje.setText(f"Productos encontrados: {len(filas)}")

        self.tabla = construir.tabla(headers=headers, datos=filas)
        self.layout.addWidget(self.tabla)
