from locators import AutorizationLocators
from locators import TemporaryCodeLocators
from locators import RecoveryPasswordLocators
from locators import AutorizationLoginLocators
from locators import AutorizationMAILLocators
from locators import YaSearchLocators
from base_page import BasePage

class LoginPageHelper(BasePage):

    def click_word_login(self):
        return self.find_element(AutorizationLoginLocators.LOCATOR_WORD_LOGIN, time=2).click()

    def entry_in_field_login(self, word):
        in_field_login = self.find_element(AutorizationLoginLocators.LOCATOR_FIELD_LOGIN)
        in_field_login.click()
        in_field_login.send_keys(word)
        return in_field_login

    def entry_login_password(self, word):
        login_password = self.find_element(AutorizationLoginLocators.LOCATOR_LOGIN_PASSWORD)
        login_password.click()
        login_password.send_keys(word)
        return login_password

    def click_login_button_remember_me(self):
        login_button_remember_me = self.find_element(AutorizationLoginLocators.LOCATOR_LOGIN_BUTTON_REMEMBER_ME)
        login_button_remember_me.click()
        return login_button_remember_me

    def click_login_button_to_come_in(self):
        login_button_to_come_in = self.find_element(AutorizationLoginLocators.LOCATOR_LOGIN_BUTTON_TO_COME_IN)
        login_button_to_come_in.click()
        return login_button_to_come_in

    def login_wrong_login_or_password(self):
        login_wrong_login_or_password = self.find_element(AutorizationLoginLocators.LOCATOR_LOGIN_WRONG_LOGIN_OR_PASSWORD)
        return [x.text for x in login_wrong_login_or_password]

    def your_login_when_registering(self):
        login_when_registering = self.find_element(AutorizationLoginLocators.LOCATOR_YOUR_LOGIN_WHEN_REGISTERING)
        return [x.text for x in login_when_registering]

class MailPageHelper(BasePage):

    def click_word_mail(self):
        return self.find_element(AutorizationMAILLocators.LOCATOR_WORD_MAIL, time=2).click()

    def entry_email_mail(self, word):
        email_mail = self.find_element(AutorizationMAILLocators.LOCATOR_EMAIL_MAIL)
        email_mail.click()
        email_mail.send_keys(word)
        return email_mail

    def entry_mail_password(self, word):
        mail_password = self.find_element(AutorizationMAILLocators.LOCATOR_MAIL_PASSWORD)
        mail_password.click()
        mail_password.send_keys(word)
        return mail_password

    def click_mail_button_remember_me(self):
        mail_button_remember_me = self.find_element(AutorizationMAILLocators.LOCATOR_MAIL_BUTTON_REMEMBER_ME)
        mail_button_remember_me.click()
        return mail_button_remember_me

    def click_mail_button_to_come_in(self):
        mail_button_to_come_in = self.find_element(AutorizationMAILLocators.LOCATOR_MAIL_BUTTON_TO_COME_IN)
        mail_button_to_come_in.click()
        return mail_button_to_come_in

    def mail_wrong_login_or_password(self):
        wrong_login_or_password = self.find_element(AutorizationMAILLocators.LOCATOR_MAIL_WRONG_LOGIN_OR_PASSWORD)
        return [x.text for x in wrong_login_or_password]

class SearchPageHelper(BasePage):

    def click_word_phono(self):
        return self.find_element(AutorizationLocators.LOCATOR_WORD_PHONE, time=2).click()

    def entry_phone_number(self, word):
        phone_number = self.find_element(AutorizationLocators.LOCATOR_NUMBER_PHONE)
        phone_number.click()
        phone_number.send_keys(word)
        return phone_number

    def entry_email_password(self, word):
        email_password = self.find_element(AutorizationLocators.LOCATOR_EMAIL_PASSWORD)
        email_password.click()
        email_password.send_keys(word)
        return email_password

    def click_button_remember_me(self):
        button_remember_me = self.find_element(AutorizationLocators.LOCATOR_BUTTON_REMEMBER_ME)
        button_remember_me.click()
        return button_remember_me

