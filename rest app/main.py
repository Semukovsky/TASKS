from flask import Flask, jsonify
from flask_restful import Api
import sys
import logging

from jobs_resources import JobsListResource, JobsResource, JobsResourceDelete, JobsResourcePost

app = Flask(__name__)
api = Api(app)

# http://127.0.0.1:8080/api/users
api.add_resource(JobsListResource, '/api/jobs')
api.add_resource(JobsResource, '/api/jobs/<int:jobs_id>')
api.add_resource(JobsResourceDelete, '/api/jobs/delete')
api.add_resource(JobsResourcePost, '/api/jobs/post')

if __name__ == '__main__':
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)
    app.run(port=8080, host='127.0.0.1')