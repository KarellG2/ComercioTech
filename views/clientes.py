from datetime import datetime

from PyQt6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QWidget,
    QVBoxLayout,
)

from assets.modules import Constructor
from assets.modules.Constantes import *


construir = Constructor.Construir()


class Clientes(QWidget):
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
            ["ID", "Nombre", "RUT", "Telefono", "Correo", "Fecha creacion"],
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
        clientes = self.mainWindow.bd.ver_clientes()
        filas = []
        self.documentos_por_id = {}

        for cliente in clientes:
            id_cliente = str(cliente.get("_id", ""))
            self.documentos_por_id[id_cliente] = cliente
            fila = [
                id_cliente,
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

    def agregar_registro(self):
        datos = self._mostrar_dialogo_cliente("Agregar cliente")
        if not datos:
            return

        self.mainWindow.bd.agregar_cliente(datos)
        self._recargar_tabla()

    def editar_registro(self):
        id_cliente = self._obtener_id_seleccionado()
        if not id_cliente:
            return

        cliente = self.documentos_por_id.get(id_cliente, {})
        datos = self._mostrar_dialogo_cliente("Editar cliente", cliente)
        if not datos:
            return

        self.mainWindow.bd.actualizar_cliente(id_cliente, datos)
        self.registro_seleccionado = None
        self._recargar_tabla()

    def eliminar_registro(self):
        id_cliente = self._obtener_id_seleccionado()
        if not id_cliente:
            return

        respuesta = QMessageBox.question(
            self,
            "Eliminar cliente",
            "¿Seguro que quieres eliminar el cliente seleccionado?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if respuesta != QMessageBox.StandardButton.Yes:
            return

        self.mainWindow.bd.eliminar_cliente(id_cliente)
        self.registro_seleccionado = None
        self._recargar_tabla()

    def seleccionar_registro(self, fila):
        self.registro_seleccionado = fila

    def _obtener_id_seleccionado(self):
        if not self.registro_seleccionado:
            QMessageBox.warning(self, "Sin selección", "Selecciona un registro de la tabla primero.")
            return None

        return self.registro_seleccionado.get("ID")

    def _mostrar_dialogo_cliente(self, titulo, datos=None):
        datos = datos or {}

        dialogo = QDialog(self)
        dialogo.setWindowTitle(titulo)
        dialogo.setMinimumWidth(430)
        dialogo.setStyleSheet(f"""
            QDialog {{ background-color: {NEGRO}; }}
            QLabel {{ color: {BLANCO}; font-weight: bold; }}
            QLineEdit {{
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
        input_rut = QLineEdit(str(datos.get("rut", "")))
        input_telefono = QLineEdit(str(datos.get("telefono", "")))
        input_correo = QLineEdit(str(datos.get("correo", "")))
        input_fecha = QLineEdit(str(datos.get("fecha_creacion", "") or datetime.now().strftime("%Y-%m-%d")))

        layout.addRow("Nombre", input_nombre)
        layout.addRow("RUT", input_rut)
        layout.addRow("Teléfono", input_telefono)
        layout.addRow("Correo", input_correo)
        layout.addRow("Fecha creación", input_fecha)

        botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        botones.accepted.connect(dialogo.accept)
        botones.rejected.connect(dialogo.reject)
        layout.addRow(botones)

        if dialogo.exec() != QDialog.DialogCode.Accepted:
            return None

        nombre = input_nombre.text().strip()
        if not nombre:
            QMessageBox.warning(self, "Campo obligatorio", "El nombre del cliente no puede quedar vacío.")
            return None

        return {
            "nombre": nombre,
            "rut": input_rut.text().strip(),
            "telefono": input_telefono.text().strip(),
            "correo": input_correo.text().strip(),
            "fecha_creacion": input_fecha.text().strip()
        }

    def _recargar_tabla(self):
        if hasattr(self.mainWindow, "aplicar_busqueda"):
            self.mainWindow.aplicar_busqueda()
        else:
            self.cargar_datos()

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

        self.tabla = construir.tabla(
            headers=headers,
            datos=filas,
            seleccionar=self.seleccionar_registro
        )
        self.layout.addWidget(self.tabla)