class TemporaryCodePageHelper(BasePage):

    def click_word_phono_authoriz(self):
        return self.find_element(TemporaryCodeLocators.LOCATOR_WORD_PHONE_AUTHORIZATION, time=2).click()

    def entry_phone_number_authoriz(self, word):
        phone_number_authoriz = self.find_element(TemporaryCodeLocators.LOCATOR_NUMBER_PHONE_AUTHORIZATION)
        phone_number_authoriz.click()
        phone_number_authoriz.send_keys(word)
        return phone_number_authoriz

    def entry_email_password_authoriz(self, word):
        email_password_authoriz = self.find_element(TemporaryCodeLocators.LOCATOR_EMAIL_PASSWORD_AUTHORIZATION)
        email_password_authoriz.click()
        email_password_authoriz.send_keys(word)
        return email_password_authoriz

    def entry_email_phone_authoriz_code(self, word):
        email_phone_authoriz_code = self.find_element(TemporaryCodeLocators.LOCATOR_EMAIL_PHONE_AUTHORIZATION_CODE)
        email_phone_authoriz_code.click()
        email_phone_authoriz_code.send_keys(word)
        return email_phone_authoriz_code

    def entry_number_1_code(self, word):
        number_1_code = self.find_element(TemporaryCodeLocators.LOCATOR_BUTTON_NUMBER_1_CODE)
        number_1_code.click()
        number_1_code.send_keys(word)
        return number_1_code

    def entry_number_2_code(self, word):
        number_2_code = self.find_element(TemporaryCodeLocators.LOCATOR_BUTTON_NUMBER_2_CODE)
        number_2_code.click()
        number_2_code.send_keys(word)
        return number_2_code

    def entry_number_3_code(self, word):
        number_3_code = self.find_element(TemporaryCodeLocators.LOCATOR_BUTTON_NUMBER_3_CODE)
        number_3_code.click()
        number_3_code.send_keys(word)
        return number_3_code

    def entry_number_4_code(self, word):
        number_4_code = self.find_element(TemporaryCodeLocators.LOCATOR_BUTTON_NUMBER_4_CODE)
        number_4_code.click()
        number_4_code.send_keys(word)
        return number_4_code

    def entry_number_5_code(self, word):
        number_5_code = self.find_element(TemporaryCodeLocators.LOCATOR_BUTTON_NUMBER_5_CODE)
        number_5_code.click()
        number_5_code.send_keys(word)
        return number_5_code

    def entry_number_6_code(self, word):
        number_6_code = self.find_element(TemporaryCodeLocators.LOCATOR_BUTTON_NUMBER_6_CODE)
        number_6_code.click()
        number_6_code.send_keys(word)
        return number_6_code

    def click_button_remember_authoriz(self):
        button_remember_authoriz = self.find_element(TemporaryCodeLocators.LOCATOR_BUTTON_REMEMBER_ME_AUTHORIZATION)
        button_remember_authoriz.click()
        return button_remember_authoriz

    def click_button_to_come_in_authoriz(self):
        button_to_come_in_authoriz = self.find_element(TemporaryCodeLocators.LOCATOR_BUTTON_TO_COME_IN_AUTHORIZATION)
        button_to_come_in_authoriz.click()
        return button_to_come_in_authoriz

    def click_link_private_office(self):
        link_private_office = self.find_element(TemporaryCodeLocators.LOCATOR_PRIVATE_OFFICE)
        link_private_office.click()
        return link_private_office

    def click_link_private_office_username(self):
        link_private_office_username = self.find_element(TemporaryCodeLocators.LOCATOR_PRIVATE_OFFICE_USERNAME)
        link_private_office_username.click()
        return link_private_office_username

    def click_link_office_username_log_off(self):
        link_office_username_lod_off = self.find_element(TemporaryCodeLocators.LOCATOR_PRIVATE_OFFICE_USERNAME_LOG_OFF)
        link_office_username_lod_off.click()
        return link_office_username_lod_off

    def click_button_to_get_code(self):
        button_to_get_code = self.find_element(TemporaryCodeLocators.LOCATOR_BUTTON_TO_GET_CODE)
        button_to_get_code.click()
        return button_to_get_code

    def click_link_change_phone_code(self):
        link_change_phone_code = self.find_element(TemporaryCodeLocators.LOCATOR_CHANGE_PHONE_OR_MAIL_CODE)
        link_change_phone_code.click()
        return link_change_phone_code

    def form_work_hint_code(self):
        form_work_hint = self.find_element(TemporaryCodeLocators.LOCATOR_FORM_WORK_HINT)
        return [x.text for x in form_work_hint]

