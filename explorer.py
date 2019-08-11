from requests import Session
from typing import Dict
from bs4 import BeautifulSoup, Tag


# local
from urls import CATALOG, LOGIN, STUDENT_LIST


class Explorer:
    def __init__(self, username: str, password: str, course: str):

        # The course to be scrapped
        self.course = course.upper()

        # Create the connection with the site. Store the cookies
        self.session = Session()

        # Login to SIDING
        credentials: Dict[str, str] = {'login': username, 'passwd': password}
        self.session.post(LOGIN, data=credentials).text

    @staticmethod
    def clean_tag(tag):
        '''
        Clean a bs4 tag and return its content
        '''
        return tag.get_text().strip()

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



    def _parse_row(self, row: Tag):
        '''
        Strips and makes a list for each row given
        '''
        return list(map(self.clean_tag, row.find_all('td')))

    def _parse_table(self, table):
        '''
            Makes a list of rows from a table of HTML
        '''
        # Find all rows in html
        rows = table.find_all('tr')[1:]  # omit headers
        # Return the list of rows
        return list(map(lambda row: self._parse_row(row), rows))

    def get_students(self, *, section_id: str):

        # Get the html of the section
        html = self._section_html(section_id=section_id)

        # Instantiate the soup for exploring the site
        soup = BeautifulSoup(html, 'html.parser')

        # Filter only the table it is needed
        filters = {'class': 'TablaConBordeFinoLightblue'}

        # Find the table
        table = soup.find('table', filters)

        return self._parse_table(table)

