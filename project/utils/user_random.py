import random
import string
import uuid
from datetime import datetime
import faker


class UserRandomUtil:

    @staticmethod
    def generate_letters_only_password():
        return ''.join(random.choices(string.ascii_letters, k=6))

    @staticmethod
    def generate_unique_email():
        timestamp = int(datetime.now().timestamp())
        return f"user_{timestamp}_{uuid.uuid4().hex[:4]}@gmail.com"

    @staticmethod
    def generate_random_first_and_last_name():
        fake = faker.Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        return first_name + " " + last_name
