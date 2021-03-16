import gspread
import gspread.exceptions as gspExceptions
from oauth2client.service_account import ServiceAccountCredentials
from typing import List
from time import sleep
from string import ascii_uppercase

QUOTA = 1  # 1s per request to the api


class Worksheet:
    def __init__(self, *, sheet_id: str):
        self.sheet_id = sheet_id

        # Define the scope of permissions
        scope = ['https://spreadsheets.google.com/feeds']
        # use creds to create a client to interact with the Google Drive API
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            'credentials.json', scope)
        self.client = gspread.authorize(creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        self.sheet = self.client.open_by_key(self.sheet_id).worksheet('Todos')

    def _add_student(self, student: List[str], student_number: str, section, table_range:str):
        '''
        Adds a student to the worksheet if it isn't already on the sheet.
        Returns a boolean if the user was added.
        '''

        try:

            # Try to find the student number in the worksheet
            self.sheet.find(student_number)
            # Return false if found
            return False
        except gspread.CellNotFound:
            # If exception of cell not found is raised
            # Apppend the student
            try:
                row = [section] + student
                self.sheet.append_row(row, table_range=table_range)

                # Return true as it was added
                return True
            except gspExceptions.APIError as e:
                err_json = e.response.json()
                if e.response.status_code == 400:
                    raise PermissionError(err_json['error']['message'])
                else:
                    raise ConnectionError(err_json['error']['message'])
                return False

    def add_students(self, student_list: List[List[str]], section: str,
                     *, index: int):
        '''
        Adds a batch of students to a section.
        The index paramater corresponds to the index of the student item
        where the student number is.
        Returns the number of students added.
        '''
        added = 0
        table_range = f"A2:{ascii_uppercase[len(student_list[0])]}{len(student_list) + 2}"
        for student in student_list:
            student_number = student[index]

            added += int(self._add_student(student, student_number, section, table_range))
            sleep(QUOTA)
        return added
