import os

#__author__ = 'scdsh'

URL = os.environ.get('MAILGUN_URL')
API_KEY = os.environ.get('MAILGUN_API_KEY')
FROM = os.environ.get('MAILGUN_FROM')

#URL = 'https://api.mailgun.net/v3/sandbox07db88b4f4ae4480a3b3c3929a8f340e.mailgun.org'
#API_KEY = 'key-2fa0b97620b1d83603639d9d64cf5a06'
#FROM = 'postmaster@sandbox07db88b4f4ae4480a3b3c3929a8f340e.mailgun.org'
ALERT_TIMEOUT=1
COLLECTION='alerts'
