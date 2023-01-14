import time
from ali_page import SearchPageHelper
from ali_page import MailPageHelper
from ali_page import RecoveryPageHelper
from ali_page import SearchHelper
from ali_page import LoginPageHelper
from ali_page import TemporaryCodePageHelper

def test_value_number_phone(browser):
    value_number_phone = SearchPageHelper(browser)
    value_number_phone.go_to_site()
    time.sleep(10)
    value_number_phone.click_word_phono()
    value_number_phone.entry_phone_number("89521514008")
    value_number_phone.entry_email_password("Lfhmz2012ljxm")

def test_negative_number_phone_2(browser):
    negative_number_2 = SearchPageHelper(browser)
    negative_number_2.go_to_site()
    time.sleep(20)
    negative_number_2.click_word_phono()
    time.sleep(10)
    negative_number_2.entry_phone_number("@#$%#$%")
    time.sleep(5)
    negative_number_2.entry_email_password("Lfhmz2012ljxm")

def test_negative_number_phone_3(browser):
    negative_number_3 = SearchPageHelper(browser)
    negative_number_3.go_to_site()
    time.sleep(10)
    negative_number_3.click_word_phono()
    negative_number_3.entry_phone_number("пыпаи")
    negative_number_3.entry_email_password("Lfhmz2012ljxm")

def test_value_email_mail(browser):
    value_email_mail = MailPageHelper(browser)
    value_email_mail.go_to_site()
    time.sleep(20)
    value_email_mail.click_word_mail()
    time.sleep(10)
    value_email_mail.entry_email_mail("aprejzel@gmail.com" +"\h")
    time.sleep(5)

def test_negative_email_mail_2(browser):
    negative_email_mail_2 = MailPageHelper(browser)
    negative_email_mail_2.go_to_site()
    time.sleep(20)
    negative_email_mail_2.click_word_mail()
    time.sleep(10)
    negative_email_mail_2.entry_email_mail("aprejzel@gmail.com" +"\h")

def test_value_mail_password(browser):
    value_mail_password = MailPageHelper(browser)
    value_mail_password.go_to_site()
    time.sleep(10)
    value_mail_password.click_word_mail()
    value_mail_password.entry_email_mail("aprejzel@gmail.com")
    value_mail_password.entry_mail_password("Lfhmz2012ljxm")
    value_mail_password.click_mail_button_remember_me()
    value_mail_password.click_mail_button_to_come_in()

def test_negative_entry_login_2(browser):
    negative_entry_login_2 = LoginPageHelper(browser)
    negative_entry_login_2.go_to_site()
    time.sleep(10)
    negative_entry_login_2.click_word_login()
    negative_entry_login_2.entry_in_field_login("123456")
    negative_entry_login_2.entry_login_password(" " + "\h")
    negative_entry_login_2.click_login_button_remember_me()
    negative_entry_login_2.click_login_button_to_come_in()

def test_recovery_password_link_come_back(browser):
    recovery_password_link_come_back = RecoveryPageHelper(browser)
    recovery_password_link_come_back.go_to_site()
    time.sleep(10)
    recovery_password_link_come_back.click_word_personal_account_recovery()
    recovery_password_link_come_back.entry_field_phone_or_mail_or_login_or_personalaccount("123456")
    recovery_password_link_come_back.entry_password_field("Lfhmz2012ljxm")
    recovery_password_link_come_back.click_button_to_come_in_recovery()
    recovery_password_link_come_back.click_link_forgot_password_recovery()
    recovery_password_link_come_back.click_link_come_back_recovery()
    authorization_page_word_text = recovery_password_link_come_back.recovery_word_authorization_text()
    assert authorization_page_word_text == "Авторизация"

def test_check_link_registration(browser):
    check_link_registration = SearchHelper(browser)
    check_link_registration.go_to_site()
    time.sleep(10)
    check_link_registration.click_word_registration()
    registration_page_word_text = check_link_registration.page_registration_word_text()
    assert registration_page_word_text == "Регистрация"

