from base_page_class import BasePage

class MainPage(BasePage):
    URL = "https://effective-mobile.ru/"

    # Основные блоки
    TITLE_MAIN = "text=Эффективный мобильный"
    SUBTITLE = "text=Ваша карьера в IT начинается здесь"
    BTN_SEND_REQUEST = 'button:has-text("Оставить заявку")'
    BTN_LEARN_MORE = 'a:has-text("узнать больше")'
    VACANCIES_BLOCK = "text=Актуальные вакансии"

    # Верхнее меню
    ABOUT = 'a[href="/about"]'
    CONTACTS = 'a[href="/contacts"]'
    SERVICES = 'a[href="/services"]'

    MENU_LINKS = {
        "about": (ABOUT, "https://effective-mobile.ru/about"),
        "contacts": (CONTACTS, "https://effective-mobile.ru/contacts"),
        "services": (SERVICES, "https://effective-mobile.ru/services"),
    }
