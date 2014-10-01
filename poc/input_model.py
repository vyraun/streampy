# This input model is the A/B test. Generic module/"skeleton"
import random

# hoe maken we dit "plug & play"

def decision(context, N):

    if N['n'] < N['N']:
        # random A or B
        X = random.sample(xrange(2),1)
        if X == [1]:
            return 'A'
        else:
            return 'B'
    elif (N['Sa']/N['Na']) > (N['Sb']/N['Nb']):
        #max of A := (N['Sa']/N['Na']) and B := (N['Sb']/N['Nb])
        return 'A'
    else:
        return 'B'

def learn(reward, action, N):

    if action == 'A':
        N['Na'] += 1
        N['Sa'] = N['Sa'] + reward
    else:
        N['Nb'] += 1
        N['Sb'] = N['Sb'] + reward
    N['n'] += 1
    
    return N


# For the admin / backend:
# def getStats(expID):
	# return N

def initN():
    return { 'n' : 0, 'Sa' : 0 , 'Na' : 0, 'Sb' : 0, 'Nb' : 0, 'N' : 10000 }