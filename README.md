Proyecto de Visión Computacional
================================

Este repositorio contiene los archivos creados y usados para el proyecto
nombrado como "Detección de libros", el cual consiste en una interfaz donde
es posible seleccionar una fotografía de libros guardada en nuestros archivos
y de la cual es posible extraer la o las portadas de libros encontrados, así
como la extracción del texto de cada una de las portadas.

Plataforma y prerrequisitos
---------------------------

Para la elaboración de este proyecto usé Python 2.7.3 desde el sistema
operativo Ubuntu 12.04. Es necesario contar con las siguientes dependencias
que no estan incluidas en la librería estandar de Python.

Necesitamos tener instalado Tkinter para Python. Ejecuta el siguiente comando
en el terminal para instalar Tkinter:

    ~$ sudo apt-get install python-tk

El módulo de OpenCV es requisito fundamental. Ejecuta el siguiente comando
en el terminal para instalar OpenCV:

    ~$ sudo apt-get install python-opencv

También necesitamos PyTesser, que es un módulo de reconocimiento óptico de
caracteres de Python, y que es descargable desde el siguiente enlace:

[PyTesser 0.0.1](https://pytesser.googlecode.com/files/pytesser_v0.0.1.zip)

Ejecución
---------

Para ejecutar el programa desde Ubuntu es necesario abrir una terminal y ubicarse en el directorio en donde se encuentra el programa y escribir el siguiente comando:

    ~$ python bookdetection.py

Modo de uso
-----------

Una vez desplegada la interfaz gráfica de usuario, ir a la opción de Buscar Archivo, y seleccionar alguna de las imágenes proporcionadas en este mismo repositorio.

Después dar click en el botón Detectar, y esperar a que se desplieguen las portadas de los libros detectados.

Si se desea probar con otra imagen, solo es cuestión de repetir el proceso.

Acerca de
---------

El programa fue elaborado como proyecto para la clase de Visión Computacional de la carrera de Ingeniero en Tecnología de Software de la Facultad de Ingeniería Mecánica y Eléctrica, impartida por la Dra. Elisa Schaeffer.

Página de la clase:
http://elisa.dyndns-web.com/~elisa/teaching/comp/vision/2013.html

Puedes encontrar el reporte final de este proyecto en el siguiente enlace:
http://ramon-gzz.blogspot.mx/search/label/Visi%C3%B3n%20Computacional
