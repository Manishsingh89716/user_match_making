from sqlalchemy.orm import Session
from models import User

# check for matchmaking based on opposite gender and city
def find_potential_matches(db: Session, user: User):
    matches = db.query(User).filter(
        User.id != user.id,
        User.gender != user.gender,
        User.city == user.city
    ).all()
    return matches