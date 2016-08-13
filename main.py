from numpy.random import randint

unidades=[1]*100 #Number of Units
gamma=0.01 #Define the probability
for x in xrange(1000): #Time
    top=max(unidades)
    bottom=min(unidades)
    probability=[]
