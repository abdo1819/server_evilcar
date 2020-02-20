from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
Base = declarative_base()

class User(Base):
    __tablename__ = 'USER_CAR'
    id = Column(Integer,primary_key=True,
                unique=True,
                autoincrement=True)
    car_id = Column(String)
    user_id = Column(String)                                   
    @property
    def serialize(self):
        return {
            'car_id' : self.car_id,
            'user_id' : self.time
        }
