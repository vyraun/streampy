import input_model
import futures
#import numpy as np

experiments = []

class PoC(object):   
    def newExperiment(self):
        global experiments
        # Add a new experiment to the end of the list
        # The experimentID is the indexnumber of the experiment
        experiments.append(input_model.initN())
        return len(experiments)-1 # or context, this can be extended
        
    def getAction(self, context):
        global experiments
        N = experiments[context]
        output = input_model.decision(context, N)
        # Do something with output, if necessary
        return output
        
    def setReward(self, reward, action, context):
        global experiments
        N = experiments[context]
        print N
        output_learn = input_model.learn(reward, action, N)