def test_input_valid_family_registration(browser):
        input_valid_family = SearchHelper(browser)
        input_valid_family.go_to_site()
        time.sleep(10)
        input_valid_family.click_word_registration()
        input_valid_family.word_name_registration("Алексей")
        input_valid_family.word_family_registration("Прейзель")

def test_input_valid_email_registration(browser):
            input_valid_email_registration = SearchHelper(browser)
            input_valid_email_registration.go_to_site()
            time.sleep(20)
            input_valid_email_registration.click_word_registration()
            time.sleep(10)
            input_valid_email_registration.word_name_registration("Алексей")
            time.sleep(10)
            input_valid_email_registration.word_family_registration("Прейзель")
            time.sleep(10)
            input_valid_email_registration.registration_email_or_phone("aprejzel@gmail.com" + "\h")

def test_continue_button_system_registration(browser):
    continue_button_system_registration = SearchHelper(browser)
    continue_button_system_registration.go_to_site()
    time.sleep(5)
    continue_button_system_registration.click_word_registration()
    continue_button_system_registration.word_name_registration("Алексей")
    continue_button_system_registration.word_family_registration("Прейзель")
    continue_button_system_registration.registration_email_or_phone("89521514008")
    continue_button_system_registration.registration_password("Lfhmz2012ljxm")
    continue_button_system_registration.registration_password_confirmation("Lfhmz2012ljxm")

def test_button_X_login_account(browser):
    button_X_login_account = SearchHelper(browser)
    button_X_login_account.go_to_site()
    time.sleep(10)
    button_X_login_account.click_word_registration()
    button_X_login_account.word_name_registration("Алексей")
    button_X_login_account.word_family_registration("Прейзель")
    button_X_login_account.registration_email_or_phone("aprejzel@gmail.com")
    button_X_login_account.registration_password("Lfhmz2012ljxm")
    button_X_login_account.registration_password_confirmation("Lfhmz2012ljxm")
    button_X_login_account.click_button_register()

def test_link_password_recovery_login_account(browser):
    link_password_recovery_login_account = SearchHelper(browser)
    link_password_recovery_login_account.go_to_site()
    time.sleep(10)
    link_password_recovery_login_account.click_word_registration()
    link_password_recovery_login_account.word_name_registration("Алексей")
    link_password_recovery_login_account.word_family_registration("Прейзель")
    link_password_recovery_login_account.registration_email_or_phone("aprejzel@gmail.com")
    link_password_recovery_login_account.registration_password("Lfhmz2012ljxm")
    link_password_recovery_login_account.registration_password_confirmation("Lfhmz2012ljxm")
    link_password_recovery_login_account.click_button_register()
    link_password_recovery_login_account.click_link_password_recovery()

def test_negative_code_check(browser):
    negative_code_check = TemporaryCodePageHelper(browser)
    negative_code_check.go_to_site()
    time.sleep(10)
    negative_code_check.click_word_phono_authoriz()
    negative_code_check.entry_phone_number_authoriz("89521514008")
    negative_code_check.entry_email_password_authoriz("Lfhmz2012ljxm")
    negative_code_check.click_button_remember_authoriz()
    negative_code_check.click_button_to_come_in_authoriz()
    negative_code_check.click_link_private_office()
    negative_code_check.click_link_private_office_username()
    negative_code_check.click_link_office_username_log_off()
    negative_code_check.entry_email_phone_authoriz_code("89521514008")
    negative_code_check.click_button_to_get_code()
    negative_code_check.entry_number_1_code("1")
    negative_code_check.entry_number_2_code("2")
    negative_code_check.entry_number_3_code("3")
    negative_code_check.entry_number_4_code("4")
    negative_code_check.entry_number_5_code("5")
    negative_code_check.entry_number_6_code("6" + "\h")