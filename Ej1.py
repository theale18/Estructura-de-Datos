"""
Implementar el TDA "Propiedad" que modela un inmueble, con una estructura definida por los siguientes componentes:
  - Calle
  - Número
  - Localidad
  - Año de construcción
  - Cantidad de ambientes

Implementar las siguientes operaciones:
  - Constructor: Debe incluir las validaciones necesarias, teniendo en cuenta que solo se almacenan propiedades construidas luego de 1870.
  - __repr__: Al usar la función print con una variable del tipo propiedad debe mostrar: 'calle' 'numero' ('localidad').
  - mismaLocalidad: Operación que recibe dos propiedades y retorna True si estan en la misma localidad y False en caso contrario.
  - mayorNumeración: Operación que recibe dos propiedades y si están en la misma calle, retorna la que posee mayor numeración. Si están calles diferentes debe lanzar una excepción.
  - calculaImpuestoARBA: Operación que retorna el porcentaje de impuesto inmobiliario de una propiedad, según la siguiente regla:
    *  Propiedades entre 1870 y 1949:
      - Entre 1 y 3 ambientes: 5% de impuesto
      - Entre 4 y 6 ambientes: 10% de impuesto
      - Más de 6 ambientes: 25 % de impuesto
    *  Propiedades desde 1950 hasta la actualidad:
      - Entre 1 y 5 ambientes: 5% de impuesto
      - Más de 5 ambientes: 35 % de impuesto
"""
class Propiedad:
  def __init__(self, calle, numero, localidad, año, cantAmb):
      self._calle = calle
      self._numero = validarTipo(numero, "numero", int)
      self._localidad = localidad
      self._año = año
      self._cantAmb = cantAmb

# def __repr__(self):
#    return self._calle + str(self._numero) + self._localidad + self._año.__repr__() +  señf._cantAmb.__repr__()

  def __impPropAntigua(self, ambientes):
    resul = 0
    if ambientes <= 3:
      resul = 5
    elif ambientes >= 4 and ambientes <= 6 :
      resul = 10
    else :
      resul = 25
    return resul

  def __impPropNueva(self, ambientes):
    resul = 0
    if ambientes <= 5:
      resul = 5
    else :
      resul = 35
    return resul

  def calcPorcImp(self):
    if self._año < 1950:
      return self.__impPropAntigua(self._cantAmb)
    else:
      return self.__impPropNueva(self._cantAmb)

  def mismaLocalidad(self, prop2):
    return self._localidad == prop2._localidad

  def __repr__(self):
    return self._calle + " " + self._numero.__repr__() + self._localidad + " " + self._año.__repr__() + " " +  self._cantAmb.__repr__()

prop1 = Propiedad("calle", 111, "localidad", 1999, 1)
prop2 = Propiedad("calle", 111, "localidad", 1999, 1)
prop3 = Propiedad("calle", 111, "otra localidad", 1999, 1)
print(prop1.mismaLocalidad(prop3))
print(prop1.calcPorcImp())
