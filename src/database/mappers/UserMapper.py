from src.database.mappers.Mapper import Mapper
from src.database.DatabaseHelper import DatabaseHelper


class UserMapper(Mapper):

    def __init__(self, university_id: str):
        self.university_id = university_id
        self.db_helper = DatabaseHelper.getInstance()

    def load(self):
        loaded_data = self.db_helper.load_user()
