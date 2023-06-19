from model.sqlite_db import SQLiteDatabase
from model.model import Teacher, Client, Participant, Course

class TeacherController:
    """ controll of the Teacher operations
    """
    def __init__(self) -> None:
        database = SQLiteDatabase()
        self.model = Teacher(database)

class ClientController:
    """ controll of the client operations
    """
    def __init__(self) -> None:
        database = SQLiteDatabase()
        self.model = Client(database)

class ParticipantController:
    """ control of the participant operations
    """
    def __init__(self) -> None:
        database = SQLiteDatabase()
        self.model = Participant(database)

class CourseController:
    """ control of the participant operations
    """
    def __init__(self) -> None:
        database = SQLiteDatabase()
        self.model = Course(database)
