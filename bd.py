from pymongo import MongoClient
from pymongo.errors import PyMongoError, ServerSelectionTimeoutError


class BaseDatos:
    def __init__(self):
        self.error = None
        self.cliente = MongoClient(
            "mongodb+srv://samdxga_db_user:VTU5HJH9c4jU1D4D@cluster0.ajxnbri.mongodb.net/",
            serverSelectionTimeoutMS=5000
        )
        self.db = self.cliente["ctech"]

    def probar_conexion(self):
        try:
            self.cliente.admin.command("ping")
            self.error = None
            return True
        except ServerSelectionTimeoutError as error:
            self.error = f"No se pudo conectar a MongoDB: {error}"
            return False
        except PyMongoError as error:
            self.error = f"Error de MongoDB: {error}"
            return False

    def _listar(self, cursor):
        try:
            datos = list(cursor)
            self.error = None
            return datos
        except PyMongoError as error:
            self.error = f"Error de MongoDB: {error}"
            return []

    def _imprimir_lista(self, datos):
        for dato in datos:
            print(dato)

    # =====================================================
    # CLIENTES
    # =====================================================

    def ver_clientes(self):
        clientes = self._listar(self.db.clientes.find())
        self._imprimir_lista(clientes)
        return clientes

    def buscar_cliente(self, id_cliente):
        try:
            cliente = self.db.clientes.find_one({"_id": id_cliente})
            self.error = None
            print(cliente)
            return cliente
        except PyMongoError as error:
            self.error = f"Error de MongoDB: {error}"
            print(self.error)
            return None

    def agregar_cliente(self, datos):
        try:
            self.db.clientes.insert_one(datos)
            self.error = None
            print("Cliente agregado correctamente.")
            return True
        except PyMongoError as error:
            self.error = f"No se pudo agregar el cliente: {error}"
            print(self.error)
            return False

    def actualizar_cliente(self, id_cliente, telefono):
        try:
            resultado = self.db.clientes.update_one(
                {"_id": id_cliente},
                {"$set": {"telefono": telefono}}
            )
            self.error = None
            print("Cliente actualizado.")
            return resultado.modified_count > 0
        except PyMongoError as error:
            self.error = f"No se pudo actualizar el cliente: {error}"
            print(self.error)
            return False

    def eliminar_cliente(self, id_cliente):
        try:
            resultado = self.db.clientes.delete_one({"_id": id_cliente})
            self.error = None
            print("Cliente eliminado.")
            return resultado.deleted_count > 0
        except PyMongoError as error:
            self.error = f"No se pudo eliminar el cliente: {error}"
            print(self.error)
            return False

    # =====================================================
    # PRODUCTOS
    # =====================================================

    def ver_productos(self):
        productos = self._listar(self.db.productos.find())
        self._imprimir_lista(productos)
        return productos

    def buscar_categoria(self, categoria):
        productos = self._listar(self.db.productos.find({"categoria": categoria}))
        self._imprimir_lista(productos)
        return productos

    def buscar_precio(self, minimo, maximo):
        productos = self._listar(
            self.db.productos.find({"precio": {"$gte": minimo, "$lte": maximo}})
        )
        self._imprimir_lista(productos)
        return productos

    def buscar_stock(self):
        productos = self._listar(self.db.productos.find({"stock": {"$lt": 15}}))
        self._imprimir_lista(productos)
        return productos

    def ordenar_precio(self):
        productos = self._listar(self.db.productos.find().sort("precio", 1))
        self._imprimir_lista(productos)
        return productos

    def agregar_producto(self, datos):
        try:
            self.db.productos.insert_one(datos)
            self.error = None
            print("Producto agregado.")
            return True
        except PyMongoError as error:
            self.error = f"No se pudo agregar el producto: {error}"
            print(self.error)
            return False

    def actualizar_stock(self, id_producto, stock):
        try:
            resultado = self.db.productos.update_one(
                {"_id": id_producto},
                {"$set": {"stock": stock}}
            )
            self.error = None
            print("Stock actualizado.")
            return resultado.modified_count > 0
        except PyMongoError as error:
            self.error = f"No se pudo actualizar el stock: {error}"
            print(self.error)
            return False

    def eliminar_producto(self, id_producto):
        try:
            resultado = self.db.productos.delete_one({"_id": id_producto})
            self.error = None
            print("Producto eliminado.")
            return resultado.deleted_count > 0
        except PyMongoError as error:
            self.error = f"No se pudo eliminar el producto: {error}"
            print(self.error)
            return False

    # =====================================================
    # PEDIDOS
    # =====================================================

    def ver_pedidos(self):
        pedidos = self._listar(self.db.pedidos.find())
        self._imprimir_lista(pedidos)
        return pedidos

    def buscar_pedido_cliente(self, id_cliente):
        pedidos = self._listar(self.db.pedidos.find({"id_cliente": id_cliente}))
        self._imprimir_lista(pedidos)
        return pedidos

    def buscar_estado(self, estado):
        pedidos = self._listar(self.db.pedidos.find({"estado": estado}))
        self._imprimir_lista(pedidos)
        return pedidos

    def actualizar_estado(self, id_pedido, estado):
        try:
            resultado = self.db.pedidos.update_one(
                {"_id": id_pedido},
                {"$set": {"estado": estado}}
            )
            self.error = None
            print("Estado actualizado.")
            return resultado.modified_count > 0
        except PyMongoError as error:
            self.error = f"No se pudo actualizar el pedido: {error}"
            print(self.error)
            return False

    def eliminar_pedido(self, id_pedido):
        try:
            resultado = self.db.pedidos.delete_one({"_id": id_pedido})
            self.error = None
            print("Pedido eliminado.")
            return resultado.deleted_count > 0
        except PyMongoError as error:
            self.error = f"No se pudo eliminar el pedido: {error}"
            print(self.error)
            return False

    def historial_cliente(self, id_cliente):
        historial = self._listar(self.db.pedidos.find({"id_cliente": id_cliente}))
        self._imprimir_lista(historial)
        return historial

    def pedidos_fecha(self, inicio, fin):
        pedidos = self._listar(
            self.db.pedidos.find({"fecha_pedido": {"$gte": inicio, "$lte": fin}})
        )
        self._imprimir_lista(pedidos)
        return pedidos

    # =====================================================
    # EMPLEADOS
    # =====================================================

    def ver_empleados(self):
        empleados = self._listar(self.db.empleados.find())
        self._imprimir_lista(empleados)
        return empleados

    def login(self, correo, contrasena):
        try:
            empleado = self.db.empleados.find_one({
                "correo": correo,
                "$or": [
                    {"contrasena": contrasena},
                    {"contraseña": contrasena}
                ]
            })
            self.error = None
        except PyMongoError as error:
            self.error = f"Error de MongoDB: {error}"
            print(self.error)
            return None

        if empleado:
            print("Inicio de sesion correcto.")
        else:
            print("Correo o contrasena incorrectos.")

        return empleado

    def buscar_administradores(self):
        administradores = self._listar(self.db.empleados.find({"rol": "Administrador"}))
        self._imprimir_lista(administradores)
        return administradores

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

        try:
            resultado = self._listar(self.db.pedidos.aggregate(consulta))
        except PyMongoError as error:
            self.error = f"Error de MongoDB: {error}"
            print(self.error)
            return []

        self._imprimir_lista(resultado)
        return resultado

    def total_por_cliente(self):
        consulta = [
            {
                "$group": {
                    "_id": "$id_cliente",
                    "Total Comprado": {"$sum": "$total_pedido"}
                }
            }
        ]

        try:
            resultado = self._listar(self.db.pedidos.aggregate(consulta))
        except PyMongoError as error:
            self.error = f"Error de MongoDB: {error}"
            print(self.error)
            return []

        self._imprimir_lista(resultado)
        return resultado

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

        try:
            resultado = self._listar(self.db.pedidos.aggregate(consulta))
        except PyMongoError as error:
            self.error = f"Error de MongoDB: {error}"
            print(self.error)
            return []

        self._imprimir_lista(resultado)
        return resultado
