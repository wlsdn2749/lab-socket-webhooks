from flask import Flask, json
from flask_restful import Resource, Api

import os

buildbranch = 'master'
buildpath = '/workspace/cn/lab-socket-webhooks/'

buildcommend = 'cd ' \
                + buildpath \
                + ' && git stash && git pull origin '\
                + buildbranch

app = Flask(__name__)                
api = Api(app)

class SetDeploy(Resource):
    def post(self):
        os.system(buildcommend)
        return {'status' : 'success'}
    
api.add_resource(SetDeploy, '/deploy')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
