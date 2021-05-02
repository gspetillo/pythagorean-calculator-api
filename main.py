from flask import Flask, request
from flask_restful import Resource , Api
import math

app = Flask(__name__)
api = Api(app)

class Hypotenuse(Resource):
    def get(self):
        args = request.args
        if('sideA' in args and 'sideB' in args):
            sideA = float(args['sideA'])
            sideB = float(args['sideB'])
            hypotenuse =  math.sqrt( pow(sideA,2) + pow(sideB,2) )
            return {
                'status': 200,
                'data': hypotenuse
            },200
        else:
            return {
                'status': 422,
                'data': 'Invalid parameters'
            },422

class Side(Resource):
    def get(self):
        args = request.args
        if('side' in args and 'hypotenuse' in args):
            side = float(args['side'])
            hypotenuse = float(args['hypotenuse'])
            if(hypotenuse>side):
                side =  math.sqrt(pow(hypotenuse,2) - pow(side,2))
                return {
                    'status': 200,
                    'data': side
                },200
            else:
                return {
                    'status': 200,
                    'data': 'Hypotenuse can\'t be greater than side'
                },200
        else:
            return {
                'status': 422,
                'data': 'Invalid parameters'
            },422
        

class PythagorasCalculator(Resource):
    def get(self):
        return {
            'about':'Welcome to PythagorasCalculator API',
            'description': 'Use routes to return values of hypotenuse or side',
            
            'routes': {
                    '/hypotenuse': [{
                        'methods':[
                            'GET'
                        ],
                        'args':{
                            'sideA':{
                                'type': 'float',
                                'required': True
                            },
                            'sideB':{
                                'type': 'float',
                                'required': True
                            },
                        },
                    }],
                    '/side': [{
                        'methods':[
                            'GET'
                        ],
                        'args':{
                            'side':{
                                'type': 'float',
                                'required': True
                            },
                            'hypotenuse':{
                                'type': 'float',
                                'required': True
                            },
                        }
                    }],
                }
            }

api.add_resource(PythagorasCalculator, '/')
api.add_resource(Hypotenuse, '/hypotenuse')
api.add_resource(Side, '/side')

if __name__ == '__main__':
    app.run(threaded=True, port=5000)