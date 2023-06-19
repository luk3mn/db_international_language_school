from interface.database_interface import DatabaseInterface

class Teacher:
    """ teacher modeling for the database
    """
    def __init__(self, database: DatabaseInterface) -> None:
        self.__database = database

    def insert_data(self, first_name, last_name, language1, language2, dob, tax_id, phone_no):
        """ inserting data on database
            """
        conn = self.__database.get_connect()
        conn.execute(f'''
                        INSERT INTO teacher (first_name, last_name, language_1, language_2, dob, tax_id, phone_no) 
                        VALUES ('{first_name}','{last_name}','{language1}','{language2}','{dob}',{tax_id},'{phone_no}')
                     ''')
        self.__database.close_connection()

class Client:
    """ client modeling for the database
    """
    def __init__(self, database: DatabaseInterface) -> None:
        self.__database = database

    def insert_data(self, client_name, address, insdustry) -> None:
        """ inserting data on client table
        """
        conn = self.__database.get_connect()
        conn.execute(f'''
            INSERT INTO client (client_name, address, industry) VALUES ('{client_name}', '{address}', '{insdustry}')
        ''')
        self.__database.close_connection()

class Participant:
    """ Participant modeling for the database
    """
    def __init__(self, database: DatabaseInterface) -> None:
        self.__database = database

    def insert_data(self, first_name, last_name, phone_no, client_id) -> None:
        """ inserting modeling data on participant table
        """
        conn = self.__database.get_connect()
        conn.execute(f'''
            INSERT INTO participant (first_name, last_name, phone_no, client_id) VALUES ('{first_name}','{last_name}','{phone_no}',{client_id})
        ''')
        self.__database.close_connection()

class Course:
    """ Course modeling for the database
    """
    def __init__(self, database: DatabaseInterface) -> None:
        self.__database = database

    def insert_data(self, course, language, level, course_length, start_date, client_id, teacher_id) -> None:
        """ inserting data into the database on course table
        """
        conn = self.__database.get_connect()
        conn.execute(f'''
                        INSERT INTO course (course_name, language, level, course_length_weeks, start_date, client_id, teacher_id) 
                        VALUES ('{course}','{language}','{level}',{course_length},'{start_date}',{client_id},{teacher_id})
                     ''')
        self.__database.close_connection()
