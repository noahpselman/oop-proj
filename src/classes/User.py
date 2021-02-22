class User():

    def __init__(self, univeristy_id: str, full_name: str, email: str) -> None:

        self._full_name: str = full_name
        self._uid: str = univeristy_id
        self._email: str = email

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, new_name: str):
        self._full_name = new_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, new_uid):
        self._uid = new_uid
