from getpass import getpass
import sys

from webapp import create_app
from webapp.model import User, db

app = create_app()
