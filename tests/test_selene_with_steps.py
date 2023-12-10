import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_steps_github():
    with allure.step("Открываем главную страницу"):
        browser.open("/")

    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("MaryMokretsova/qa_guru_python_9_8")
        s("#query-builder-test").submit()

    with allure.step("Переходим по ссылке репозиторий"):
        s(by.link_text("MaryMokretsova/qa_guru_python_9_8")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 3"):
        s(by.partial_text("#3")).should(be.visible)
