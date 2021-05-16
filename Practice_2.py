from __future__ import print_function
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import requests
import ssl



SERVICE_ACCOUNT_FILE = 'practicepython_1.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1c8u_JTDzJseTI7VbqlWic9pLGoDo_gOUHW-6Q9joFPw'

service = build('sheets', 'v4', credentials=creds)

#requests.get('https://www.googleapis.com/auth/spreadsheets', verify=False)

#ssl._create_default_https_context = ssl._create_unverified_context

    # Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="Sheet1!A1:C100").execute()
#values = result.get('values', [])

print(result)
