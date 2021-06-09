from sqlalchemy import Column, Integer, String, Date
from database import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    title = Column(String(40))
    body = Column(String)

    def __repr__(self):
        return '<Note title=%r' % self.title


if __name__ == '__main__':
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import engine
    print('creating database...')
    Base.metadata.create_all(engine)
    note1 = Note(title='hello world')
    note1.body = 'my first note'
    note2 = Note(title='goodbye')
    note2.body = 'my second note'
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add_all([note1, note2])
    session.commit()
