import urllib3
from urllib3.exceptions import InsecureRequestWarning

def pytest_configure():
    urllib3.disable_warnings(category=InsecureRequestWarning)
