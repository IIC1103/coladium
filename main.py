# main libs
from dotenv import load_dotenv
from os import getenv
from typing import Dict
from time import sleep

# local
from explorer import Explorer
from sheets_service import Worksheet

load_dotenv()


def main():
    data: Dict[str, str] = {
        'username': getenv('SIDING_USERNAME'),
        'password': getenv('SIDING_PASSWORD'),
        'course': getenv('COURSE')
    }
    explorer = Explorer(**data)
    worksheet = Worksheet(sheet_id=getenv('SHEET_ID'))
    print('Collecting students')
    sections = []
    for sid in explorer.sections_ids:
        sections.append(explorer.get_students(section_id=sid))
        sleep(1.3)
    print('Adding to google sheets.')

    total = len(sections)
    for section_number, student_set in enumerate(sections, start=1):
        print(f'Section {section_number}/{total}.')
        added = worksheet.add_students(student_set, section_number, index=0)
        print(f'{added} students added.')
    print('Done.')


if __name__ == "__main__":
    main()
