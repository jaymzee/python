import sqlalchemy

from sqlalchemy.orm import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)


from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name='John', fullname='John Snow', nickname='snowflake')
user2 = User(name='Frodo', fullname='Frodo Baggins', nickname='frofro')
session.add(user1)
session.add(user2)
session.commit()
print(user1)
print(user1.id)
print(user2)
print(user2.id)

query = session.query(User).filter_by(name='John')
count = query.count()
print(count)
query = session.query(User).filter(User.name.like('%ohn'))
count = query.count()
print(count)

