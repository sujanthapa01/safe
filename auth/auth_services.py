from config import auth 
from state.auth_state import user_state
from colorama import init, Fore, Style
from db.db_services import create_profile
import time
from main import action
from config import db
init()


def is_username_taken(username: str) -> bool:
    result = db.child("profiles").child(username).get()
    return result.val() is not None

def user_credientials_input(action: str):
    """Prompt the user for credentials safely"""

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if action == "register_user":
        while True:
            username = input("Make a username: ").lower().strip()

            if is_username_taken(username):
                print(f"'@{username}' already exists. Try again.")
            else:
                break

        return {
            "email": email,
            "password": password,
            "username": username
        }

    return {
        "email": email,
        "password": password
    }


def create_user_service(username) -> dict | None:
    """Create a new user with the given email and password."""
    created_at = int(time.time())
    try:
      email, password = user_credientials_input()
      user = auth.create_user_with_email_and_password(email, password)
      uid = user["localId"]
      create_profile(uid,{ 
          "email" : email,
          "username" : username,
          "created_at" : created_at

      })
      return user
    except Exception as e:
        print(f"error creating user {e}")
        return None


def login_user_service() -> any:
    """Log in a user with the given email and password."""
    try: 
        email, password = user_credientials_input()
        user = auth.sign_in_with_email_and_password(email, password)
        user_state().set_user(user)
        print("**login successful**")
        print(user)
        print(Fore.RED + Style.BRIGHT +user["email"] + Style.RESET_ALL)
        return user
    except Exception as e:
        print(f"error logging in user {e}")
    return None



    
def logout_user_service() -> None:
      """Log out the current user."""
      user_state().clear_user()
      print("**logout successful**")    