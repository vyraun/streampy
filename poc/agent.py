import poc
import random as rnd
import futures
#import numpy as np

poc = poc.PoC()
with futures.ThreadPoolExecutor(1) as executor:
    cont = executor.submit(poc.newExperiment)
    context = cont.result()
    print context

    for i in xrange(10000):
        act = executor.submit(poc.getAction, context)
        #futures.wait(act)
        action = act.result()
        
        if(action == "A"):
            executor.submit(poc.setReward(round(rnd.random()), action, context))
        else:
            executor.submit(poc.setReward(round(rnd.random()), action, context))