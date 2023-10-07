import pytest
import elements
import locators
import time
from selenium.webdriver.common.action_chains import ActionChains

# @pytest.mark.skip
def test_sign_up_button():
    """Убедится что при клике на кнопку Sign up появляется окно c тайтлом Registration"""
    url = "https://guest:welcome2qauto@qauto.forstudy.space/"
    driver = elements.get_site(url)
    element = elements.find_element(driver, *locators.MainPageLocators.sign_up_button)
    assert element is not None
    elements.click(element)
    element = elements.find_element(driver, *locators.SignUpPopupLocators.popup_title_registration)
    assert element is not None, "The element not found"


# @pytest.mark.skip
def test_contacts_on_the_main_page():
    """Убедится что на главной странице присутствуют контакты компании"""
    url = "https://guest:welcome2qauto@qauto.forstudy.space/"
    driver = elements.get_site(url)
    element = elements.find_element(driver, *locators.MainPageLocators.contacts_title)
    assert element is not None, "The element not found"


# @pytest.mark.skip
# def test_login_with_true_credentials():
#     """Залогиниться авторизованным пользователем и убедиться что на странице https://qauto.forstudy.space/panel/garage появляется тайтл Garage """
#     url = "https://guest:welcome2qauto@qauto.forstudy.space/"
#     email_login = "leonidych73@gmail.com"
#     password_login = "Password1@"
#     driver = elements.get_site(url)
#     element = elements.find_element(driver, *locators.MainPageLocators.signin_button)
#     elements.click(element)
#     element = elements.find_element(driver, *locators.SignInPopupLocators.email_field_login)
#     elements.field_input(element, email_login)
#     element = elements.find_element(driver, *locators.SignInPopupLocators.password_field_login)
#     elements.field_input(element, password_login)
#     element = elements.find_element(driver, *locators.SignInPopupLocators.login_button_primary)
#     elements.click(element)
#     element = elements.find_element(driver, *locators.MainAuthorizedPageLocators.garage_title)
#     assert element is not None, "The element not found"


def deco_auth(func):  # Декоратор для авторизации пользователя.
    def wrapper():
        url = "https://guest:welcome2qauto@qauto.forstudy.space/"
        email_login = "leonidych73@gmail.com"
        password_login = "Password1@"
        driver = elements.get_site(url)
        element = elements.find_element(driver, *locators.MainPageLocators.signin_button)
        elements.click(element)
        element = elements.find_element(driver, *locators.SignInPopupLocators.email_field_login)
        elements.field_input(element, email_login)
        element = elements.find_element(driver, *locators.SignInPopupLocators.password_field_login)
        elements.field_input(element, password_login)
        element = elements.find_element(driver, *locators.SignInPopupLocators.login_button_primary)
        elements.click(element)
        func(driver)
        time.sleep(5)
    return wrapper


def deco_remove_car(func):  # Декоратор для удаления добавленного автомобиля из гаража.
    def wrapper(driver):
        func(driver)
        elements.click(elements.find_element(driver, *locators.MainAuthorizedPageLocators.last_car_edit_button))
        elements.click(elements.find_element(driver, *locators.EditCarPopupLocator.remove_car_button))
        elements.click(elements.find_element(driver, *locators.EditCarPopupLocator.remove_button))
    return wrapper


# @pytest.mark.skip
@deco_auth
def test_login_with_true_credentials(driver):
    """Залогиниться авторизованным пользователем и убедиться что на странице https://qauto.forstudy.space/panel/garage появляется тайтл Garage """
    element = elements.find_element(driver, *locators.MainAuthorizedPageLocators.garage_title)
    assert element is not None, "The element not found"

# @pytest.mark.skip
@deco_auth
@deco_remove_car
def test_add_car(driver):
    """Добавить авто в гараж, убедиться что на странице появляется запись с названием добавленного автомобиля"""
    mileage_value = "120000"
    elements.click(elements.find_element(driver, *locators.MainAuthorizedPageLocators.add_car_button))
    elements.click(elements.find_element(driver, *locators.AddCarPopupLocators.brand_field))
    elements.click(elements.find_element(driver, *locators.AddCarPopupLocators.bmw_option))
    element = elements.find_element(driver, *locators.AddCarPopupLocators.mileage_field)
    elements.field_input(element, mileage_value)
    elements.click(elements.find_element(driver, *locators.AddCarPopupLocators.add_button))
    element = elements.find_element(driver, *locators.AddCarPopupLocators.last_car_name)
    text = elements.get_text_element(element)
    time.sleep(2)
    assert text == "BMW 3", "Car name not found"

# @pytest.mark.skip
@deco_auth
@deco_remove_car
def test_mileage_reduction(driver):
    """Проверить что при корректировке пробега если ввести меньший пробег чем был введен при
    добавлении автомобиля, то появится служебное сообщение "New mileage is less then previous entry" """
    mileage_value = "120000"
    edited_mileage_value = "100000"
    elements.click(elements.find_element(driver, *locators.MainAuthorizedPageLocators.add_car_button))
    elements.click(elements.find_element(driver, *locators.AddCarPopupLocators.brand_field))
    elements.click(elements.find_element(driver, *locators.AddCarPopupLocators.bmw_option))
    element = elements.find_element(driver, *locators.AddCarPopupLocators.mileage_field)
    elements.field_input(element, mileage_value)
    elements.click(elements.find_element(driver, *locators.AddCarPopupLocators.add_button))
    time.sleep(1)
    elements.click(elements.find_element(driver, *locators.MainAuthorizedPageLocators.last_car_edit_button))
    element = elements.find_element(driver, *locators.AddCarPopupLocators.mileage_field)
    elements.field_input(element, edited_mileage_value)
    elements.click(elements.find_element(driver, *locators.EditCarPopupLocator.save_button))
    element = elements.find_element(driver,*locators.EditCarPopupLocator.warning_message_less_mileage)
    assert element is not None, "There is not warning message"
    assert (elements.get_text_element(element)) == "New mileage is less then previous entry", "Wrong warning message"
    elements.click(elements.find_element(driver, *locators.EditCarPopupLocator.cancel_button))

