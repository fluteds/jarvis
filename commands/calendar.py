import requests
import icalendar
from datetime import datetime
from config import CALENDAR_URL

def fetch_calendar_events():
    try:
        response = requests.get(CALENDAR_URL)
        if response.status_code == 200:
            return response.text
        else:
            print("Failed to fetch calendar events: Status code", response.status_code)
            return None
    except requests.RequestException as e:
        print("Failed to fetch calendar events:", e)
        return None
    
def get_next_event(calendar_data):
    calendar = icalendar.Calendar.from_ical(calendar_data)
    today = datetime.today().date()
    next_event = None

    for event in calendar.walk('vevent'):
        event_date = event.get('dtstart').dt.date()
        if event_date >= today:
            next_event = (event_date, event.get('dtstart').dt.time(), event.get('dtend').dt.time(), event.get('summary'))
            break
    
    return next_event

    
    events.sort(key=lambda x: x[0])  # Sort events by date
    return events
