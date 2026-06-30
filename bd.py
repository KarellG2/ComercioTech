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


class Productos(QWidget):
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
            ["ID", "Nombre", "Descripcion", "Precio", "Categoria", "Stock"],
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
        if texto and filtro == "Categoria":
            productos = self.mainWindow.bd.buscar_categoria(texto)
        else:
            productos = self.mainWindow.bd.ver_productos()

        filas = []
        self.documentos_por_id = {}

        for producto in productos:
            id_producto = str(producto.get("_id", ""))
            self.documentos_por_id[id_producto] = producto
            fila = [
                id_producto,
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

    def agregar_registro(self):
        datos = self._mostrar_dialogo_producto("Agregar producto")
        if not datos:
            return

        self.mainWindow.bd.agregar_producto(datos)
        self._recargar_tabla()

    def editar_registro(self):
        id_producto = self._obtener_id_seleccionado()
        if not id_producto:
            return

        producto = self.documentos_por_id.get(id_producto, {})
        datos = self._mostrar_dialogo_producto("Editar producto", producto)
        if not datos:
            return

        self.mainWindow.bd.actualizar_producto(id_producto, datos)
        self.registro_seleccionado = None
        self._recargar_tabla()

    def eliminar_registro(self):
        id_producto = self._obtener_id_seleccionado()
        if not id_producto:
            return

        respuesta = QMessageBox.question(
            self,
            "Eliminar producto",
            "¿Seguro que quieres eliminar el producto seleccionado?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if respuesta != QMessageBox.StandardButton.Yes:
            return

        self.mainWindow.bd.eliminar_producto(id_producto)
        self.registro_seleccionado = None
        self._recargar_tabla()

    def seleccionar_registro(self, fila):
        self.registro_seleccionado = fila

    def _obtener_id_seleccionado(self):
        if not self.registro_seleccionado:
            QMessageBox.warning(self, "Sin selección", "Selecciona un registro de la tabla primero.")
            return None

        return self.registro_seleccionado.get("ID")

    def _mostrar_dialogo_producto(self, titulo, datos=None):
        datos = datos or {}

        dialogo = QDialog(self)
        dialogo.setWindowTitle(titulo)
        dialogo.setMinimumWidth(460)
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

        input_nombre = QLineEdit(str(datos.get("nombre", "")))
        input_descripcion = QTextEdit(self._descripcion_para_editar(datos.get("descripcion", "")))
        input_descripcion.setFixedHeight(90)
        input_precio = QLineEdit(str(datos.get("precio", "")))
        input_categoria = QLineEdit(str(datos.get("categoria", "")))
        input_stock = QLineEdit(str(datos.get("stock", "")))

        layout.addRow("Nombre", input_nombre)
        layout.addRow("Descripción", input_descripcion)
        layout.addRow("Precio", input_precio)
        layout.addRow("Categoría", input_categoria)
        layout.addRow("Stock", input_stock)

        botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        botones.accepted.connect(dialogo.accept)
        botones.rejected.connect(dialogo.reject)
        layout.addRow(botones)

        if dialogo.exec() != QDialog.DialogCode.Accepted:
            return None

        nombre = input_nombre.text().strip()
        if not nombre:
            QMessageBox.warning(self, "Campo obligatorio", "El nombre del producto no puede quedar vacío.")
            return None

        try:
            precio = self._convertir_numero(input_precio.text().strip())
            stock = int(input_stock.text().strip() or 0)
        except ValueError:
            QMessageBox.warning(self, "Dato inválido", "Precio y stock deben ser números válidos.")
            return None

        return {
            "nombre": nombre,
            "descripcion": self._leer_descripcion(input_descripcion.toPlainText().strip()),
            "precio": precio,
            "categoria": input_categoria.text().strip(),
            "stock": stock
        }

    def _convertir_numero(self, texto):
        if not texto:
            return 0

        if "." in texto:
            return float(texto)

        return int(texto)

    def _descripcion_para_editar(self, descripcion):
        if isinstance(descripcion, (list, dict)):
            return json.dumps(descripcion, ensure_ascii=False, indent=2)

        return str(descripcion)

    def _leer_descripcion(self, texto):
        if texto.startswith("[") or texto.startswith("{"):
            try:
                return json.loads(texto)
            except json.JSONDecodeError:
                return texto

        return texto

    def _recargar_tabla(self):
        if hasattr(self.mainWindow, "aplicar_busqueda"):
            self.mainWindow.aplicar_busqueda()
        else:
            self.cargar_datos()

    def _formatear_descripcion(self, descripcion):
        if isinstance(descripcion, list):
            partes = []
            for item in descripcion:
                if isinstance(item, dict):
                    partes.extend(f"{clave}: {valor}" for clave, valor in item.items())
                else:
                    partes.append(str(item))
            return " | ".join(partes)

        if isinstance(descripcion, dict):
            return " | ".join(f"{clave}: {valor}" for clave, valor in descripcion.items())

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

        self.tabla = construir.tabla(
            headers=headers,
            datos=filas,
            seleccionar=self.seleccionar_registro
        )
        self.layout.addWidget(self.tabla)
