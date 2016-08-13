from numpy.random import randint, choice
import matplotlib.pyplot as plt

def contar(lista, number):
    count=0
    for x in lista:
        if number==x:
            count+=1
    return count

unidades=[1]*1000 #Force of Units
gamma=0.01 #Define the probability
booleans=[True, False]
for x in xrange(10000): #Time
    top=max(unidades)
    for y in xrange(1, top+1):
        repeticiones=contar(unidades,y)
        if repeticiones!=0:
            plt.loglog(repeticiones, y, "ro")
    suma=sum(unidades)
    probability=[1.*y/suma for y in unidades]
    selection=choice(unidades,1,p= probability)[0]
    boolean=choice(booleans, 1, p=[gamma, 1-gamma])[0]
    if len(unidades)>1:
        unidades.remove(selection)
    if (boolean):
        unidades+=[1]*selection
    elif ((not boolean) and selection!=100):
        probability2=[1.*y/(suma-selection) for y in unidades]
        selection2=choice(unidades, 1, p=probability2)[0]
        unidades.remove(selection2)
        unidades+=[selection+selection2]
    else:
        "WTF?"
        
plt.show()
