from flask import jsonify
from flask_restful import reqparse, abort, Resource
from data import db_session
from data.jobs import Jobs

parser_1 = reqparse.RequestParser()
parser_1.add_argument('team_leader', required=True, type=int)
parser_1.add_argument('job', required=True)
parser_1.add_argument('work_size', required=True, type=int)
parser_1.add_argument('collaborators', required=True)
parser_1.add_argument('start_date', required=True)
parser_1.add_argument('is_finished', required=True, type=bool)

parser_2 = reqparse.RequestParser()
parser_2.add_argument('jobs_id', required=True, type=int)


def abort_if_user_not_found(jobs_id):
    db_session.global_init('db/mars_explorer.db')
    session = db_session.create_session()
    jobs = session.query(Jobs).get(jobs_id)
    if not jobs:
        abort(404, message=f"Jobs {jobs_id} not found")


class JobsResource(Resource):
    def get(self, jobs_id):
        abort_if_user_not_found(jobs_id)
        db_session.global_init('db/mars_explorer.db')
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        return jsonify({'user': jobs.to_dict(
            only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'is_finished')
        )})

class JobsListResource(Resource):
    def get(self):
        db_session.global_init('db/mars_explorer.db')
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [job.to_dict(
            only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'is_finished')
        ) for job in jobs]})

class JobsResourceDelete(Resource):
    def delete(self):
        args = parser_2.parse_args()
        jobs_id = args['jobs_id']
        abort_if_user_not_found(jobs_id)
        db_session.global_init('db/mars_explorer.db')
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsResourcePost(Resource):
    def post(self):
        db_session.global_init('db/mars_explorer.db')
        args = parser_1.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=args['start_date'],
            is_finished=args['is_finished']
        )
        session.add(jobs)
        session.commit()
        return jsonify({'success': 'OK'})