import datetime 
import pickle 
import os.path
from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = 'credentials.json"

TOKEN_FILE = 'token.pickle'

TIMEZONE = "Europe/Berlin"

def get_authenticated_service():

    credentials = None 

    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            credentials = pickle.load(token)

    if not credentials or not credientials.valid:
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes = ['https://www.googleapis.com/auth/calendar']
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(credentials, token)
    return build ("calendar" , "v3" , credentials = credentials, cache_discovery = False)

def create_event(summary, location, start_time_str, end_time_str):
    service = get_authenticated_service()

    event = {
        "summary": summary,
        "location": location,
        "start": {
            "dateTime": start_time,
            "timeZone": TIMEZONE,
        },
        "enf": {
            "dateTime": end_time,
            "timeZone": TIMEZONE,
        },  
    }

    event = service.events().insert(calendarId="primary", body=event, sendNotifications=True).execute()
    print(f"Event created: {event.get('htmlLink')}")
    