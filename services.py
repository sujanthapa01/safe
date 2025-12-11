from config import auth 

def user_credientials_input() -> tuple[str, str]:
    """Prompt the user for email and password input."""
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    return email, password


def create_user_service() -> any:
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
        print("**login successful**")
        print(user)
        return user
    except Exception as e:
        print(f"error logging in user {e}")
    return None



    """Log out the user associated with the given token."""
    # Pyrebase does not have a built-in logout function.
    # Logout can be handled client-side by deleting the token.
    pass  