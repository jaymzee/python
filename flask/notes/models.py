from database import Base
from sqlalchemy import Column, Integer, String, Date

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    title = Column(String(40), nullable=False, default='')
    body = Column(String, nullable=False, default='')

    def __repr__(self):
        return '<Note title=%r>' % self.title


if __name__ == '__main__':
    from database import engine, SessionLocal
    print('creating database...')
    Base.metadata.create_all(engine)
    note1 = Note(title='hello world')
    note1.body = 'my first note'
    note2 = Note(title='goodbye')
    note2.body = 'my second note'
    session = SessionLocal()
    session.add_all([note1, note2])
    session.commit()
