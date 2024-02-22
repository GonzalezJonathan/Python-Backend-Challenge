import pandas as pd

_PRODUCT_DF = pd.DataFrame({
  "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
  "quantity": [3, 10, 0, 5]
})

def is_product_available(product_name, quantity):
  #filtro el producto en el dataframe
  producto = _PRODUCT_DF[_PRODUCT_DF['product_name'] == product_name]

  #verifico si la cantidad de stock es suficiente
  if not producto.empty and producto['quantity'].values[0] >= quantity:
    return True
  else:
    return False

#retorna false ya que la cantidad de granizado no es suficiente      
result0 = is_product_available("Granizado", 11)

#retorna true ya que la cantidad de granizado si es suficiente
result1 = is_product_available("Granizado", 5)

print(result0)

print(result1)
