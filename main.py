from auth.auth_services import create_user_service, login_user_service, logout_user_service
import inquirer
from state.auth_state import user_state

state = user_state()

while True:
    user = state.get_user()

    if user:
        choices = ["logout_user"]
    else:
        choices = ["register_user", "login_user"]

    questions = [
        inquirer.List(
            "action",
            choices=choices,
            message="Select an action:"
        )
    ]

    answer = inquirer.prompt(questions)
    action = answer["action"]

    action_map = {
        "register_user": create_user_service,
        "login_user": login_user_service,
        "logout_user": logout_user_service,
    }

    action_map[action]()  
