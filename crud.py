from sqlalchemy.orm import Session
from sqlalchemy import and_, func
from datetime import date
from fastapi import HTTPException
from .models import Hotel, Room, Booking
from .schemas import HotelCreate

def create_hotel(db: Session, hotel: HotelCreate):
    new_hotel = Hotel(
        name=hotel.name,
        location=hotel.location
    )

    db.add(new_hotel)
    db.commit()
    db.refresh(new_hotel)

    return new_hotel

def get_hotels(db: Session):
    return db.query(Hotel).all()

def create_room(db: Session, room):
    new_room = Room(
        room_number=room.room_number,
        room_type=room.room_type,
        price=room.price,
        hotel_id=room.hotel_id
    )

    db.add(new_room)
    db.commit()
    db.refresh(new_room)

    return new_room


def get_rooms(db: Session):
    return db.query(Room).all()

def create_booking(db: Session, booking):
    room = (db.query(Room).filter(Room.id == booking.room_id).with_for_update().first())
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    existing_booking = db.query(Booking).filter(
        Booking.room_id == booking.room_id,
        Booking.check_in < booking.check_out,
        Booking.check_out > booking.check_in
    ).first()

    if existing_booking:
        raise HTTPException(
            status_code=400,
            detail="Room is already booked for these dates"
        )
    days = (booking.check_out - booking.check_in).days

    if days <= 0:
        raise HTTPException(
        status_code=400,
        detail="Check-out date must be after check-in date"
        )

    total_price = room.price * days

    db_booking = Booking(
        booking_reference="",                                                             
        customer_name=booking.customer_name,
        check_in=booking.check_in,
        check_out=booking.check_out,
        room_id=booking.room_id,
        total_price=total_price
    )
    
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)

    db_booking.booking_reference = f"BK-{db_booking.id:06d}"
    db.commit()
    db.refresh(db_booking)


    return db_booking

def cancel_booking(db: Session, booking_id: int):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    db.delete(booking)
    db.commit()

    return {"message": "Booking cancelled successfully"}

def get_available_rooms(db: Session, check_in, check_out):
    booked_room_ids = (
        db.query(Booking.room_id)
        .filter(
            and_(
                Booking.check_in < check_out,
                Booking.check_out > check_in
            )
        )
        .subquery()
    )

    available_rooms = (
        db.query(Room)
        .filter(~Room.id.in_(booked_room_ids))
        .all()
    )

    return available_rooms

def get_bookings(db: Session):
    return db.query(Booking).all()

def get_admin_metrics(db: Session):
    total_rooms = db.query(Room).count()

    currently_occupied = (
        db.query(Booking)
        .filter(
            Booking.check_in <= date.today(),
            Booking.check_out > date.today()
        )
        .count()
    )

    revenue_this_month = (
        db.query(func.sum(Booking.total_price))
        .filter(
            func.month(Booking.check_in) == date.today().month,
            func.year(Booking.check_in) == date.today().year
        )
        .scalar()
    )

    if revenue_this_month is None:
        revenue_this_month = 0

    return {
        "total_rooms": total_rooms,
        "currently_occupied": currently_occupied,
        "revenue_this_month": revenue_this_month
    }
