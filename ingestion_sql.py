from random import choice, randint
from faker import Faker
from controller.controller import TeacherController, ClientController, ParticipantController, CourseController

class GenerateData:
    """ Generate random data
    """
    def __init__(self, length) -> None:
        self.length = length

    def generate_data(self):
        """ able to generate random data for database
        """
        fake = Faker()

        # provide random data to "teacher" table
        tax: int = 0
        for count in range(self.length):
            teach = TeacherController().model
            lang = ['portuguese','english','spanish','french','arabic','russian','german','japanese','chinese']

            first_name = fake.first_name()
            last_name = fake.last_name()
            language1 = fake.lexify(text=choice(lang))
            language2 = fake.lexify(text=choice(lang))
            dob = fake.date_time()
            tax += 1+randint(1,100)
            phone_no = fake.phone_number()

            teach.insert_data(first_name, last_name, language1, language2, dob, tax, phone_no)
        print(f'Registers inserted into the "Teacher" table in the database: {count+1}')

        # able to generate random data for the "client" table
        for count in range(self.length):
            client = ClientController().model
            name = fake.name()
            address = fake.address()
            industry = fake.company()
            client.insert_data(name, address, industry)
        print(f'Registers inserted into the "Client" table in the database: {count+1}')


        # provide data for participant table into the database
        for count in range(self.length):
            participant = ParticipantController().model

            name = fake.first_name()
            surname = fake.last_name()
            phone_no = fake.phone_number()
            client_id = randint(1,self.length)
            participant.insert_data(name,surname,phone_no,client_id)
        print(f'Registers inserted into the "Participant" table in the database: {count+1}')

        # provide data for the course table into of the database
        for count in range(self.length):
            course = CourseController().model

            course_name = fake.lexify(text=choice(['course1','course2','course3','course4','course5']))
            language = fake.lexify(text=choice(['portuguese','english','spanish','french','arabic','russian','german','japanese','chinese']))
            level = fake.lexify(text=choice(['A1','A2','B1','B2','C1','C2']))
            course_length = randint(12, 96)
            start_date = fake.date_time()
            client_id = randint(1,self.length)
            teacher_id = randint(1,self.length)
            course.insert_data(course_name,language,level,course_length,start_date, client_id, teacher_id)
        print(f'Registers inserted into the "Course" table in the database: {count+1}')
