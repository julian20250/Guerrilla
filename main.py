from numpy.random import randint, choice
import matplotlib
import matplotlib.style
matplotlib.style.use('classic')
import matplotlib.pyplot as plt
import sys

def contar(lista, number):
    count=0
    for x in lista:
        if number==x:
            count+=1
    return count


total=10000 #Total Units
unidades=[1]*total #Creating (total) units with force 1
gamma=0.01 #Define the probability
booleans=[True, False]
time = input("Digit time > ") #Time
print("When you wish to stop, use ctrl-c; all changes are saved.")
for x in range(int(time)): 
    sys.stdout.write("\r{0}".format("Passed %i of %s time units"%(x+1,time)))
    sys.stdout.flush()
    suma=sum(unidades)
    probability=[1.*y/suma for y in unidades]
    selection=choice(unidades,1,p= probability)[0]
    boolean=choice(booleans, 1, p=[gamma, 1-gamma])[0]
    if len(unidades)>1:
        unidades.remove(selection)
    if (boolean):
        unidades+=[1]*selection
    elif ((not boolean) and selection!=total):
        probability2=[1.*y/(suma-selection) for y in unidades]
        selection2=choice(unidades, 1, p=probability2)[0]
        unidades.remove(selection2)
        unidades+=[selection+selection2]

for x in range(1, max(unidades)+1):
    repeticiones=contar(unidades,x)
    if repeticiones!=0:
        plt.loglog(repeticiones,x,"ro")
plt.show()
