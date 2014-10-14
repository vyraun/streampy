import input_model
from flask import Flask, request
from flask.ext.restful import reqparse, abort, Resource, Api

app = Flask(__name__)
api = Api(app)

experiments = [input_model.initTheta()]

class Action(Resource):
    def get(self, exp_id):
        global experiments
        # Context is still empty, we do not do anything with it yet
        # The information that you initially receive is an exp_id and a context
        # Both should be stored in a database, but for now we use a list
        context = request.json
        theta = experiments[exp_id-1]
        output = input_model.decision(context, theta)
        # Here we can do something with the output
        # Save it in the database or whatnot
        return {'output': output}
    
class Reward(Resource):  
    def put(self, exp_id, reward, action):
        global experiments
        # Here as well, context is still empty
        context = request.json
        theta = experiments[exp_id-1]
        # Just put the reward, action and theta in input_model
        # Return a 200
        reward = input_model.learn(reward, action, theta)
        print reward
        return 200

api.add_resource(Action, '/<int:exp_id>/')
api.add_resource(Reward, '/<int:exp_id>/<string:reward>/<string:action>')

if __name__ == '__main__':
    app.run(debug=True)