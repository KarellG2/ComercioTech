## Explicacion de los Modulos
ComercioTech es una aplicacion de escritorio desarrollada con la libreria PyQt6
Utiliza una arquitectura modular con el paradigma de Programacion Orientada a Objetos con el objetivo de optimizar la reutilizacion de codigo y fomentar la escalabilidad del proyecto


## Arquitectura de Modulos

## MODULO Constructor.py

> Este modulo provee las plantillas para los componentes de la interfaz grafica de usuario. Contiene la clase Construir que encapsula la logica de la creacion de widgets

=================================================================================================================================================

# 1.- header(self, texto, font_size= 30)

    1.1 Retorna un contenedor QFrame con una altura fija de 195 pixeles que es utilizado como encabezado dentro de una vista
    
    1.2 Recibe el parametro texto que define el contenido que se visualizara en el encabezado de la vista que la utilice 
    
    1.3 El parametro font_size modifica el tamaño del texto del encabezado, por defecto tiene un valor de 30 pixeles


# 2.- boton(self, texto, comando, color, fg=None, width=210, height= 50)

    2.1 La funcion "boton" crea y returna un componente "QPushButton" estandarizado.

    2.2 El parametro "texto" define el contenido del boton

    2.3 El parametro "comando" permite otorgarle al boton una funcion, la cual se ejecuta mediante el evento "clicked"

    2.4 "Color" define el color de fondo del boton, el cual puede ser entregado mediante el modulo "constantes.py" o con valores hexadecimales.

    2.5 "fg" Define el color del texto, en caso de no entregarse valor el metodo asigna automaticamente un color dependiendo del color de fondo utilizado.

    2.6 La funcion "fg" detecta si el color de fondo es "ROJO", "NEGRO" o "COLOR_PRINCIPAL" y asigna al boton el color "BLANCO".

    2.7 Los parametros "width" y "height" definen la geometria del boton, por defecto reciben el valor 210 y 50 respectivamente

    2.8 Los bordes del boton son redondeados automaticamente, calculando la altura otorgada.

    2.9 El metodo implementa el efecto visual "hover", lo que le permite cambiar de color cuando el usuario posiciona el cursor sobre el.


# 3.- entrada(self, comando=None, color= None, fg= None, width= 210, height= 50)

    3.1 La funcion entrada genera dos labels para ingreso de datos, uno sirve para describir el tipo de informacion que se espera recibir, mientras que el otro recibe los caracteres ingresados
    
    3.2 Los elementos retornados son un "QLabel" y un "QLineEdit".
    
    3.3 El elemento "QLabel" es utilizado para mostrar el nombre o descripcion del campo.

    3.4 El parametro "label_texto" genera un valor por defecto al elemento descriptivo de la entrada de texto.

    3.5 El parametro "Placeholder" permite mostrar un texto de a ayuda y/o ejemplo visible dentro del campo de entrada, sin modificar el valor real ingresado por el usuario.

    3.6 El parametro "color" define el color de fondo del campo de entrada, si no se entrega ningun valor el fondo queda transparente.

    3.7 El parametro "fg" define el color del texto, si no se entregara valor se utiliza la constante "BLANCO".

    3.8 Los parametros "width" y "height" definen la geometria del campo de entrada, por defecto reciben los valores 210 y 40 respectivamente.

    3.9 Cuandl un campo recibe el foco el borde cambia su color a "HOVER_COLOR"

    3.10 El parametro "Password" permite ocultar los caracteres ingresados, por defecto recibe un valor "False", este es utilizado en el ingreso de contraseña en la vista "login"

