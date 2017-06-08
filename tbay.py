from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    
    #relationship
    seller_id = Column(Integer, ForeignKey('users.id'),nullable=False)
    bids = relationship("Bid", backref="item")
    
    def __str__ (self):
        return "Name: " + self.name + " ("+self.description + ")"
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    #relationship
    auctions = relationship("Item", backref="Seller")
    bids = relationship("Bid", backref="Buyer")
    
    def __str__ (self):
        return "User: " + self.username + " ("+self.password + ")"
  
class Bid(Base):
    __tablename__ = "bid"

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)

    #relationship
    buyer_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    
def reset_db():
  Base.metadata.drop_all(engine)
  Base.metadata.create_all(engine)

def main():
    
    reset_db()
   
  # Add three 
    john = User()
    john.id = 1
    john.username = "john"
    john.password = "johnd"
    session.add(john)
    session.commit()

    angela = User()
    angela.id = 2
    angela.username = "angela"
    angela.password = "angelam"
    session.add(angela)
    session.commit() 
    
    peter = User()
    peter.id = 3
    peter.username = "peter"
    peter.password = "peter123"
    session.add(peter)
    session.commit()
  
  # Make one user auction a baseball
    baseball = Item()
    baseball.id = 1
    baseball.name = "Baseball"
    baseball.description = "white baseball from superseries"
    baseball.Seller = peter
    session.add(baseball)
    session.commit()
    
    # Each user places two bid on the ball (only two users and three bids)
    john_bid1 = Bid()
    john_bid1.id = 1
    john_bid1.price = 1001
    john_bid1.Buyer = john
    john_bid1.Item = baseball
    session.add(john_bid1)
    session.commit()
    
    john_bid2 = Bid()
    john_bid2.id = 2
    john_bid2.price = 1004
    john_bid2.Buyer = john
    john_bid2.Item = baseball
    session.add(john_bid2)
    session.commit()
    
    peter_bid1 = Bid()
    peter_bid1.id = 3
    peter_bid1.price = 900
    peter_bid1.Buyer = john
    peter_bid1.Item = baseball
    session.add(peter_bid1)
    session.commit()
 
    # Perform a query to find out which user placed the highest bid
    row = session.query(User.username, Item.name).join(Bid, Item).filter(Item.name == "Baseball").order_by(Bid.price).all()
    highest_bidder = row[-1].username
    print ("{} had the highest bid for the {}".format(highest_bidder, row[-1].name))

if __name__ == "__main__":
  main()


  