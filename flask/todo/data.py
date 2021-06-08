import sqlalchemy
import sqlalchemy.orm
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.exc import SQLAlchemyError

engine = sqlalchemy.create_engine('sqlite:///todo.db', echo=True)
Session = sqlalchemy.orm.sessionmaker(bind=engine)
Base = sqlalchemy.orm.declarative_base()

class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    description = Column(String, unique=True)
    completed = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return "<Task(description='%s', completed=%s)>" % (
                self.description, self.completed)

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'completed': self.completed
        }


if __name__ == '__main__':
    Base.metadata.create_all(engine)
