import poc
import random as rnd
import futures
#import numpy as np

poc = poc.PoC()
with futures.ThreadPoolExecutor(1) as executor:
    cont = executor.submit(poc.newExperiment)
    context = cont.result()  # see "ExpID"
    print context

    for i in xrange(10000):
        act = executor.submit(poc.getAction, context)  ## will be http://blabla.com/expID/getAction?context={JSON} (of POST)
        #futures.wait(act)
        action = act.result()
        
        if(action == "A"):
            executor.submit(poc.setReward(round(rnd.random()), action, context))
        else:
            executor.submit(poc.setReward(round(rnd.random()), action, context))
			## Nadenken: hoe koppelen we actie en reward? (ActionID)
				# Maar, hoe "online" / schaalbaar.
				# Kijk ook naar Redis (database systeem)
				# Think about possible errors / synchronise issue


# Comments (01-10-2014):
# This will run outside of "our" system (simulates API calls)
	# So, we need to move this to a REST API framework.
	# Check Flask
	
# Admin / aanmaken van experiment gescheiden van uitvoer ervan.
	# Laten we ervan uit gaan dat er een "admin" is waarin je experimenten aanmaakt. Dit geeft een expID.
		# (gaan we misschien nog maken, maar niet hoogste prio)
		# Dit maakt een data base entry aan voor het experiment, waarin de ID staat, en Theta (nu, N), en het "input model (leer en decision)"