class RecoveryPageHelper(BasePage):

    def click_word_login_recovery(self):
        return self.find_element(RecoveryPasswordLocators.LOCATOR_WORD_RECOVERY_LOGIN, time=2).click()

    def click_word_phone_recovery(self):
        return self.find_element(RecoveryPasswordLocators.LOCATOR_WORD_RECOVERY_PHONE, time=2).click()

    def click_word_mail_recovery(self):
        return self.find_element(RecoveryPasswordLocators.LOCATOR_WORD_RECOVERY_MAIL, time=2).click()

    def click_word_personal_account_recovery(self):
        return self.find_element(RecoveryPasswordLocators.LOCATOR_WORD_RECOVERY_PERSONAL_ACCOUNT, time=2).click()

    def entry_field_phone_or_mail_or_login_or_personalaccount(self, word):
        field_login_recovery = self.find_element(RecoveryPasswordLocators.LOCATOR_FIELD_RECOVERY_USERNAME)
        field_login_recovery.click()
        field_login_recovery.send_keys(word)
        return field_login_recovery

    def entry_password_field(self, word):
        password_field = self.find_element(RecoveryPasswordLocators.LOCATOR_PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(word)
        return password_field

    def entry_field_symbols(self, word):
        field_symbols = self.find_element(RecoveryPasswordLocators.LOCATOR_FIELD_SYMBOLS)
        field_symbols.click()
        field_symbols.send_keys(word)
        return field_symbols

    def click_button_continue_recovery(self):
        button_continue_recovery = self.find_element(RecoveryPasswordLocators.LOCATOR_RECOVERY_BUTTON_CONTINUE)
        button_continue_recovery.click()
        return button_continue_recovery

    def click_link_come_back_recovery(self):
        link_come_back_recovery = self.find_element(RecoveryPasswordLocators.LOCATOR_RECOVERY_LINK_COME_BACK)
        link_come_back_recovery.click()
        return link_come_back_recovery

    def click_button_to_come_in_recovery(self):
        button_to_come_in_recovery = self.find_element(RecoveryPasswordLocators.LOCATOR_BUTTON_TO_COME_IN_RECOVERY)
        button_to_come_in_recovery.click()
        return button_to_come_in_recovery

    def click_link_forgot_password_recovery(self):
        link_forgot_password_recovery = self.find_element(RecoveryPasswordLocators.LOCATOR_LINK_FORGOT_PASSWORD_RECOVERY)
        link_forgot_password_recovery.click()
        return link_forgot_password_recovery

    def recovery_wrong_login_or_text_with_pictures(self):
        wrong_login_or_text_with_pictures = self.find_element(RecoveryPasswordLocators.LOCATOR_RECOVERY_WRONG_LOGIN_OR_PICTURES)
        return [x.text for x in wrong_login_or_text_with_pictures]

    def recovery_word_authorization_text(self):
        word_authorization_text = self.find_element(RecoveryPasswordLocators.LOCATOR_WORD_AUTHORIZATION)
        value_word_authorization_text = word_authorization_text.text
        return value_word_authorization_text

class SearchHelper(BasePage):

    def click_word_registration(self):
        return self.find_element(YaSearchLocators.LOCATOR_LINK_REGISTRATION, time=2).click()

    def click_button_register(self):
        button_register = self.find_element(YaSearchLocators.LOCATOR_BUTTON_REGISTER)
        button_register.click()
        return button_register

    def click_button_login_to_account(self):
        button_login_to_account = self.find_element(YaSearchLocators.LOCATOR_BUTTON_LOGIN_TO_ACCOUNT)
        button_login_to_account.click()
        return button_login_to_account

    def click_link_password_recovery(self):
        link_password_recovery = self.find_element(YaSearchLocators.LOCATOR_LINK_PASSWORD_RECOVERY)
        link_password_recovery.click()
        return link_password_recovery

    def word_name_registration(self, word):
        name_registration = self.find_element(YaSearchLocators.LOCATOR_NAME_REGISTRATION)
        name_registration.click()
        name_registration.send_keys(word)
        return name_registration

    def word_family_registration(self, word):
        family_registration = self.find_element(YaSearchLocators.LOCATOR_FAMILY_REGISTRATION)
        family_registration.click()
        family_registration.send_keys(word)
        return family_registration

    def registration_email_or_phone(self, word):
        address_email_or_phone = self.find_element(YaSearchLocators.LOCATOR_REGISTRATION_EMAIL_OR_PHONE)
        address_email_or_phone.click()
        address_email_or_phone.send_keys(word)
        return address_email_or_phone

    def registration_password(self, word):
        password_registration = self.find_element(YaSearchLocators.LOCATOR_PASSWORD_REGISTRATION)
        password_registration.click()
        password_registration.send_keys(word)
        return password_registration

    def registration_password_confirmation(self, word):
        password_confirmation_registration = self.find_element(YaSearchLocators.LOCATOR_PASSWORD_CONFIRMATION_REGISTRATION)
        password_confirmation_registration.click()
        password_confirmation_registration.send_keys(word)
        return password_confirmation_registration

    def page_registration_word_text(self):
        registration_word_text = self.find_element(YaSearchLocators.LOCATOR_REGISTRATION_WORD_TEXT)
        value_registration_word_text = registration_word_text.text
        return value_registration_word_text



    def registration_account_exists(self):
        account_exists_text = self.find_element(YaSearchLocators.LOCATOR_REGISTRATION_ACCOUNT_EXISTS)
        return [x.text for x in account_exists_text]