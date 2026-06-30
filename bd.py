from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson import ObjectId


class BaseDatos:

    def __init__(self):
        self.error = ""
        self.cliente = MongoClient(
            "mongodb+srv://samdxga_db_user:VTU5HJH9c4jU1D4D@cluster0.ajxnbri.mongodb.net/",
            serverSelectionTimeoutMS=5000
        )
        self.db = self.cliente["ctech"]

    # =====================================================
    # UTILIDADES
    # =====================================================

    def _guardar_error(self, accion, error):
        self.error = f"No se pudo {accion}: {error}"
        print(self.error)

    def _listar(self, cursor, accion="cargar datos"):
        try:
            self.error = ""
            return list(cursor)
        except PyMongoError as error:
            self._guardar_error(accion, error)
            return []

    def _uno(self, consulta, accion="buscar registro"):
        try:
            self.error = ""
            return consulta
        except PyMongoError as error:
            self._guardar_error(accion, error)
            return None

    def _filtro_id(self, id_registro):
        candidatos = []

        def agregar(valor):
            if valor not in candidatos:
                candidatos.append(valor)

        agregar(id_registro)

        id_texto = str(id_registro).strip()
        if ObjectId.is_valid(id_texto):
            agregar(ObjectId(id_texto))

        if id_texto.isdigit():
            agregar(int(id_texto))

        if len(candidatos) == 1:
            return {"_id": candidatos[0]}

        return {"_id": {"$in": candidatos}}

    def _insertar(self, coleccion, datos, accion):
        try:
            self.error = ""
            resultado = coleccion.insert_one(datos)
            print(accion)
            return resultado.inserted_id
        except PyMongoError as error:
            self._guardar_error(accion.lower(), error)
            return None

    def _actualizar(self, coleccion, id_registro, datos, accion):
        try:
            self.error = ""
            resultado = coleccion.update_one(
                self._filtro_id(id_registro),
                {"$set": datos}
            )
            print(accion)
            return resultado.modified_count
        except PyMongoError as error:
            self._guardar_error(accion.lower(), error)
            return 0

    def _eliminar(self, coleccion, id_registro, accion):
        try:
            self.error = ""
            resultado = coleccion.delete_one(self._filtro_id(id_registro))
            print(accion)
            return resultado.deleted_count
        except PyMongoError as error:
            self._guardar_error(accion.lower(), error)
            return 0

    # =====================================================
    # CLIENTES
    # =====================================================

    def ver_clientes(self):
        return self._listar(self.db.clientes.find(), "cargar clientes")

    def buscar_cliente(self, id_cliente):
        try:
            self.error = ""
            return self.db.clientes.find_one(self._filtro_id(id_cliente))
        except PyMongoError as error:
            self._guardar_error("buscar cliente", error)
            return None

    def agregar_cliente(self, datos):
        return self._insertar(
            self.db.clientes,
            datos,
            "Cliente agregado correctamente."
        )

    def actualizar_cliente(self, id_cliente, datos):
        # Compatibilidad: si llega un texto, se asume que es el teléfono.
        if not isinstance(datos, dict):
            datos = {"telefono": datos}

        return self._actualizar(
            self.db.clientes,
            id_cliente,
            datos,
            "Cliente actualizado."
        )

    def eliminar_cliente(self, id_cliente):
        return self._eliminar(
            self.db.clientes,
            id_cliente,
            "Cliente eliminado."
        )

    # =====================================================
    # PRODUCTOS
    # =====================================================

    def ver_productos(self):
        return self._listar(self.db.productos.find(), "cargar productos")

    def buscar_categoria(self, categoria):
        return self._listar(
            self.db.productos.find({"categoria": categoria}),
            "buscar productos por categoría"
        )

    def buscar_precio(self, minimo, maximo):
        return self._listar(
            self.db.productos.find({"precio": {"$gte": minimo, "$lte": maximo}}),
            "buscar productos por precio"
        )

    def buscar_stock(self):
        return self._listar(
            self.db.productos.find({"stock": {"$lt": 15}}),
            "buscar productos por stock"
        )

    def ordenar_precio(self):
        return self._listar(
            self.db.productos.find().sort("precio", 1),
            "ordenar productos por precio"
        )

    def agregar_producto(self, datos):
        return self._insertar(
            self.db.productos,
            datos,
            "Producto agregado."
        )

    def actualizar_producto(self, id_producto, datos):
        return self._actualizar(
            self.db.productos,
            id_producto,
            datos,
            "Producto actualizado."
        )

    def actualizar_stock(self, id_producto, stock):
        return self._actualizar(
            self.db.productos,
            id_producto,
            {"stock": stock},
            "Stock actualizado."
        )

    def eliminar_producto(self, id_producto):
        return self._eliminar(
            self.db.productos,
            id_producto,
            "Producto eliminado."
        )

    # =====================================================
    # PEDIDOS
    # =====================================================

    def ver_pedidos(self):
        return self._listar(self.db.pedidos.find(), "cargar pedidos")

    def buscar_pedido_cliente(self, id_cliente):
        return self._listar(
            self.db.pedidos.find({"id_cliente": id_cliente}),
            "buscar pedidos por cliente"
        )

    def buscar_estado(self, estado):
        return self._listar(
            self.db.pedidos.find({"estado": estado}),
            "buscar pedidos por estado"
        )

    def agregar_pedido(self, datos):
        return self._insertar(
            self.db.pedidos,
            datos,
            "Pedido agregado."
        )

    def actualizar_pedido(self, id_pedido, datos):
        return self._actualizar(
            self.db.pedidos,
            id_pedido,
            datos,
            "Pedido actualizado."
        )

    def actualizar_estado(self, id_pedido, estado):
        return self._actualizar(
            self.db.pedidos,
            id_pedido,
            {"estado": estado},
            "Estado actualizado."
        )

    def eliminar_pedido(self, id_pedido):
        return self._eliminar(
            self.db.pedidos,
            id_pedido,
            "Pedido eliminado."
        )

    def historial_cliente(self, id_cliente):
        return self._listar(
            self.db.pedidos.find({"id_cliente": id_cliente}),
            "cargar historial del cliente"
        )

    def pedidos_fecha(self, inicio, fin):
        return self._listar(
            self.db.pedidos.find({"fecha_pedido": {"$gte": inicio, "$lte": fin}}),
            "buscar pedidos por fecha"
        )

    # =====================================================
    # EMPLEADOS
    # =====================================================

    def ver_empleados(self):
        return self._listar(self.db.empleados.find(), "cargar empleados")

    def login(self, correo, contraseña):
        try:
            self.error = ""
            empleado = self.db.empleados.find_one({
                "correo": correo,
                "contraseña": contraseña
            })
            return empleado is not None
        except PyMongoError as error:
            self._guardar_error("iniciar sesión", error)
            return False

    def buscar_administradores(self):
        return self._listar(
            self.db.empleados.find({"rol": "Administrador"}),
            "buscar administradores"
        )

    # =====================================================
    # CONSULTAS AVANZADAS
    # =====================================================

    def pedidos_clientes(self):
        consulta = [
            {
                "$lookup": {
                    "from": "clientes",
                    "localField": "id_cliente",
                    "foreignField": "_id",
                    "as": "cliente"
                }
            }
        ]

        return self._listar(
            self.db.pedidos.aggregate(consulta),
            "cargar pedidos con clientes"
        )

    def total_por_cliente(self):
        consulta = [
            {
                "$group": {
                    "_id": "$id_cliente",
                    "Total Comprado": {"$sum": "$total_pedido"}
                }
            }
        ]

        return self._listar(
            self.db.pedidos.aggregate(consulta),
            "calcular total por cliente"
        )

    def producto_mas_vendido(self):
        consulta = [
            {"$unwind": "$productos_pedidos"},
            {
                "$group": {
                    "_id": "$productos_pedidos.id_producto",
                    "Cantidad": {"$sum": "$productos_pedidos.cantidad"}
                }
            },
            {"$sort": {"Cantidad": -1}}
        ]

        return self._listar(
            self.db.pedidos.aggregate(consulta),
            "buscar producto más vendido"
        )
