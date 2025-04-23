from sqlalchemy import orm
import sqlalchemy
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()


class Department(SqlAlchemyBase):
    __tablename__ = 'department'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    title = sqlalchemy.Column(sqlalchemy.String, index=True)
    chief = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    members = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)

    def __repr__(self):
        return f'<Department> {self.title}'
