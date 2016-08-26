from numpy.random import randint, choice
import matplotlib
import matplotlib.style
import numpy as np
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
condition= input("Read datos.txt? (y/n) > ")

if condition=="y":
    f=open("datos.txt", "r")
    unidades=f.readlines()
    unidades=[int(x) for x in unidades]

else:
    unidades=[1]*total #Creating (total) units with force 1
    
gamma=0.01 #Define the probability
booleans=[True, False]
time = input("Digit time > ") #Time
if time=="inf":
    time2=3
else:
    time2=time
print("When you wish to stop, use ctrl-c; all changes are saved.")
x=0
counter=0
while (x<int(time2)): 
    try:        
        sys.stdout.write("\r{0}".format("Passed %i of %s time units"%(counter+1,time)))
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
        if time=="inf":
            x-=1
        x+=1
        counter+=1
    except KeyboardInterrupt:
        break
   
if sum(unidades)!=total:
    raise Warning("The ending force doesn't not coincide")
f= open("datos.txt", "w")
for x in unidades:
    f.write(str(x)+"\n")
f.close()
l1=[]
l2=[]
for x in range(1, max(unidades)+1):
    repeticiones=contar(unidades,x)
    if repeticiones!=0:
        plt.loglog(x,repeticiones,"ro")
        l1.append(np.log(x))
        l2.append(np.log(repeticiones))
z=np.polyfit(l1,l2,1)
plt.plot([np.e**x for x in l1],[np.e**z[1]*(np.e**x)**z[0] for x in l1])
print("\nThe slope is %f"%z[0])

plt.show()
