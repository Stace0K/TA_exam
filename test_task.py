import time
import subprocess
from testpage import OperationsHelper
import yaml
import logging


with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_vulnerability(quick_vulnerability_check):
    logging.info('Test Vulnerability: running')
    res = str(subprocess.run(quick_vulnerability_check, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
    assert '0 error(s)' in res, 'Test Vulnerability FAILED'


def test_log_in(browser):
    logging.info('Test Log in: running')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_passwd(testdata['passwd'])
    testpage.login_btn()
    assert testpage.get_enter_login() == f'Hello, {testdata["login"]}', 'Test Log in FAILED'


def test_font_size(browser):
    logging.info('Test Font size: running')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.about_btn()
    time.sleep(3)
    fs = testpage.font_size()
    assert fs == '32px', 'Test Font size FAILED'

