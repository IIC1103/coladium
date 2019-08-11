# main libs
from dotenv import load_dotenv
from requests import Session
from typing import Dict
from os import getenv
from bs4 import BeautifulSoup


# local
from urls import CATALOG, LOGIN, STUDENT_LIST

load_dotenv()


# OR, the same with increased verbosity
load_dotenv(verbose=True)

data: Dict[str, str] = {
    'login': getenv('USER'),
    'passwd': getenv('PASSWORD')
}
browser = Session()
browser.post(LOGIN, data=data)

catalog = browser.get(CATALOG).text
print(catalog)
matches = catalog.split('IIC1103')
print(matches[0])
ids = list(map(lambda x: x[-7: -2], matches))

print(ids)


class Explorer:
    def __init__(self, username: str, password: str, course: str):

        # The course to be scrapped
        self.course = course

        # Create the connection with the site. Store the cookies
        self.session = Session()

        # Login to SIDING
        credentials: Dict[str, str] = {'login': username, 'passwd': password}
        self.session.post(LOGIN, data=credentials)

    @property
    def sections_ids(self):
        '''
        A list of ids of every section of the course
        '''

        # Get the HTML of the catalog
        catalog_html = self.session.get(CATALOG).text

        # Split by course code and make a list of matches
        matches = catalog_html.split(self.course)[:-1]  # Last one has no info

        # Search the sections in the matches found
        return [sid[-7:-2] for sid in matches]

    def _section_html(self, *, section_id: str):
        '''
        Grabs the HTML of a section an returns it
        '''

        # Insert section id
        url = STUDENT_LIST.substitute(section_id=section_id)

        # return the HTML
        return self.session.get(url).text

    def _parse_row(self, row):
        '''
        Strips and makes a list for each row given
        '''

        return list(map(lambda s: s.strip(), row.find_all('td')))

    def _parse_table(self, table):
        '''
            Makes a list of rows from a table of HTML
        '''

        print(type(table))

        # Find all rows in html
        rows = table.find_all('tr')[:-1]  # omit headers

        # Return the list of rows
        return list(map(lambda row: self._parse_row(row), rows))

    def get_students(self, *, section_id: str):
        