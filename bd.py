from pymongo import MongoClient


class BaseDatos:

    def __init__(self):
        self.cliente = MongoClient("mongodb+srv://samdxga_db_user:VTU5HJH9c4jU1D4D@cluster0.ajxnbri.mongodb.net/")

        self.db = self.cliente["ctech"]

    # =====================================================
    # CLIENTES
    # =====================================================

    def ver_clientes(self):
        clientes = self.db.clientes.find()

        for cliente in clientes:
            print(cliente)

    def buscar_cliente(self, id_cliente):
        cliente = self.db.clientes.find_one(
            {"_id": id_cliente}
        )

        print(cliente)

    def agregar_cliente(self, datos):

        self.db.clientes.insert_one(datos)

        print("Cliente agregado correctamente.")

    def actualizar_cliente(self, id_cliente, telefono):

        self.db.clientes.update_one(
            {"_id": id_cliente},
            {
                "$set": {
                    "telefono": telefono
                }
            }
        )

        print("Cliente actualizado.")

    def eliminar_cliente(self, id_cliente):

        self.db.clientes.delete_one(
            {"_id": id_cliente}
        )

        print("Cliente eliminado.")

    # =====================================================
    # PRODUCTOS
    # =====================================================

    def ver_productos(self):

        productos = self.db.productos.find()

        for producto in productos:
            print(producto)

    def buscar_categoria(self, categoria):

        productos = self.db.productos.find(
            {
                "categoria": categoria
            }
        )

        for producto in productos:
            print(producto)

    def buscar_precio(self, minimo, maximo):

        productos = self.db.productos.find(
            {
                "precio": {
                    "$gte": minimo,
                    "$lte": maximo
                }
            }
        )

        for producto in productos:
            print(producto)

    def buscar_stock(self):

        productos = self.db.productos.find(
            {
                "stock": {
                    "$lt": 15
                }
            }
        )

        for producto in productos:
            print(producto)

    def ordenar_precio(self):

        productos = self.db.productos.find().sort(
            "precio",
            1
        )

        for producto in productos:
            print(producto)

    def agregar_producto(self, datos):

        self.db.productos.insert_one(datos)

        print("Producto agregado.")

    def actualizar_stock(self, id_producto, stock):

        self.db.productos.update_one(
            {"_id": id_producto},
            {
                "$set": {
                    "stock": stock
                }
            }
        )

        print("Stock actualizado.")

    def eliminar_producto(self, id_producto):

        self.db.productos.delete_one(
            {
                "_id": id_producto
            }
        )

        print("Producto eliminado.")

    # =====================================================
    # PEDIDOS
    # =====================================================

    def ver_pedidos(self):

        pedidos = self.db.pedidos.find()

        for pedido in pedidos:
            print(pedido)

    def buscar_pedido_cliente(self, id_cliente):

        pedidos = self.db.pedidos.find(
            {
                "id_cliente": id_cliente
            }
        )

        for pedido in pedidos:
            print(pedido)

    def buscar_estado(self, estado):

        pedidos = self.db.pedidos.find(
            {
                "estado": estado
            }
        )

        for pedido in pedidos:
            print(pedido)

    def actualizar_estado(self, id_pedido, estado):

        self.db.pedidos.update_one(
            {
                "_id": id_pedido
            },
            {
                "$set": {
                    "estado": estado
                }
            }
        )

        print("Estado actualizado.")

    def eliminar_pedido(self, id_pedido):

        self.db.pedidos.delete_one(
            {
                "_id": id_pedido
            }
        )

        print("Pedido eliminado.")

    def historial_cliente(self, id_cliente):

        historial = self.db.pedidos.find(
            {
                "id_cliente": id_cliente
            }
        )

        for pedido in historial:
            print(pedido)

    def pedidos_fecha(self, inicio, fin):

        pedidos = self.db.pedidos.find(
            {
                "fecha_pedido": {
                    "$gte": inicio,
                    "$lte": fin
                }
            }
        )

        for pedido in pedidos:
            print(pedido)

    # =====================================================
    # EMPLEADOS
    # =====================================================

    def ver_empleados(self):

        empleados = self.db.empleados.find()

        for empleado in empleados:
            print(empleado)

    # def login(self, correo, contraseña):

    #     empleado = self.db.empleados.find_one(
    #         {
    #             "correo": correo,
    #             "contraseña": contraseña
    #         }
    #     )

        if empleado:
            print("Inicio de sesión correcto.")
        else:
            print("Correo o contraseña incorrectos.")

    def buscar_administradores(self):

        administradores = self.db.empleados.find(
            {
                "rol": "Administrador"
            }
        )

        for admin in administradores:
            print(admin)

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

        resultado = self.db.pedidos.aggregate(consulta)

        for dato in resultado:
            print(dato)

    def total_por_cliente(self):

        consulta = [
            {
                "$group": {
                    "_id": "$id_cliente",
                    "Total Comprado": {
                        "$sum": "$total_pedido"
                    }
                }
            }
        ]

        resultado = self.db.pedidos.aggregate(consulta)

        for dato in resultado:
            print(dato)

    def producto_mas_vendido(self):

        consulta = [
            {
                "$unwind": "$productos_pedidos"
            },
            {
                "$group": {
                    "_id": "$productos_pedidos.id_producto",
                    "Cantidad": {
                        "$sum": "$productos_pedidos.cantidad"
                    }
                }
            },
            {
                "$sort": {
                    "Cantidad": -1
                }
            }
        ]

        resultado = self.db.pedidos.aggregate(consulta)

        for dato in resultado:
            print(dato)