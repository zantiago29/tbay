from tbay import User, Item, Bid, session
from datetime import datetime

john = User()
john.id = 1
john.username = "johnd"
john.password = "johnd"
session.add(john)
session.commit()

angela = User()
angela.id = 2
angela.username = "angelam"
angela.password = "angelam"
session.add(angela)
session.commit()

car = Item()
car.id = 1
car.name = "honda"
car.description = "2005 japanese car in blue"
session.add(car)
session.commit()

bike = Item()
bike.id = 2
bike.name = "gt"
bike.description = "2012 black bicycle"
session.add(bike)
session.commit()

