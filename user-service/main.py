from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import get_db, User
from .auth import verify_token

app = FastAPI()

@app.get("/")
def get_users(db: Session = Depends(get_db), token_data: dict = Depends(verify_token)):
    users = db.query(User).all()
    return {"current_user": token_data.get("preferred_username"), "data": users}

@app.post("/seed")
def seed_user(db: Session = Depends(get_db)):
    new_user = User(username="admin", email="admin@enterprise.com")
    db.add(new_user)
    db.commit()
    return {"message": "User created"}
