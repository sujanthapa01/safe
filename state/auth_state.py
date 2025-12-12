class user_state:
    _user = None   # global shared variable

    @classmethod
    def set_user(cls, user_info: dict):
        cls._user = user_info

    @classmethod
    def clear_user(cls):
        cls._user = None

    @classmethod
    def get_user(cls) -> dict | None:
        return cls._user
