Bienvenidos a mi repositorio!

Aquí resolví el challenge que me han propuesto.

Antes de ejectutar el código de los archivos hay que tener en cuenta 2 cosas:
1. Instalar la librería requests de python -> "pip install requests".
2. Instalar la librería pandas de python -> "pip install pandas".

Luego de eso ya podrán ejecutar cada uno de los archivos para obtener la resolución.

Explicación de la solución del Ejercicio 2.2
En este la solución que pensé para evitar obtener un potencial loop infino fue la de, encaso de que el cliente ingrese un sabor de helado que no tenga nada de stock,
le retorno todos los sabes que no tienen stock, esto con la idea de evitar que siga eligiendo sabores los cuales no se tenga stock.
Por otro lado existía la posibilidad de que el cliente eligiera un sabor donde si tuvieramos stock pero no la cantidad que el desee, en ese caso se le retorna un mensaje
diciendole la cantidad de stock que tenemos de ese sabor.
Con esas 2  mejoras a la función anterior, tenemos la solución a un eventual loop infinito.
