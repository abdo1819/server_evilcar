import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Violation(Base):
    __tablename__ = 'violation'

    id = Column(Integer, primary_key=True)
    car_id = Column(Integer)
    longitude = Column(Float)
    latitude = Column(Float)
    speed = Column(Float)
    time = Column(DateTime)
    
    @property
    def serialize(self):

        return {
            'car_id' : self.car_id,
            'longitude' : self.longitude,
            'latitude' : self.latitude,
            'speed' : self.speed,
            'time' : self.time
        }


engine = create_engine('sqlite:///violations.db')


Base.metadata.create_all(engine)
