from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("/")

    s(".header-search-button").click()
    s("#query-builder-test").send_keys("MaryMokretsova/qa_guru_python_9_8")
    s("#query-builder-test").submit()

    s(by.link_text("MaryMokretsova/qa_guru_python_9_8")).click()

    s("#issues-tab").click()

    s(by.partial_text("#3")).should(be.visible)