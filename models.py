from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Date
from .database import Base
from sqlalchemy import Date

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    location = Column(String(100))
from sqlalchemy import Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    room_number = Column(String(20))
    room_type = Column(String(50))
    price = Column(Float)
    is_available = Column(Boolean, default=True)

    hotel_id = Column(Integer, ForeignKey("hotels.id"))    
class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    booking_reference = Column(String(20), unique=True, index=True)   
    customer_name = Column(String(100))
    check_in = Column(Date)
    check_out = Column(Date)
    total_price= Column(Float)
    room_id = Column(Integer, ForeignKey("rooms.id")) 
    