# @pytest.mark.skip
def test_restore_access_popup():
    """Проверить что если зарегистрированный пользователь кликнет в меню логина на кнопку Forgot_password то
    появится окно Restore access"""
    url = "https://guest:welcome2qauto@qauto.forstudy.space/"
    driver = elements.get_site(url)
    elements.click(elements.find_element(driver, *locators.MainPageLocators.signin_button))
    elements.click(elements.find_element(driver, *locators.SignInPopupLocators.forgot_password))
    element = elements.find_element(driver, *locators.SignInPopupLocators.restore_access_title)
    assert element is not None, "The element not found"

# @pytest.mark.skip
@deco_auth
def test_fuel_expenses_button(driver):
    """Проверить, что если на странице авторизованного пользователя кликнуть на кнопку Fuel expenses то
    осуществиться пререход на страницу https://qauto.forstudy.space/panel/expenses """
    expected_url = "https://guest:welcome2qauto@qauto.forstudy.space/panel/expenses"
    elements.click(elements.find_element(driver, *locators.MainAuthorizedPageLocators.fuel_expenses_button))
    assert driver.current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {driver.current_url}"

# @pytest.mark.skip
@deco_auth
@deco_remove_car
def test_add_fuel_expense_button(driver):
    """Добавить автомобиль, убедиться что кнопка Add fuel expense присутствует в блоке информации нового автомобиля"""
    mileage_value = "120000"
    elements.click(elements.find_element(driver, *locators.MainAuthorizedPageLocators.add_car_button))
    elements.click(elements.find_element(driver, *locators.AddCarPopupLocators.brand_field))
    elements.click(elements.find_element(driver, *locators.AddCarPopupLocators.bmw_option))
    element = elements.find_element(driver, *locators.AddCarPopupLocators.mileage_field)
    elements.field_input(element, mileage_value)
    elements.click(elements.find_element(driver, *locators.AddCarPopupLocators.add_button))
    element = elements.find_element(driver, *locators.MainAuthorizedPageLocators.add_fuel_expense_button)
    assert element is not None, "The element not found"

# @pytest.mark.skip
@deco_auth
@deco_remove_car
def test_correct_changed_model(driver):
    """Убедиться, что после корректировки модели автомобиля на странице гараж отображается правильная модель """
    mileage_value = "50000"
    elements.click(elements.find_element(driver, *locators.MainAuthorizedPageLocators.add_car_button))
    elements.click(elements.find_element(driver, *locators.AddCarPopupLocators.brand_field))
    elements.click(elements.find_element(driver, *locators.AddCarPopupLocators.bmw_option))
    element = elements.find_element(driver, *locators.AddCarPopupLocators.mileage_field)
    elements.field_input(element, mileage_value)
    elements.click(elements.find_element(driver, *locators.AddCarPopupLocators.add_button))
    elements.click(elements.find_element(driver, *locators.MainAuthorizedPageLocators.last_car_edit_button))
    elements.click(elements.find_element(driver, *locators.AddCarPopupLocators.brand_field))
    elements.click(elements.find_element(driver, *locators.AddCarPopupLocators.porsche_option))
    elements.click(elements.find_element(driver, *locators.AddCarPopupLocators.model_field))
    elements.click(elements.find_element(driver, *locators.AddCarPopupLocators.panamera_option))
    elements.click(elements.find_element(driver, *locators.EditCarPopupLocator.save_button))
    time.sleep(3)
    element = elements.find_element(driver, *locators.AddCarPopupLocators.last_car_name)
    text = elements.get_text_element(element)
    assert text == "Porsche Panamera", "Car name not found"

@deco_auth
def test_unit_distance_change(driver):
    """Убедиться что при изменении единицы измерения пробега в настройке в меню добавления автомобилямера расстояния меняется на соответствующую"""
    elements.click(elements.find_element(driver, *locators.MainAuthorizedPageLocators.add_car_button))
    element = elements.find_element(driver, *locators.AddCarPopupLocators.mileage_measure_input)
    input_unit = elements.get_text_element(element)
    elements.click(elements.find_element(driver, *locators.AddCarPopupLocators.x_button))
    elements.click(elements.find_element(driver, *locators.MainAuthorizedPageLocators.settings_button))
    actions = ActionChains(driver) # происходит перекрытие елементов поэтому использую ActionChains
    if input_unit == "km":
        # elements.click(elements.find_element(driver, *locators.MainAuthorizedPageLocators.distance_ml_settings))
        actions.click(elements.find_element(driver, *locators.MainAuthorizedPageLocators.distance_ml_settings)).perform()
        changed_unit = "ml"
    else:
        # elements.click(elements.find_element(driver, *locators.MainAuthorizedPageLocators.distance_ml_settings))
        actions.click(elements.find_element(driver, *locators.MainAuthorizedPageLocators.distance_km_settings)).perform()
        changed_unit = "km"
    time.sleep(1)
    elements.click(elements.find_element(driver, *locators.MainAuthorizedPageLocators.garage_button))
    elements.click(elements.find_element(driver, *locators.MainAuthorizedPageLocators.add_car_button))
    element = elements.find_element(driver, *locators.AddCarPopupLocators.mileage_measure_input)
    input_unit = elements.get_text_element(element)
    assert input_unit == changed_unit, "Input distance unit is wrong"




