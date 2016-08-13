from numpy.random import randint, choice

unidades=[1]*100 #Force of Units
gamma=0.01 #Define the probability
booleans=[True, False]
for x in xrange(1000): #Time
    top=max(unidades)
    bottom=min(unidades)
    suma=sum(unidades)
    probability=[1.*y/suma for y in unidades]
    selection=choice(unidades,1,p= probability)[0]
    boolean=choice(booleans, 1, p=[gamma, 1-gamma])[0]
    if boolean:        
        unidades.remove(selection)
        
