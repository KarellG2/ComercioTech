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
1.  COLOR_PRINCIPAL = '#864194'
2.  HOVER_COLOR     = '#00FFAA'
3.  BLANCO          = '#F1F1F1'
4.  ROJO            = '#e93103'
5.  NEGRO           = '#222a40'

=================================================================================================================================================


# MODULO principal / main.py

## El script principal, administrador del ciclo de vida de la aplicacion

=================================================================================================================================================

## Modulo main - Clase ventanaPrincipal

1.  Hereda de la clase QMainWindow y establece "MercadoTech" como titulo principal

2.  Define una resolucion de 800x550 pixeles y un fondo general con la constante NEGRO

3.  Implementa un control de visualizacion con el controlador QStacckedWidget, para apilar diferentes pantallas, iniciando con la vista principla pantalla_inicio


=================================================================================================================================================


## Modulo login - Clase pantallaInicio

1.  Hereda QWidget y estructura el layout principal

2.  Integra el metodo header("ComercioTech") desde el modulo Constructor.py

    3.- Renderiza el contenedor central con un texto indicando un subtitulo: "Venta de Articulos Tecnologicos"