import json
from pytest import fixture
from selenium import webdriver


def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data

@fixture(params=[
    webdriver.Chrome, webdriver.Firefox, webdriver.Edge
])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()

@fixture(params=load_test_data('test_data.json'))
def tv_brand(request):
    data = request.param
    return data
