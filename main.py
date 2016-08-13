import unidad
from numpy.random import randint

unidad=unidad.unidad
unidades=[]
for x in xrange(100):
    unidades.append(unidad(randint(1, 11)))
print [x.fuerza for x in unidades]
