# Install dependencies
#pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2

from datetime import datetime, timedelta
import os.path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_calendar_service():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    return service

def get_today_events(service):
    now = datetime.utcnow()
    start_of_day = now.replace(hour=0, minute=0, second=0)
    end_of_day = start_of_day + timedelta(days=1)

    events_result = service.events().list(
        calendarId='primary',
        timeMin=start_of_day.isoformat() + 'Z',
        timeMax=end_of_day.isoformat() + 'Z',
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    return events_result.get('items', [])

def display_events(events):
    if not events:
        print("No events today 🎉")
        return

    print("\nToday's Events:\n")

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        start_time = datetime.fromisoformat(start.replace('Z', ''))

        time_str = start_time.strftime('%H:%M')
        title = event.get('summary', '(No title)')

        print(f"{time_str} – {title}")

if __name__ == "__main__":
    service = get_calendar_service()
    events = get_today_events(service)
    display_events(events)
