import json
import random as rnd
from requests import put, get

# This is an example to put something with a context
#r = put('http://localhost:5000/1/1/1', data=json.dumps({'context_id' = 'dasdsf'}), headers = {'content-type': 'application/json'})

# Given by admin
exp_id = 1

print("check")

# Headers for putting and getting
header = {'content-type': 'application/json'}

for i in xrange(150):
    #print("in loop")
    # Since we still have an empty context, we will not send a context
    # Get the action, by giving the expID
    #print('http://127.0.0.1:5000/{0}/'.format(exp_id))
    r = get('http://127.0.0.1:5000/{0}/'.format(exp_id))
    action = r.json()['output']
    print(action)
    
    # Since we will not make a difference between action A and B, we do not need an if-else statement.
    reward = round(rnd.random())
    # Put something without context
    r = put('http://127.0.0.1:5000/{0}/{1}/{2}'.format(exp_id, reward, action))

print("done")