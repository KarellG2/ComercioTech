## Explicacion de los Modulos
MercadoTech es una aplicacion de escritorio desarrollada con la libreria PyQt6
Utiliza una arquitectura modular con el paradigma de Programacion Orientada a Objetos con el objetivo de optimizar la reutilizacion de codigo y fomentar la escalabilidad del proyecto


## Arquitectura de Modulos

## MODULO Constructor.py

> Este modulo provee las plantillas para los componentes de la interfaz grafica de usuario. Contiene la clase Construir que encapsula la logica de la creacion de widgets

=================================================================================================================================================

# 1.- header(self, texto, font_size= 30)
    1.1 Retorna un contenedor QFrame con una altura fija de 75 pixeles
    
    1.2 Aplica un color de fondo definido por la constante COLOR_PRINCIPAL en Constants.py 
    
    1.3 Renderiza un QLabel que contiene el argumento texto configurado con color blanco por defecto y tipologia negrita

    1.4 El argumento font_size define un tamaño fijo para el header de 30 pixeles



# 2.- boton(self, texto, comando, color, fg=None, width=210, height= 50)

    2.1 La funcion boton instala elementos QPushButton estandarizados en la interfaz grafica

    2.2 El parametro "comando" enlaza el componente a una funcion mediante el evento "clicked"

    2.3 El parametro color determina un color en hexadecimal para el fondo / relleno del boton

    2.4 El parametro fg determina el color del texto, la logica del renderizado asigna un texto blanco por defecto si el color de relleno es rojo, en caso contrario y si no se asigno otro color el fg asume un color negro

    2.5 Los parametros "width" y "height" controlan la geometria y area clickeable del boton

    2.6 La implementacion de la pseudoclase ":hover" permite alterar dinamicamente la visualizacion con el valor "HOVER_COLOR" al interactuar con el cursor


=================================================================================================================================================


## MODULO Constantes.py

# Este modulo actua como un registro de las configuraciones globales visuales, centralizando las constantes de tamaños y colores

=================================================================================================================================================

# Paleta de Colores Declarada:
    1.- COLOR_PRINCIPAL = '#864194'
    2.- HOVER_COLOR     = '#00FFAA'
    3.- BLANCO          = '#F1F1F1'
    4.- ROJO            = '#e93103'
    5.- NEGRO           = '#222a40'

=================================================================================================================================================


## MODULO principal / main.py

# El script principal, administrador del ciclo de vida de la aplicacion

=================================================================================================================================================

# Clase ventanaPrincipal

    1.- Hereda de la clase QMainWindow y establece "MercadoTech" como titulo principal

    2.- Define una resolucion de 800x550 pixeles y un fondo general con la constante NEGRO

    3.- Implementa un control de visualizacion con el controlador QStacckedWidget, para apilar diferentes pantallas, iniciando con la vista principla pantalla_inicio


=================================================================================================================================================


# Clase pantallaInicio

    1.- Hereda QWidget y estructura el layout principal

    2.- Integra el metodo header("MercadoTech") desde el modulo Constructor.py

    3.- Renderiza el contenedor central con un texto indicando un subtitulo: "Venta de Articulos Tecnologicos"




=================================================================================================================================================



## MODULO de Base de Datos / bd.py

Este módulo gestiona la conexión, persistencia y procesamiento NoSQL con la base de datos distribuida MongoDB clúster `ctech`. Centraliza la lógica de negocio mediante la clase `BaseDatos`, proveyendo soporte multiplataforma (Windows/Linux) seguro y escalable.

=================================================================================================================================================

# 1.- Justificación Técnica del DBMS (MongoDB)

    1.- Modelado Flexible: Representando las entidades complejas (Clientes, Productos, Empleados y Pedidos) como documentos JSON/BSON dinámicos, adaptándose a la variabilidad de atributos sin alterar los esquemas rígidos.
    
    2.- Escalabilidad Nativa: Soporta el crecimiento horizontal mediante sharding distribuyendo colecciones de forma automática entre múltiples nodos, garantizando el rendimiento ante un alto volumen de transacciones de MercadoTech.
    
    3.- Alta Disponibilidad (Replica Sets): Implementa las tolerancias a fallos mediante replicación automatizada, asegurando la continuidad operativa y failover automático si el nodo primario llega a quedar inaccesible.
    
    4.- Seguridad Integral: Capacidad nativa de aislamiento mediante mecanismos de autenticación robustos, control de acceso basado en roles (RBAC) y soporte para cifrado de datos tanto en tránsito (TLS/SSL) como en reposo.


