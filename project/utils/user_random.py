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

    @staticmethod
    def generate_invalid_email():
        return f"user_{uuid.uuid4().hex[:8]}"  # No @ or domain

    @staticmethod
    def generate_email_without_domain():
        return f"user_{uuid.uuid4().hex[:8]}@"

    @staticmethod
    def generate_email_without_domain_extension():
        return f"user_{uuid.uuid4().hex[:8]}@example"

    @staticmethod
    def generate_too_short_password():
        return ''.join(random.choices(string.ascii_letters, k=5))

    @staticmethod
    def generate_too_long_password():
        return ''.join(random.choices(string.ascii_letters, k=31))

    @staticmethod
    def generate_mismatched_password(password):
        # Same length, but guaranteed to differ
        first_char = "B" if password.startswith("A") else "A"
        return first_char + password[1:]

    @staticmethod
    def generate_too_short_username():
        return ''.join(random.choices(string.ascii_letters, k=3))

    @staticmethod
    def generate_too_long_username():
        return ''.join(random.choices(string.ascii_letters, k=31))
