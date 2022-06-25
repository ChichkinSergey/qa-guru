from selene import have
from selene.support.shared import browser


# positive test
def test_google_search(setup, window_size):
    browser.element("#search").should(have.text("yashaka/selene: User-oriented Web UI browser tests in Python"))

# negative test
def test_google_search_neg(setup, window_size):
    browser.element("#search").should(have.no.text("sdfsdfasdf"))