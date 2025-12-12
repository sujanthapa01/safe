from config import auth 
from state.auth_state import user_state
from colorama import init, Fore, Style

init()

def user_credientials_input() -> tuple[str, str]:
    """Prompt the user for email and password input.""" 
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    return email, password


def create_user_service() -> dict | None:
    """Create a new user with the given email and password."""
    try:
      email, password = user_credientials_input()
      user = auth.create_user_with_email_and_password(email, password)
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