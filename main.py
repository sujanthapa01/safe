from services import create_user_service, login_user_service
import inquirer

options = [
    inquirer.List(
        "action",
        choices=["register_user", "login_user"]
    )
]

choosen = inquirer.prompt(options)

action_map ={
"register_user": create_user_service,
"login_user": login_user_service
}

action_map[choosen["action"]]()