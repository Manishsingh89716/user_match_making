📌 Approach & Assumptions for Marriage Matchmaking App

✅ Approach (How We Built This)

1. Used FastAPI for a fast, scalable backend.
2. Implemented CRUD operations to create, read, update, and delete user profiles.
3. Designed a matchmaking system that finds matches based on:
 a) Opposite gender
 b) Same city
4. Used SQLite + SQLAlchemy for easy database management.
5. Added email validation using Pydantic’s EmailStr.
6. Ensured proper error handling (e.g., user not found, email already exists).


✅ Assumptions (What We Considered)

1. Matchmaking is based only on gender and city (not interests or age).
2. Each user has a unique email to prevent duplicate accounts.
3. Users can update their details partially (optional fields in PUT /users/{id}).
4. A user can be deleted permanently (no soft delete).
5. The app is a backend only (no frontend, only API).

📌 7. How to Run?

✅ Step 1: Clone the repository
1. git clone https://github.com/Manishsingh89716/user_match_making

✅ Step 2: Install Dependencies
2. pip install -r requirements.txt

✅ Step 3: Run FastAPI Server
3. cd User_Matchmaking_App
4. uvicorn main:app --reload
