from database import Base
from sqlalchemy import Column, Integer, String, Date

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    title = Column(String(40), unique=True)
    body = Column(String )

    def __repr__(self):
        return '<Note title=%r>' % self.title


if __name__ == '__main__':
    from database import engine
    print('creating database...')
    Base.metadata.create_all(engine)
