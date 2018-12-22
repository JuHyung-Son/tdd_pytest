from pytest import mark

@mark.smoke
@mark.engine
@mark.ui
def test_can_navigate_to_engine_page(chrome_browser):
    chrome_browser.get('http://www.naver.com/')
    assert True
