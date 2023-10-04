"""
En la Universidad se esta desarrollando un software para la 
asignacion de aulas para las materias en los edificios de la 
Universidad. Un aula se define con 2 cosas:
-  Nombre de la Materia
-  Cantidad de Alumnos


"""

class Materia:
  def __init__(self, nombre, cantAlum):
    self._nombre = nombre
    self._cantAlum = cantAlum
    self._cantVentanas = 28

  def cantAlum(self):
    return self._cantAlum

  def __repr__(self):
    return self._nombre +" " + self._cantAlum.__repr__()

class Edificio:

  def asignarMateria2(self, nombreM, cantAlum):
    f = 0
    encontre = False
    while f < len(self._estruc) and not encontre:
      c = 0
      while c < len(self._estruc[0]) and not encontre:
        print(self._estruc[f][c], f, c)
        if self._estruc[f][c] == None:
          self._estruc[f][c] = Materia(nombreM, cantAlum) # mate
          encontre = True
        f = f + 1
        c = c + 1
      if encontre:
          return (f,c)
      else:
          raise Exception("Edificio lleno")

  # asumimos cantAulasxPiso > 0
  def __init__(self, nombreE, cantAulasxPiso):
    self._nombre = nombreE
    self._estruc = np.zeros(( 3, cantAulasxPiso),Materia)

# asumimos que la matriz no esta vacia
  def asignarMateria(self, nombreM, cantAlum):
    for f in range(len(self._estruc)):
      for c in range(len(self._estruc[0])):
        if self._estruc[f][c] == 0:
          self._estruc[f][c] = Materia(nombreM, cantAlum) # mate
          return (f,c) # <---
    raise Exception("Edificio lleno")

  def vaciar(self):
    for f in range(len(self._estruc)):
      for c in range(len(self._estruc[0])):
        self._estruc[f][c] = 0

    # self._estruc = np.zeros(( 3, len(self._estruc[0]),Materia)


  def cantAlumPiso(self, piso):
    total = 0
    for c in range(len(self._estruc[piso])):
      if self._estruc[piso][c] != 0:
        mate = self._estruc[piso][c]
        total = total + mate.cantAlum()
    return total

  def __repr__(self):
    return self._nombre + " " + self._estruc.__repr__()



malvinas = Edificio("Mavinas", 2)

malvinas.asignarMateria("ED com1",44)
malvinas.asignarMateria("ED com2",4)
malvinas.asignarMateria("ED com3",23)
malvinas.asignarMateria("ED com4",45)
malvinas.asignarMateria("ED com5",485)
malvinas.asignarMateria("ED com6",485)
# malvinas.asignarMateria("ED com6",485)

print(malvinas.cantAlumPiso(1))
print(malvinas)
malvinas.vaciar()
print(malvinas)
