import pytest
import requests
import yaml
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


with open('testdata.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture(scope='session')
def browser():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


S = requests.Session()


@pytest.fixture()
def login():
    try:
        result = S.post(url=data['gateway'], data={'username': data['login'], 'password': data['password']})
        response_json = result.json()
        token = response_json.get('token')
    except:
        logging.exception('Get token exception')
        token = None
    logging.debug(f'Return token success')
    return token


@pytest.fixture()
def quick_vulnerability_check():
    return 'nikto -h https://test-stand.gb.ru/ -ssl -Tuning 4'


