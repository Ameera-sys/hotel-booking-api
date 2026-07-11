from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .models import Hotel, Room
from .schemas import HotelCreate, RoomCreate
from datetime import date
from .crud import (create_hotel, get_hotels, create_room, get_rooms, get_available_rooms, get_admin_metrics)

from . import crud,schemas, models


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.get("/")
def home():
    return {"message":"Welcome to Hotel Booking API"}

@app.post("/hotels")
def add_hotel(hotel: HotelCreate, db: Session = Depends(get_db)):
    return create_hotel(db, hotel)

@app.get("/hotels")
def read_hotels(db: Session = Depends(get_db)):
    return get_hotels(db)

@app.post("/rooms")
def add_room(room: RoomCreate, db: Session = Depends(get_db)):
    return create_room(db, room)


@app.get("/rooms")
def read_rooms(db: Session = Depends(get_db)):
    return get_rooms(db)

  
@app.post("/bookings", response_model=schemas.BookingResponse)
def add_booking(
    booking: schemas.BookingCreate,
    db: Session = Depends(get_db)
):
    return crud.create_booking(db, booking)

@app.get("/bookings", response_model=list[schemas.BookingResponse])
def read_bookings(db: Session = Depends(get_db)):
    return crud.get_bookings(db)

@app.delete("/bookings/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    return crud.cancel_booking(db, booking_id)

@app.get("/rooms/available", response_model=list[schemas.RoomResponse])
def available_rooms(
    check_in: date,
    check_out: date,
    db: Session = Depends(get_db)
):
    return crud.get_available_rooms(db, check_in, check_out)

@app.get("/admin/metrics")
def admin_metrics(db: Session = Depends(get_db)):
    return get_admin_metrics(db)


