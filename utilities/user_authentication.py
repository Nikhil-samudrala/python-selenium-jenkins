import time

from utilities.BaseClass import BaseClass

class UserAuthentication:
    @staticmethod
    def user_login(login_obj, hrms_id):
        login_obj.get_login_page()
        time.sleep(1)
        username_input = login_obj.get_username()
        username_input.send_keys(hrms_id)
        generate_otp_button = login_obj.get_generate_otp_button()
        if generate_otp_button:
            generate_otp_button.click()
            otp_boxes = login_obj.get_otp_boxes()
            if len(otp_boxes) > 0:
                for each in otp_boxes:
                    each.send_keys(1)
                submit_button = login_obj.get_submit_button()
                submit_button.click()
            else:
                raise Exception('OTP input boxes not found')
        else:
            raise Exception('Generate otp button not found')
        time.sleep(1)

    @staticmethod
    def user_logout(dashboard):
        try:
            dashboard.driver.get(BaseClass.BASE_URL+'app/dashboard/employee-dashboard')
            profile_details = dashboard.get_profile_details()
            profile_details.click()
            logout_link = dashboard.logout_user()
            time.sleep(2)
            logout_link.click()
        except Exception as exc:
            print(exc)

    @staticmethod
    def handle_policy_popover(dashboard):
        try:
            popover = dashboard.get_policy_pop_over()
            time.sleep(1.5)
            popover_close_button = dashboard.get_pop_over_close_button(popover)
            popover_close_button.click()
            print('popover closed...')
        except Exception as e:
            print("policy popover is not displayed")
