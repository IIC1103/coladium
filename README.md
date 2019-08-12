# Coladium

A script for collecting all the students on a course in SIDING (in all the course's sections) and placing them on a google sheets.

## Credits

Thanks to [@lileiva](https://github.com/lileiva) for collaborating and doing all the siding side of the script.

## Requirements

* Python 3.68+
* Pipenv
* Google clouds api project (with google sheets)

### Installing

Install pipenv.

```bash
pip install -U pipenv
```

Install dependencies.

```bash
pipenv install --dev
```

Set up the environment variables.

```bash
touch .env
```

The `.env` should look like this.

```dotenv
SIDING_USERNAME = {siding admin username}
SIDING_PASSWORD = {siding admin password}
COURSE = {siding course name i.e IIC1103}
SHEET_ID = {google sheets id}
```

You should also download a credentials file from google cloud platform. For more information [read the beginning of this](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html)

**PLEASE MAKE SURE YOU RENAME THE FILE TO `credentials.json`**, otherwise it won't work.

## Usage

```bash
pipenv shell
python main.py
```
