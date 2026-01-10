from threading import Thread
from Compte import *

a = Compte(450, 0)


listT = []

for i in range(10):
    t1 = Thread( target=a.ajout , args =(42,) )
    t2 = Thread( target =a.retrait ,args=(42,))
    t1.start()
    t2.start()
    listT.append(t1)
    listT.append(t2)

for t in listT:
    t.join()
