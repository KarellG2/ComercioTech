from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout

from assets.modules import Constructor
from assets.modules.Constantes import *


construir = Constructor.Construir()


class Pedidos(QWidget):
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
            ["ID", "ID cliente", "Cliente", "Fecha", "Productos", "Total", "Estado"],
            []
        )

    def cargar_datos(self, texto="", filtro="Todos"):
        if texto and filtro == "Estado":
            pedidos = self.mainWindow.bd.buscar_estado(texto)
        else:
            pedidos = self.mainWindow.bd.pedidos_clientes()

        filas = []

        for pedido in pedidos:
            cliente = self._nombre_cliente(pedido)
            fila = [
                pedido.get("_id", ""),
                pedido.get("id_cliente", ""),
                cliente,
                pedido.get("fecha_pedido", ""),
                self._formatear_productos(pedido.get("productos_pedidos", [])),
                pedido.get("total_pedido", ""),
                pedido.get("estado", "")
            ]

            if self._coincide(fila, texto, filtro):
                filas.append(fila)

        self._actualizar_tabla(
            ["ID", "ID cliente", "Cliente", "Fecha", "Productos", "Total", "Estado"],
            filas
        )

    def _nombre_cliente(self, pedido):
        clientes = pedido.get("cliente", [])
        if clientes and isinstance(clientes, list):
            return clientes[0].get("nombre", "Sin cliente")
        return "Sin cliente"

    def _formatear_productos(self, productos):
        partes = []
        for producto in productos:
            id_producto = producto.get("id_producto", "")
            cantidad = producto.get("cantidad", "")
            precio = producto.get("precio", "")
            partes.append(f"Producto {id_producto} x{cantidad} (${precio})")
        return " | ".join(partes)

    def _coincide(self, fila, texto, filtro):
        if not texto:
            return True

        texto = texto.lower()
        campos = {
            "Todos": fila,
            "Nombre": [fila[2]],
            "Estado": [fila[6]]
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
            self.mensaje.setText(f"Pedidos encontrados: {len(filas)}")

        self.tabla = construir.tabla(headers=headers, datos=filas)
        self.layout.addWidget(self.tabla)
