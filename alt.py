import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from parameters import URL, USERNAME, PASSWORD


def get_admin_courses(driver):
    big_table = driver.find_element_by_tag_name("table")
    body = big_table.find_element_by_tag_name("tbody")
    table_element = big_table.find_elements_by_tag_name("tr")[1]
    work_zone = table_element.find_element_by_class_name(
        "ColorFondoZonaTrabajo")
    tables = work_zone.find_element_by_tag_name(
        "table").find_element_by_tag_name(
            "tbody").find_element_by_tag_name(
                "tr").find_element_by_tag_name(
                    "td").find_elements_by_tag_name("table")
    for table in tables:
        if is_admin_table(table):
            return table


def is_admin_table(table):
    body = table.find_element_by_tag_name("tbody")
    if not body:
        return False
    tr_elem = table.find_element_by_tag_name("tr")
    if not tr_elem:
        return False
    td_elem = table.find_element_by_tag_name("td")
    if not td_elem:
        return False
    return "administrador" in td_elem.text.lower()


# Create browser and get url
driver = webdriver.Chrome()
driver.get(URL)

# Fill username and password
username = driver.find_element_by_id("user-siding")
password = driver.find_element_by_id("password-siding")
username.clear()
username.send_keys(USERNAME)
password.clear()
password.send_keys(PASSWORD)
password.submit()


# Hasta acá funciona


# Click "Docencia"
driver.find_element_by_id("TopMenu_link_550").click()

# Click "IngCursos"
driver.find_element_by_id(
    "link_sect_siding_dirdes_ingcursos_cursos_index_phtml").click()

menu_url = driver.current_url

admin_table = get_admin_courses(driver).find_element_by_tag_name(
    "tbody").find_elements_by_tag_name("tr")[2:]

for element in admin_table:
    element.find_element_by_tag_name("a").click()
    driver.get(menu_url)

driver.close()