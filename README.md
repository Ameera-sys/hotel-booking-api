# Real-Time Hotel Booking & Inventory API

## Overview

The Real-Time Hotel Booking & Inventory API is a backend application built using FastAPI and MySQL. It enables hotel management, room management, booking creation, room availability checking, booking cancellation, and an admin dashboard for monitoring hotel metrics.

The project is containerized using Docker, making it easy to set up and run in any environment.

---

## Features

* Hotel Management

  * Create Hotel
  * View Hotels

* Room Management

  * Add Rooms
  * View Rooms

* Booking Management

  * Create Booking
  * Generate Unique Booking Reference
  * Automatic Total Price Calculation
  * Cancel Booking

* Availability Management

  * Check Available Rooms for Selected Dates
  * Prevent Double Booking using database transaction locking

* Admin Dashboard

  * Total Rooms
  * Currently Occupied Rooms
  * Monthly Revenue

---

## Tech Stack

* Python 3.11
* FastAPI
* SQLAlchemy ORM
* MySQL
* Docker & Docker Compose
* Pydantic
* Uvicorn

---

## Project Structure

```
hotel-booking-api/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## API Endpoints

### Hotel

* POST /hotels
* GET /hotels

### Rooms

* POST /rooms
* GET /rooms
* GET /rooms/available

### Booking

* POST /bookings
* GET /bookings
* DELETE /bookings/{booking_id}

### Admin

* GET /admin/metrics

---

## How to Run

### Clone the repository

```bash
git clone <repository-url>
cd hotel-booking-api
```

### Start the application

```bash
docker compose up --build
```

### Open Swagger Documentation

```
http://localhost:8000/docs
```

---

## Key Features Implemented

* RESTful API Design
* SQLAlchemy ORM
* MySQL Database Integration
* Dockerized Application
* Room Availability Checking
* Double Booking Prevention
* Booking Reference Generation
* Revenue Calculation
* Admin Dashboard Metrics

---

## Future Improvements

* JWT Authentication
* User Registration & Login
* Hotel Search by Location
* Pagination & Filtering
* Booking History
* Unit Testing
* Cloud Deployment (AWS / Render)

---

## Author

S Ameera Fatima

Computer Science Engineering Student

Backend Developer | Python | FastAPI | SQLAlchemy | MySQL | Docker
