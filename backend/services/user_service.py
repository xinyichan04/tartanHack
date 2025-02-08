from models import db, User

def get_user_preferences():
    user = User.query.first()
    return user.preferences if user else {}

def update_user_preferences(preferences):
    user = User.query.first()
    if user:
        user.preferences = preferences
        db.session.commit()
