import allure
from pages.main_page_class import MainPage
from playwright.sync_api import expect

@allure.feature("Главная страница")
@allure.story("Проверка элементов")
def test_main_elements(page):
    main = MainPage(page)
    main.open(MainPage.URL)

    expect(page.locator(main.TITLE_MAIN)).to_be_visible()
    expect(page.locator(main.SUBTITLE)).to_be_visible()
    expect(page.locator(main.BTN_SEND_REQUEST)).to_be_visible()
    expect(page.locator(main.BTN_LEARN_MORE)).to_be_visible()
    expect(page.locator(main.VACANCIES_BLOCK)).to_be_visible()


@allure.feature("Главная страница")
@allure.story("Переходы по меню")
def test_header_navigation(page):
    main = MainPage(page)
    main.open(MainPage.URL)

    for name, (locator, url) in main.MENU_LINKS.items():
        with allure.step(f"Переход по меню: {name}"):
            page.locator(locator).click()
            expect(page).to_have_url(url)
            page.goto(main.URL)
