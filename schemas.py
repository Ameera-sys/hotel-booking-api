from pydantic import BaseModel
from datetime import date

class HotelCreate(BaseModel):
    name: str
    location: str
class RoomCreate(BaseModel):
    room_number: str
    room_type: str
    price: float
    hotel_id: int    

class RoomResponse(RoomCreate):
    id: int

    class Config:
        from_attributes = True

class BookingCreate(BaseModel):
    customer_name: str
    check_in: date
    check_out: date
    room_id: int

class BookingResponse(BookingCreate):
    id: int
    booking_reference: str
    total_price: float

    class Config:
        from_attributes = True    