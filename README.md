# Bienvenido al Repositorio de Resolución de Challenges para InceptIA

¡Hola! Gracias por visitar mi repositorio donde resolví el challenge propuesto por InceptIA. Aquí encontrarás la solución a los desafíos planteados y las instrucciones para ejecutar el código.

## Antes de Comenzar

Antes de ejecutar los archivos, asegúrate de seguir estos pasos:

1. Instala la librería `requests` de Python ejecutando el siguiente comando:
   ```bash
   pip install requests
   ```

2. Instala la librería `pandas` de Python con el siguiente comando:
   ```bash
   pip install pandas
   ```

Estas bibliotecas son esenciales para el correcto funcionamiento de los archivos.

## Ejecución de los Archivos

Una vez que hayas instalado las librerías necesarias, puedes ejecutar cada uno de los archivos para obtener la resolución de los desafíos.

## Explicación de la Solución del Ejercicio 2.2

En el ejercicio 2.2, abordé la problemática de posibles bucles infinitos. Para evitar situaciones en las que el cliente elige sabores de helado sin stock, he implementado una mejora en la función. Ahora, si el cliente selecciona un sabor sin stock, se le mostrará una lista de todos los sabores agotados, evitando así que continúe eligiendo opciones no disponibles.

Además, he considerado otra situación en la que el cliente elige un sabor con stock limitado. En este caso, la función devuelve un mensaje informando al cliente sobre la cantidad disponible de ese sabor específico. Con estas dos mejoras, se garantiza una solución efectiva para evitar bucles infinitos y proporcionar información clara al cliente.

## Agradecimientos

¡Gracias por revisar mi trabajo y considerar mi aplicación para el puesto de Python Developer en InceptIA!
