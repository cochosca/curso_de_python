from googleapiclient.discovery import build
from google.oauth2 import service_account
import os.path

# Generacion de las credenciales // Generate credentials 
SERVICE_ACCOUNT_FILE = 'path/to/llaves.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheet']
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID  spreadsheet.
SAMPLE_SPREADSHEET_ID = '1Vm7YdHEandb4yb3cJZVTfzalG9ruvwIzLsf42oU1dtA'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range='prueba!A1:B15').execute()
values = result.get('values', [])
print(values)



