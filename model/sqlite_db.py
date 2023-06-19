import sqlite3
from interface.database_interface import DatabaseInterface

class SQLiteDatabase(DatabaseInterface):
    """ class of the SQLite modeling
    """
    def __init__(self) -> None:
        self.__connection = sqlite3.connect('./data/ils.db')
        self.__cursor = self.__connection.cursor()
        self.__create_table()

    def __create_table(self) -> None:
        """ creation table method from database
            
        """
        teacher_tb = """
            CREATE TABLE IF NOT EXISTS teacher (
                teacher_id  INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name  VARCHAR(40) NOT NULL,
                last_name   VARCHAR(40) NOT NULL,
                language_1  VARCHAR(3),
                language_2  VARCHAR(3),
                dob         DATE,
                tax_id      INTEGER,
                phone_no    VARCHAR(20)
            );
        """

        client_tb = """
            CREATE TABLE IF NOT EXISTS client (
                client_id   INTEGER PRIMARY KEY AUTOINCREMENT,
                client_name VARCHAR(40) NOT NULL,
                address     VARCHAR(60),
                industry    VARCHAR(20)
            );
        """

        participant_tb = """
            CREATE TABLE IF NOT EXISTS participant (
                participant_id  INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name      VARCHAR(40),
                last_name       VARCHAR(40),
                phone_no        VARCHAR(20),
                client_id       INTEGER,
                FOREIGN KEY(client_id) REFERENCES client(client_id)
            )
        """

        course_tb = """
            CREATE TABLE IF NOT EXISTS course (
                course_id           INTEGER PRIMARY KEY AUTOINCREMENT,
                course_name         VARCHAR(40),
                language            VARCHAR(3),
                level               VARCHAR(2),
                course_length_weeks INTEGER,
                start_date          DATE,
                client_id           INTEGER,
                teacher_id          INTEGER,    
                FOREIGN KEY(teacher_id) REFERENCES teacher(teacher_id),
                FOREIGN KEY(client_id) REFERENCES client(client_id)
            )
        """

        self.__cursor.execute(teacher_tb)
        self.__cursor.execute(client_tb)
        self.__cursor.execute(participant_tb)
        self.__cursor.execute(course_tb)
        self.__connection.commit()

    def get_connect(self) -> object:
        """ implementing of the interface method for connection 
            with database and return a cursor
        """
        return self.__cursor

    def close_connection(self) -> None:
        """ save changes on dataabse and close the connection
        """
        self.__connection.commit()
        self.__connection.close()
    