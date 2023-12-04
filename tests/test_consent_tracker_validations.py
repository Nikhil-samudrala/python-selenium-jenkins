import random
import string
import time
from selenium.webdriver.common.keys import Keys
from pageObjects.dashboard.dashboard_page import Dashboard
from pageObjects.login.login_page import Login
from utilities.BaseClass import BaseClass
from utilities.user_authentication import UserAuthentication
from pageObjects.policies.policies_page import PoliciesPage


class TestConsentTrackerValidations(BaseClass):
    @staticmethod
    def click_element_by_text(elements, target):
        for i in elements:
            if i.text == target:
                print(i.text)
                i.click()
                return i.text
        return

    @staticmethod
    def select_element_by_scroll(driver, policy_page, options_holder, target_option):
        holder_height = options_holder.size['height']
        print("holder height", holder_height)
        current_scroll = 0
        scroll_height = driver.execute_script('return arguments[0].scrollHeight', options_holder)
        print("scroll_height", scroll_height)
        time.sleep(1)
        select_options = policy_page.get_options(options_holder)
        selected_option = TestConsentTrackerValidations.click_element_by_text(select_options, target_option)
        if not selected_option:
            while current_scroll < scroll_height:
                driver.execute_script(
                    'if(arguments[1]<arguments[0].scrollHeight){arguments[0].scrollTo(0,arguments[1]+arguments[2]);}',
                    options_holder, current_scroll, holder_height)
                select_options = policy_page.get_options(options_holder)

                selected_option = TestConsentTrackerValidations.click_element_by_text(select_options, target_option)
                if selected_option:
                    break
                current_scroll += holder_height
                time.sleep(0.2)
            if not selected_option:
                driver.execute_script(
                    '{arguments[0].scrollTo(0,arguments[0].scrollHeight);}',
                    options_holder)
                select_options = policy_page.get_options(options_holder)
                selected_option = TestConsentTrackerValidations.click_element_by_text(select_options, target_option)
        return selected_option

    @staticmethod
    def move_to_policies_page(dashboard):
        time.sleep(4)
        UserAuthentication.handle_policy_popover(dashboard)
        dashboard.get_hr_groups_tab().click()
        dashboard.get_policies_tab().click()

    @staticmethod
    def add_actions(policy_page, driver):
        random_num = random.randint(1,8)
        for i in range(0, random_num):
            driver.execute_script("document.querySelector('.ant-btn-dashed').scrollIntoView(false)")
            time.sleep(1)
            policy_page.get_add_action_button().click()

    @staticmethod
    def enter_action_inputs(policy_page, driver):
        inputs = policy_page.get_action_inputs()
        for i, action_input in enumerate(inputs):
            driver.execute_script(f"document.getElementsByName('consentActions[{i}]')[0].scrollIntoView(false)")
            length_of_string = 10
            res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length_of_string))
            action_input.send_keys(res)

    @staticmethod
    def add_policy_as_policy(self, driver, dashboard):
        policy_page = PoliciesPage(driver)
        policy_page.get_add_policy_button().click()
        time.sleep(2)
        policy_page.get_policies_radio_buttons()[2].click()
        policy_page.get_add_action_button().click()
        TestConsentTrackerValidations.add_actions(policy_page, driver)
        TestConsentTrackerValidations.enter_action_inputs(policy_page, driver)
        driver.execute_script("document.getElementsByName('companyId')[0].scrollIntoView(false)")
        time.sleep(1)
        policy_page.get_company_element().click()
        company_virtual_list = policy_page.get_companies_list()
        driver.execute_script("window.scrollTo(0, document.querySelector('#app').scrollHeight - 1000)")
        TestConsentTrackerValidations.select_element_by_scroll(driver, policy_page, company_virtual_list,
                                                               "Optival")
        policy_page.get_company_element().click()
        time.sleep(1)
        policy_page.get_department_element().click()
        department_list = policy_page.get_department_list()
        TestConsentTrackerValidations.select_element_by_scroll(driver, policy_page, department_list, "Software")
        policy_page.get_department_element().click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.querySelector('#app').scrollHeight)")
        time.sleep(2)
        policy_page.get_effective_from().click()
        policy_page.get_today_link_element().click()
        policy_owner = policy_page.get_policy_owner_input()
        policy_owner.send_keys("med000849")
        time.sleep(2)
        policy_owner.send_keys(Keys.ENTER)
        length_of_string = 50
        res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length_of_string))
        policy_page.get_policy_title_input().send_keys(res)
        policy_page.get_workplace_element().send_keys(res)
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.querySelector('#app').scrollHeight)")
        time.sleep(1)
        policy_page.get_submit_button().click()
        time.sleep(2)
        alert_message = policy_page.get_success_alert().text
        assert "Policy Created Successfully" in alert_message
        dashboard.get_home_tab().click()
        dashboard.get_dashboard_tab().click()
        total_text = dashboard.get_reporting_manager_id().text
        print(total_text)
        repo_manager_id = total_text.split("(")[1].split(")")[0]
        print(repo_manager_id)
        UserAuthentication.user_logout(dashboard)
        time.sleep(2)
        return repo_manager_id

    @staticmethod
    def approve_policy_as_policy(self, login_obj, dashboard, repo_manager_id):
        policy_page = PoliciesPage(self.driver)
        UserAuthentication.user_login(login_obj, repo_manager_id)
        TestConsentTrackerValidations.move_to_policies_page(dashboard)
        policy_page.get_all_requests_link().click()
        policy_page.get_approve_buttonn().click()

    def test_execute_script(self):
        self.driver.implicitly_wait(10)
        dashboard = Dashboard(self.driver)
        login_obj = Login(self.driver)
        UserAuthentication.user_login(login_obj, "med000849")
        TestConsentTrackerValidations.move_to_policies_page(dashboard)
        
        # To raise new policy of policy type
        # repo_manager_id = TestConsentTrackerValidations.add_policy_as_policy(self.driver, dashboard)
        # To approve new policy of policy type
        # TestConsentTrackerValidations.approve_policy_as_policy(login_obj, dashboard, repo_manager_id)














