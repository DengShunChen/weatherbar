from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

date='2019/05/04'
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1L-HZDaf9ZPKkXmDkdcOAOofCzCUfOydgssGiDgFuBuA'
SAMPLE_RANGE_NAME = date+'感恩代禱事項!A:B'

def readprayer():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
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
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    strings=''
    if not values:
        print('No data found.')
    else:
        for r,row in enumerate(values):
            # Print columns A and E, which correspond to indices 0 and 4.
            try:
              if r == 0:
              #  print('    %-4.4s: %s %s' % (row[0], row[1]),date)
                strings = strings + '    %-4.4s: %s %s' % (row[0], date, row[1]) + '\n'
              else:
             #   print('%2.2d. %-4.4s: %s' % (r,row[0], row[1]))
                strings = strings + '%2.2d. %-4.4s: %s' % (r,row[0], row[1]) + '\n'
            except: 
            #  print('%2.2d. %-4.4s: %s' % (r,row[0], '<<尚未填寫>>'))
              strings = strings + '%2.2d. %-4.4s: %s' % (r,row[0], '<<尚未填寫>>') + '\n'

    return strings

if __name__ == '__main__':
    strings = readprayer()
    print(strings)
