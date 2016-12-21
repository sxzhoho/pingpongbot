from __future__ import print_function
import httplib2
import os
import time

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials
def update_score( player1, player2, score1, score2):
    gameDate = time.strftime("%d/%m/%Y")
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)
    requests=[]
    requests.append({
        'appendCells': {
            'sheetId': 0,
            'rows': [
                {
                    'values': [
                        {
                            'userEnteredValue': {'stringValue': player1},

                        }, {
                            'userEnteredValue': {'numberValue': score1},

                        }, {
                            'userEnteredValue': {'stringValue': player2},

                        }, {
                            'userEnteredValue': {'numberValue': score2},

                        }, {
                            'userEnteredValue': {'stringValue': gameDate},
                        }
                    ]
                }
            ],
            'fields': 'userEnteredValue,userEnteredFormat.backgroundColor'
        }
    })
    spreadsheet_id = '1aXEr4QOHmtOMHcmRd8Ddodlg_Yw029rEZ0TN0WEJPbw'

    batchUpdateRequest = {'requests': requests}
    service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id,
                                    body=batchUpdateRequest).execute()

def main():
    update_score( 'atul2', 'shawn', 2, 22)
    
    


if __name__ == '__main__':
    main()
