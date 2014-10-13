import input_model
from flask import Flask
from flask.ext.restful import reqparse, abort, Resource, Api

app = Flask(__name__)
api = Api(app)

experiments = []

class StreamPy(Resource):
    def get(self, exp_id, context):
        return context
    
    def setReward(self, exp_id, context, reward, action):
        args = parser.parse_args()
        task 
        return context
    

api.add_resource(StreamPy, '/<int:exp_id>/')

if __name__ == '__main__':
    app.run(debug=True)