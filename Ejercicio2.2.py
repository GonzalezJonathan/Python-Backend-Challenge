import pandas as pd

_PRODUCT_DF = pd.DataFrame({
  "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
  "quantity": [0, 10, 0, 5]
})

def is_product_available(product_name, quantity):
  #filtro el producto en el dataframe
  producto = _PRODUCT_DF[_PRODUCT_DF['product_name'] == product_name]

  #variable que corresponderá a que el cliente ingrese un sabor sin stock
  producto_s_stock = _PRODUCT_DF[(_PRODUCT_DF['quantity'] == 0) & (_PRODUCT_DF['product_name'] == product_name)]

  #variable donde almaceno todos los sabores sin stock
  productos_s_stock = _PRODUCT_DF[_PRODUCT_DF['quantity'] == 0]['product_name']

  #verifico si la cantidad de stock es suficiente
  if not producto.empty and producto['quantity'].values[0] >= quantity:
    return True
  else:
    if not producto_s_stock.empty :
      print('Estimado cliente no tenemos stock de los siguientes sabores:', ', '.join(productos_s_stock))
      return False
    else:  
      print('Estimado cliente del sabor que nos pidió tenemos la siguiente cantidad: ',producto['quantity'].values[0])
      return False

#retorna true ya que la cantidad de granizado si es suficiente
result = is_product_available("Granizado", 15)

print(result)