from pytest import mark


def test_televisions_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected")

@mark.xfail
def test_browser_can_navigate_to_training_ground(browser):
    browser.get('http://techstepacademy.com/trining-ground')