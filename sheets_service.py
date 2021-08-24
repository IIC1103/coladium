from project_types import Student
import gspread
import gspread.exceptions as gspExceptions
from oauth2client.service_account import ServiceAccountCredentials
from typing import List, Set
from time import sleep
from string import ascii_uppercase

QUOTA = 1  # 1s per request to the api


class Worksheet:
    def __init__(self, *, sheet_id: str):
        self.sheet_id = sheet_id

        # Define the scope of permissions
        scope = ["https://spreadsheets.google.com/feeds"]
        # use creds to create a client to interact with the Google Drive API
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        self.client = gspread.authorize(creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        self.sheet = self.client.open_by_key(self.sheet_id).worksheet("Todos")

    def _as_student(self, row: List[str]) -> Student:
        return tuple(map(str, row))

    @property
    def current_students(self) -> Set[Student]:
        """Obtains the current list of students from the spreadsheet"""

        students: Set[Student] = set(
            map(lambda row: self._as_student(row), self.sheet.get("A2:H"))
        )
        print(list(filter(lambda row: "manu.ripamonti@uc.cl" in row, students)))
        return students

    def add_students(self, student_list: Set[Student]):
        """
        Adds a batch of students to a section.
        The index paramater corresponds to the index of the student item
        where the student number is.
        Returns the number of students added.
        """
        section = 0
        rows = sorted(student_list, key=lambda student: int(student[section]))
        self.sheet.append_rows(rows)