#   4.- sidebar(self, items, stack, logo, width=210, active_index=0)

    4.1 El metodo "sidebar" genera el menu lateral que se utiliza para la navegacion entre vistas.

    4.2 Se retorna un contenedor "QFrame" con botones de navegacion construidos a partir de una lista.

    4.3 El parametro items recibe una lista de diccionarios que representan una opcion del menu de navegacion.

    4.4 Cada elemento de "items" contiene las claves "texto", "icono" e "index" 

    4.5 La clave "texto" define el nombre del boton en el menu.

    4.6 La clave "icono" permite ingresar una imagen / texto adicional antes del nombre del boton, de no ser entregado algun valor el boton solo mostrara el texto.

    4.7 La clave index indica la posicion dentro del "QStackedWidget".

    4.8 El parametro "stack" recibe el "QStackedWidget" que controla las vistas del panel.

    4.9 Al presionar un boton del menu la vista cambia mediante "stack.setCurrentIndex(index)".

    4.10 El parametro "logo" define el textode la parte superior del menu lateral, actualmente se utiliza el nombre de la organizacion.

    4.11 el parametro "width" define el ancho de la barra lateral, por defecto su valor es de 210 pixeles.

    4.12 el parametro "active_index" define que index se mostrara como activo al cargar la interfaz.

    4.13 El metodo utiliza dos estilos visuales, uno para el boton "activo" y el otro para los "inactivos", al ser presionada una opcion el boton cambia a ser "activo" y los otros cambian a "inactivo".

    4.14 El metodo esta centralizado en el archivo "main.py" para evitar la repeticion de codigo.

#   5.- tabla(self, headers=None, datos=None, width=None, height=None, seleccionar=None)

    5.1 El metodo "tabla" genera una tabla utilizando el componente "QTableWidget"

    5.2 El parametro "headers" recibe la lista con los nombres de los campos de la tabla.

    5.3 El parametro "datos" recibe una lista con las filas que contienen los valores a las columnas definidas con "headers"

    5.4 En caso de no entregarse "headers" ni "datos" se genera una lista vacia evitando errores al momento de crear la tabla.

    5.5 El metodo tiene una funcion llamada "formatar_valor" que se encarga de convertir los valores recibidos a texto, pudiendo recibir el parametro "datos" con listas.

    5.6 La tabla esta configurada como solo lectura, evitando modificar los datos en las celdas.

    5.7 La seleccion de datos se realiza con la fila completa.

    5.8 Solo se permite seleccionar una fila a la vez, esto con la finalidad de evitar errores.

    5.9 El metodo ajusta automaticamente el tamaño de las filas y columnas segun el contenido.

    5.10 Los parametros "width" y "height" definen la geometria de la tabla.

    5.11 El parametro "seleccionar" permite recibir una funcion  a ejecutar cuando el usuario selecciona una fila.

    5.12 La finalidad del parametro "seleccionar" es facilitar la implementacion de botones como "editar", "eliminar" o "ver detalles", ya que permite obtener los datos de la fila seleccionada.


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

    1.- Hereda de la clase QMainWindow y establece "ComercioTech" como titulo principal

    2.- Define una resolucion de 800x550 pixeles y un fondo general con la constante NEGRO

    3.- Implementa un control de visualizacion con el controlador QStacckedWidget, para apilar diferentes pantallas, iniciando con la vista principla pantalla_inicio


=================================================================================================================================================


# Clase pantallaInicio

    1.- Hereda QWidget y estructura el layout principal

    2.- Integra el metodo header("ComercioTech") desde el modulo Constructor.py

    3.- Renderiza el contenedor central con un texto indicando un subtitulo: "Venta de Articulos Tecnologicos"




=================================================================================================================================================



## MODULO de Base de Datos / bd.py

Este módulo gestiona la conexión, persistencia y procesamiento NoSQL con la base de datos distribuida MongoDB clúster `ctech`. Centraliza la lógica de negocio mediante la clase `BaseDatos`, proveyendo soporte multiplataforma (Windows/Linux) seguro y escalable.

=================================================================================================================================================

# 1.- Justificación Técnica del DBMS (MongoDB)

    1.- Modelado Flexible: Representando las entidades complejas (Clientes, Productos, Empleados y Pedidos) como documentos JSON/BSON dinámicos, adaptándose a la variabilidad de atributos sin alterar los esquemas rígidos.
    
    2.- Escalabilidad Nativa: Soporta el crecimiento horizontal mediante sharding distribuyendo colecciones de forma automática entre múltiples nodos, garantizando el rendimiento ante un alto volumen de transacciones de ComercioTech.
    
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