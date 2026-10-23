from uuid import uuid4


def generate_random_task():
    return f"Test task {uuid4().hex[:8]}"
