from databse import Base
from sqlalchemy import Column, Integer, String, Boolean

class ToDos(Base):
    # table name in db
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    desc = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)

