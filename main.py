# main libs
from dotenv import load_dotenv
from os import getenv
from typing import Dict

import time

# local
from explorer import Explorer

load_dotenv()


def main():
    data: Dict[str, str] = {
        'username': getenv('SIDING_USERNAME'),
        'password': getenv('SIDING_PASSWORD'),
        'course': getenv('COURSE')
    }
    explorer = Explorer(**data)
    for sid in explorer.sections_ids:
        print(explorer.get_students(section_id=sid))
        time.sleep(1.25)


if __name__ == "__main__":
    main()
