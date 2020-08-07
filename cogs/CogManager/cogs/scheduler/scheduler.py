from __future__ import print_function

import schedule
import time
from redbot.core import commands, checks
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from oauth2client import client
from oauth2client.service_account import ServiceAccountCredentials
# If modifying these scopes, delete the file token.pickle.

scope = ["https://www.googleapis.com/auth/calendar", "https://www.googleapis.com/auth/calendar.events","https://www.googleapis.com/auth/drive...","https://www.googleapis.com/auth/drive"]

class Scheduler(commands.Cog):

    @commands.command()
    async def events(self, ctx: commands.Context, *args: str):
        # if args.lower() == 'soon':
        creds = 'cogs/CogManager/cogs/scheduler/creds.json'
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'cogs/CogManager/cogs/scheduler/creds.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        ctx.channel.send('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            ctx.channel.send('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            ctx.channel.send()