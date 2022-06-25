import pytest
from selene import be
from selene.support.shared import browser

@pytest.fixture()
def setup():
    browser.open('https://www.google.com/')
    browser.element("[name='q']").should(be.blank).type("selene python").press_enter()

@pytest.fixture()
def window_size():
    browser.driver.set_window_size(width=800, height=600)






