###configuration###
import sys
from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship
 
from sqlalchemy import create_engine

#indicate to this is a sepecial sqlalchemy class instance 
#that corrsponds to the tables in our database
Base = declarative_base()


###class###
class Restaurant(Base):
    ####table: to show to sqlalchimy that this refer to the table
    __tablename__ = 'restaurant'

    ###mapper code:to maps python objects to columns in our database#
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)

class MenuItem(Base):
    ###table: to show to sqlalchimy that this refer to the table
    __tablename__ = 'menu_item'
    ###mapper code#
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    #indicate the relationship between this class and the Restaurant class#
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        #returns object data in easily serializealbe format
        return {
            'name' : self.name,
            'description' : self.description,
            'id' : self.id,
            'price': self.price,
            'course' : self.course,
        }


###configuration###
engine = create_engine('sqlite:///restaurantmenu.db')
#go to te database and add the table we create
Base.metadata.create_all(engine)

    
