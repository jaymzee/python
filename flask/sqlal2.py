import sqlalchemy

from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

from sqlalchemy import Column, Integer, String, ForeignKey

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    password = Column(String)

    def __repr__(self):
        return f"<User(name={self.name})>"


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User, backref='products')

    def __repr__(self):
        return f"<Product(name={self.name})>"


from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name='John', password='1234')
user2 = User(name='Frodo', password='sam')
session.add(user1)
session.add(user2)

product1 = Product(name='potato', user=user1)
product2 = Product(name='apple', user=user1)

session.add(product1)
session.add(product2)

session.commit()

