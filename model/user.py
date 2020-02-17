from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
Base = declarative_base()

class user(Base):
    __tablename__ = 'USERS'
    car_id = Column(String)
    user_id = Column(String)                                   
    @property
    def serialize(self):
        return {
            'car_id' : self.car_id,
            'user_id' : self.time
        }
