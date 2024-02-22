import requests

class GeoAPI:
  API_KEY = "d81015613923e3e435231f2740d5610b"
  LAT = "-35.836948753554054"
  LON = "-61.870523905384076"
  
  @classmethod
  def is_hot_in_pehuajo(cls):
    try:
      url = f"http://api.openweathermap.org/data/2.5/weather?lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}&units=metric"
      
      res = requests.get(url)

      res.raise_for_status()

      #convierto la respuesta a formato JSON
      data = res.json()
      
      #obtengo la temperatura
      temperatura = data['main']['temp']

      # retorno un booleano según la condicion
      return temperatura > 28
    except requests.exceptions.RequestException as e:
      # muestro mensaje de error
      print(f"Error en la solicitud HTTP: {e}")
      #retorno false en caso de ocurrir error en la solicitud http
      return False
    except Exception as e:
      print(f"Error : {e}")
      return False
    
result = GeoAPI.is_hot_in_pehuajo()
print(result)
