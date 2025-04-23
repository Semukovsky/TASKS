from sqlalchemy import orm
import sqlalchemy
from datetime import datetime

import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    job = sqlalchemy.Column(sqlalchemy.String, index=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    user = orm.relationship('User')

    def __repr__(self):
        return f'<Job> {self.job}'
