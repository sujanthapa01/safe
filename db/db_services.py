from config import db
from state.auth_state import user_state

state = user_state()

def create_profile(data) -> dict:

    user = state.get_user()
    
    uid = user["localId"]

    db.child("profile").child(uid).data(data)
    
    return {"message": "Profile created"}



