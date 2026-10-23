import os
from dotenv import load_dotenv

load_dotenv()

MAX_RETRIES = 3
BASE_URL_NOTES_PRJCT = os.getenv("BASE_URL_NOTES")

URL_NOTES_REGISTER = f"{BASE_URL_NOTES_PRJCT}register"
URL_NOTES_LOGIN = f"{BASE_URL_NOTES_PRJCT}login"

URL_API_BASE = os.environ.get('URL_API_BASE')
