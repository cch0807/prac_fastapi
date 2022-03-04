import uuid
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Boolean, String, Text, Column
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://{username}:{password}@{host}:{port}/{db_name}'.format(
  username='cch', password='1234', host='127.0.0.1',port='5432', db_name='prac'
))

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.metadata.create_all(bind=engine)

def get_db():
  db = db_session()
  try:
    yield db
  finally:
    db.close()
    
class Memo(Base):
  __tablename__ = 'memos'

  id = Column(String(120), primary_key=True, default=lambda: str(uuid.uuid4()))
  title = Column(String(80), default='No title', nullable=False, index=True)
  content = Column(Text, nullable=True)