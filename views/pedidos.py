import json

from PyQt6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QTextEdit,
    QWidget,
    QVBoxLayout,
)

from assets.modules import Constructor
from assets.modules.Constantes import *


construir = Constructor.Construir()


class Pedidos(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.mainWindow = main_window
        self.registro_seleccionado = None
        self.documentos_por_id = {}
        self.setStyleSheet(f"background-color:{NEGRO}")

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(12)

        self.mensaje = QLabel("")
        self.mensaje.setStyleSheet(f"color: {BLANCO}; font-size: 13px;")
        self.layout.addWidget(self.mensaje)

        self._crear_botones_accion()

        self.tabla = None
        self._actualizar_tabla(
            ["ID", "ID cliente", "Cliente", "Fecha", "Productos", "Total", "Estado"],
            []
        )

    def _crear_botones_accion(self):
        acciones = QHBoxLayout()
        acciones.setSpacing(10)

        self.boton_agregar = construir.boton(
            texto="Agregar",
            comando=self.agregar_registro,
            color=COLOR_PRINCIPAL,
            fg=BLANCO,
            width=120,
            height=38
        )
        self.boton_editar = construir.boton(
            texto="Editar",
            comando=self.editar_registro,
            color=NEGRO,
            fg=BLANCO,
            width=120,
            height=38
        )
        self.boton_eliminar = construir.boton(
            texto="Eliminar",
            comando=self.eliminar_registro,
            color=ROJO,
            fg=BLANCO,
            width=120,
            height=38
        )

        acciones.addWidget(self.boton_agregar)
        acciones.addWidget(self.boton_editar)
        acciones.addWidget(self.boton_eliminar)
        acciones.addStretch()
        self.layout.addLayout(acciones)

    def cargar_datos(self, texto="", filtro="Todos"):
        if texto and filtro == "Estado":
            pedidos = self.mainWindow.bd.buscar_estado(texto)
        else:
            pedidos = self.mainWindow.bd.pedidos_clientes()

        filas = []
        self.documentos_por_id = {}

        for pedido in pedidos:
            id_pedido = str(pedido.get("_id", ""))
            self.documentos_por_id[id_pedido] = pedido
            cliente = self._nombre_cliente(pedido)
            fila = [
                id_pedido,
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

    def agregar_registro(self):
        datos = self._mostrar_dialogo_pedido("Agregar pedido")
        if not datos:
            return

        self.mainWindow.bd.agregar_pedido(datos)
        self._recargar_tabla()

    def editar_registro(self):
        id_pedido = self._obtener_id_seleccionado()
        if not id_pedido:
            return

        pedido = self.documentos_por_id.get(id_pedido, {})
        datos = self._mostrar_dialogo_pedido("Editar pedido", pedido)
        if not datos:
            return

        self.mainWindow.bd.actualizar_pedido(id_pedido, datos)
        self.registro_seleccionado = None
        self._recargar_tabla()

    def eliminar_registro(self):
        id_pedido = self._obtener_id_seleccionado()
        if not id_pedido:
            return

        respuesta = QMessageBox.question(
            self,
            "Eliminar pedido",
            "¿Seguro que quieres eliminar el pedido seleccionado?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if respuesta != QMessageBox.StandardButton.Yes:
            return

        self.mainWindow.bd.eliminar_pedido(id_pedido)
        self.registro_seleccionado = None
        self._recargar_tabla()

    def seleccionar_registro(self, fila):
        self.registro_seleccionado = fila

    def _obtener_id_seleccionado(self):
        if not self.registro_seleccionado:
            QMessageBox.warning(self, "Sin selección", "Selecciona un registro de la tabla primero.")
            return None

        return self.registro_seleccionado.get("ID")

    def _mostrar_dialogo_pedido(self, titulo, datos=None):
        datos = datos or {}

        dialogo = QDialog(self)
        dialogo.setWindowTitle(titulo)
        dialogo.setMinimumWidth(520)
        dialogo.setStyleSheet(f"""
            QDialog {{ background-color: {NEGRO}; }}
            QLabel {{ color: {BLANCO}; font-weight: bold; }}
            QLineEdit, QTextEdit {{
                background-color: transparent;
                color: {BLANCO};
                border: 2px solid {COLOR_PRINCIPAL};
                border-radius: 14px;
                padding: 6px 10px;
            }}
        """)

        layout = QFormLayout(dialogo)
        layout.setSpacing(12)

        input_cliente = QLineEdit(str(datos.get("id_cliente", "")))
        input_fecha = QLineEdit(str(datos.get("fecha_pedido", "")))
        input_productos = QTextEdit(self._productos_para_editar(datos.get("productos_pedidos", [])))
        input_productos.setFixedHeight(120)
        input_total = QLineEdit(str(datos.get("total_pedido", "")))
        input_estado = QLineEdit(str(datos.get("estado", "")))

        layout.addRow("ID cliente", input_cliente)
        layout.addRow("Fecha", input_fecha)
        layout.addRow("Productos JSON", input_productos)
        layout.addRow("Total", input_total)
        layout.addRow("Estado", input_estado)

        ayuda = QLabel('Ejemplo productos: [{"id_producto": "P001", "cantidad": 2, "precio": 5000}]')
        ayuda.setWordWrap(True)
        ayuda.setStyleSheet(f"color: {BLANCO}; font-size: 12px;")
        layout.addRow("", ayuda)

        botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        botones.accepted.connect(dialogo.accept)
        botones.rejected.connect(dialogo.reject)
        layout.addRow(botones)

        if dialogo.exec() != QDialog.DialogCode.Accepted:
            return None

        id_cliente = input_cliente.text().strip()
        if not id_cliente:
            QMessageBox.warning(self, "Campo obligatorio", "El ID del cliente no puede quedar vacío.")
            return None

        try:
            productos = self._leer_productos(input_productos.toPlainText().strip())
            total = self._convertir_numero(input_total.text().strip())
        except ValueError as error:
            QMessageBox.warning(self, "Dato inválido", str(error))
            return None

        return {
            "id_cliente": id_cliente,
            "fecha_pedido": input_fecha.text().strip(),
            "productos_pedidos": productos,
            "total_pedido": total,
            "estado": input_estado.text().strip()
        }

    def _convertir_numero(self, texto):
        if not texto:
            return 0

        if "." in texto:
            return float(texto)

        return int(texto)

    def _productos_para_editar(self, productos):
        if isinstance(productos, (list, dict)):
            return json.dumps(productos, ensure_ascii=False, indent=2)

        return str(productos)

    def _leer_productos(self, texto):
        if not texto:
            return []

        try:
            productos = json.loads(texto)
        except json.JSONDecodeError as error:
            raise ValueError(f"Productos debe ser JSON válido. Error: {error}")

        if not isinstance(productos, list):
            raise ValueError("Productos debe ser una lista JSON.")

        return productos

    def _recargar_tabla(self):
        if hasattr(self.mainWindow, "aplicar_busqueda"):
            self.mainWindow.aplicar_busqueda()
        else:
            self.cargar_datos()

    def _nombre_cliente(self, pedido):
        clientes = pedido.get("cliente", [])
        if clientes and isinstance(clientes, list):
            return clientes[0].get("nombre", "Sin cliente")
        return "Sin cliente"

    def _formatear_productos(self, productos):
        partes = []
        for producto in productos:
            if not isinstance(producto, dict):
                partes.append(str(producto))
                continue

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

        self.tabla = construir.tabla(
            headers=headers,
            datos=filas,
            seleccionar=self.seleccionar_registro
        )
        self.layout.addWidget(self.tabla)
