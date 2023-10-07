from selenium.webdriver.common.by import By


class MainPageLocators():
    sign_up_button = (By.XPATH, '//button[@class="hero-descriptor_btn btn btn-primary"]')
    contacts_title = (By.XPATH, '//h2[text()="Contacts"]')
    signin_button = (By.XPATH, '//button[@class="btn btn-outline-white header_signin"]')


class SignInPopupLocators():
    email_field_login = (By.XPATH, '//input[@id="signinEmail"]')
    password_field_login = (By.XPATH, '//input[@id="signinPassword"]')
    login_button_primary = (By.XPATH, '//button[@class="btn btn-primary"]')
    forgot_password = (By.XPATH, '//button[@class="btn btn-link" and contains(text(),"Forgot password")]')
    restore_access_title = (By.XPATH, '//h4[@class="modal-title" and contains(text(),"Restore access")]')



class SignUpPopupLocators():
    popup_title_registration = (By.XPATH, '//h4[@class="modal-title" and text() = "Registration"]')


class MainAuthorizedPageLocators():
    garage_title = (By.XPATH, '//h1[contains(text(), "Garage")]')
    add_car_button = (By.XPATH, '//button[contains(text(), "Add car")]')
    last_car_edit_button = (By.XPATH, '//span[@class="icon icon-edit"]')    #'(//button[@class="car_edit btn btn-edit"])[1]')
    fuel_expenses_button = (By.XPATH, '//a[@href="/panel/expenses"]/span[@class="icon icon-fuel"]')
    add_fuel_expense_button = (By.XPATH, '//button[@class="car_add-expense btn btn-success" and contains(text(), "Add fuel expense")]')
    settings_button = (By.XPATH, '//a[@class="btn btn-white btn-sidebar sidebar_btn" and@href="/panel/settings"]')
    distance_km_settings = (By.XPATH, '/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-settings/div/div[2]/div/div[2]/div/button[1]')
    distance_ml_settings = (By.XPATH, '//button[@class="settings-control btn btn-secondary" and contains(text(), "ml")]')
    garage_button = (By.XPATH, '//a[@class="btn btn-white btn-sidebar sidebar_btn"and contains(text(), "Garage")]')

class AddCarPopupLocators():
    brand_field = (By.XPATH, '//*[@id="addCarBrand"]')
    model_field = (By.XPATH, '//*[@id="addCarModel"]')
    bmw_option = (By.XPATH, '//*[@id="addCarBrand"]/option[2]')
    porsche_option = (By.XPATH, '//*[@id="addCarBrand"]/option[4]')
    x5_option = (By.XPATH, '//*[@id="addCarModel"]/option[3]')
    panamera_option = (By.XPATH, '//*[@id="addCarModel"]/option[3]')
    mileage_field = (By.XPATH, '//*[@id="addCarMileage"]')
    add_button = (By.XPATH, '//button[@class="btn btn-primary" and text()="Add"]')
    last_car_name = (By.XPATH, '(//p[@class="car_name h2"])[1]')
    mileage_measure_input = (By.XPATH, '//div[@class="input-group-text"]')
    x_button = (By.XPATH, '//span[@aria-hidden="true"]')


class EditCarPopupLocator():
    remove_car_button = (By.XPATH, '//button[@class="btn btn-outline-danger" and contains(text(), "Remove car")]')
    remove_button = (By.XPATH, '//button[@class="btn btn-danger"]')
    warning_message_less_mileage = (By.XPATH, '//p[@class="alert alert-danger"]')
    save_button = (By.XPATH, '//button[@class="btn btn-primary" and contains(text(), "Save")]')
    cancel_button = (By.XPATH, '//button[@class="btn btn-secondary" and contains(text(), "Cancel")]')
