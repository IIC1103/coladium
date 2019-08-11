import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
from os import getenv

load_dotenv(verbose=True)


class Worksheet:
    def __init__(self, *args, **kwargs):
        self.sheet_id = getenv('SHEETS_ID')
        # use creds to create a client to interact with the Google Drive API
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            'credentials.json', scope)
        self.client = gspread.authorize(creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        self.sheet = self.client.open_by_key(
        ).worksheet('Todos')
    def _add_student(self, student: List[str]):
        if not (self.sheet.findall())
# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)