# 2.- Esquema de Datos y Diccionario de Colecciones

    1.- Colección "clientes"
    Almacena la información de contacto de los compradores.
    - Campos: _id (ObjectId), nombre (str), rut (Int), correo (str), fecha_creacion (DateTime).
    
    Ejemplo de documento:
    ```json
    {
        "_id": "667cb4a2f1d2c3a4b5e6f7a8",
        "nombre": "ABCDE",
        "rut": 123456789,
        "correo": "ABCDE@GMAIL.COM",
        "fecha_creacion": "10-10-2010 13:00:00"
    }
    ```

    2.- Colección "empleados"
    Almacena las credenciales y el control de acceso diferido según el nivel de privilegios asignado. 
    Se aplica directivas de seguridad protegiendo contraseñas mediante funciones hash.
    - Campos: _id (ObjectId), nombre (str), rut (str), correo (str), telefono (str), 
    cargo (String), rol (String), fecha_contrato (DateTime), contraseña (str/hash).
    
    Ejemplo de documento:
    ```json
    {
        "_id": "667cb4a2f1d2c3a4b5e6f7a9",
        "nombre": "BCDE",
        "rut": "987654321-K",
        "correo": "BCDE@GMAIL.COM",
        "telefono": "+56912346789",
        "cargo": "Administrador",
        "rol": "admin",
        "fecha_contrato": "01-01-2001 09:30:04",
        "contrasena": "$2b$12$eImiTxAk4vmM8Kj3W..."
    }
    ```

    3.- Colección "productos"
    Almacena la información de los productos registrados en el sistema, dependiendo del producto su descripción
    puede ser una lista con un datos mas especificos.
    - Campos: _id (ObjectId), nombre (str), descripcion (lista), precio (Int), categoria (str), stock (Int).
    
    Ejemplo de documento:
    ```json
    {
        "_id": "667cb4a2f1d2c3a4b5e6f7b0",
        "nombre": "monitor",
        "descripcion": [
            { "hz": 1000 },
            { "tamano_cm": 70 }
        ],
        "precio": 150000,
        "categoria": "computacion",
        "stock": 25
    }
    ```

    4.- Colección "pedidos"
    Almacena el procesamiento de boletas de venta. Relacionandose con las entidades mediante referencias cruzadas a través del identificador del cliente, integrando un subdocumento que contiene el identificador del producto, nombre, precio y cantidad de los ítems comprados.
    - Campos: _id (ObjectId), id_cliente (ObjectId), fecha_pedido (DateTime), productos_pedidos (lista), total_pedido (Int), estado (str).
    
    Ejemplo de documento:
    ```json
    {
        "_id": "667cb4a2f1d2c3a4b5e6f7b1",
        "id_cliente": "667cb4a2f1d2c3a4b5e6f7a8",
        "fecha_pedido": "2026-06-26T22:30:00Z",
        "productos_pedidos": [
            {
                "id_producto": "667cb4a2f1d2c3a4b5e6f7b0",
                "nombre": "monitor",
                "precio": 150000,
                "cantidad": 1
            }
        ],
        "total_pedido": 150000,
        "estado": "entregado"
    }
    ```


# 3.- Mapeo de Operaciones y Cobertura de Requisitos de Negocio

    1.- Gestión de Clientes: Métodos funcionales `agregar_cliente()`, `actualizar_cliente()`, `eliminar_cliente()` y `buscar_cliente()`. Cubre el ciclo completo de operaciones CRUD operando directamente con comandos (`insert_one`, `update_one`, `delete_one`).
    
    2.- Gestión de Productos: Métodos funcionales `agregar_producto()`, `actualizar_producto()` y `eliminar_producto()`. Permite el aprovisionamiento dinámico de existencias y actualizaciones críticas del stock.
    
    3.- Gestión de Pedidos y Generación de Boletas: Resuelto mediante operaciones de agregación complejas. El método `pedidos_clientes()` implementa la etapa `$lookup` para cruzar dinámicamente la colección de pedidos con los metadatos del cliente emisor del flujo. Los estados transicionales quedan validados mediante marcas de tiempo (timestamp) en el campo `fecha_pedido`.
    
    4.- Historial de Transacciones: El pipeline analítico implementado permite consultar el comportamiento histórico de compras y calcular resúmenes contables automáticos por cliente usando la agregación `$group` y operadores lógicos como `$sum` dentro del método `total_por_cliente()`.
    
    5.- Inteligencia de Negocio / Reportes: El método `producto_mas_vendido()` ejecuta un pipeline de agregación avanzado que es una desestructura de arreglos internos mediante `$unwind`, consolidando las cantidades vendidas por identificador usando el `$group` y ordena descendentemente mediante `$sort` para extraer el top de artículos líderes en ventas.