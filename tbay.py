from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
    def __str__ (self):
        return "Name: " + self.name + " ("+self.description + ")"
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    def __str__ (self):
        return "User: " + self.username + " ("+self.password + ")"
  
class Bid(Base):
    __tablename__ = "bid"

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)  


user = session.query(User).all()
user1 = user[0]
session.delete(user1)
session.commit()

user2 = user[1]
session.delete(user2)
session.commit()

result = session.query(User).all()

for user in result:
    print(user)

Base.metadata.create_all(engine)
  