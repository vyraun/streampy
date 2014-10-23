# This input model is the A/B test. Generic module/"skeleton"
import random

# hoe maken we dit "plug & play"

def decision(context, theta):

    if theta['n'] < theta['N']:
        # random A or B
        X = random.sample(xrange(2),1)
        if X == [1]:
            return 'A'
        else:
            return 'B'
    elif (theta['Sa']/theta['Na']) > (theta['Sb']/theta['Nb']):
        #max of A := (theta['Sa']/theta['Na']) and B := (theta['Sb']/theta['Nb])
        return 'A'
    else:
        return 'B'




def learn(reward, action, theta):

    reward = int(float(reward))

    if action == 'A':
        theta['Na'] += 1
        theta['Sa'] = theta['Sa'] + reward
    else:
        theta['Nb'] += 1
        theta['Sb'] = theta['Sb'] + reward
    theta['n'] += 1
    
    return theta


# For the admin / backend:
# def getStats(expID):
	# return theta

def initTheta():
    return { 'n' : 0, 'Sa' : 0 , 'Na' : 0, 'Sb' : 0, 'Nb' : 0, 'N' : 10000 }