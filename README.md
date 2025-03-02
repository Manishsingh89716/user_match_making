📌 Approach & Assumptions for Marriage Matchmaking App

✅ Approach (How We Built This)

Used FastAPI for a fast, scalable backend.
Implemented CRUD operations to create, read, update, and delete user profiles.
Designed a matchmaking system that finds matches based on:
Opposite gender
Same city
Used SQLite + SQLAlchemy for easy database management.
Added email validation using Pydantic’s EmailStr.
Ensured proper error handling (e.g., user not found, email already exists).


✅ Assumptions (What We Considered)

Matchmaking is based only on gender and city (not interests or age).
Each user has a unique email to prevent duplicate accounts.
Users can update their details partially (optional fields in PUT /users/{id}).
A user can be deleted permanently (no soft delete).
The app is a backend only (no frontend, only API).
