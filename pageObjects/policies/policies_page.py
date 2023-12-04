from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from elementLocators.policies.policies_elements import PoliciesElements


class PoliciesPage:

    def __init__(self, driver):
        self.driver = driver

    def get_add_policy_button(self):
        return self.driver.find_element(*PoliciesElements.add_policy_button)

    def get_policies_radio_buttons(self):
        return self.driver.find_elements(*PoliciesElements.policy_radio_buttons)

    def get_add_action_button(self):
        return self.driver.find_element(*PoliciesElements.add_action_button)

    def get_action_inputs(self):
        return self.driver.find_elements(*PoliciesElements.action_inputs)

    def get_company_element(self):
        return self.driver.find_element(*PoliciesElements.company_element)

    def get_companies_list(self):
        return self.driver.find_elements(*PoliciesElements.virtual_list)[-1]

    def get_options(self, list):
        return list.find_elements(*PoliciesElements.options)

    def get_department_element(self):
        return self.driver.find_element(*PoliciesElements.department)

    def get_department_list(self):
        return self.driver.find_elements(*PoliciesElements.virtual_list)[-1]

    def get_effective_from(self):
        return self.driver.find_elements(*PoliciesElements.effective_from)[0]

    def get_today_link_element(self):
        return self.driver.find_element(*PoliciesElements.today_link)

    def get_policy_owner_input(self):
        return self.driver.find_elements(*PoliciesElements.policy_owner_input)[-1]

    def get_policy_title_input(self):
        return self.driver.find_element(*PoliciesElements.policy_title)

    def get_workplace_element(self):
        return self.driver.find_element(*PoliciesElements.workplace)

    def get_submit_button(self):
        return self.driver.find_element(*PoliciesElements.submit)

    def get_success_alert(self):
        return self.driver.find_element(*PoliciesElements.success_alert)

    def get_all_requests_link(self):
        return self.driver.find_element(*PoliciesElements.all_requests)

    def get_table_of_requests(self):
        # wait = WebDriverWait(self.driver, 10)
        # return wait.until(ec.presence_of_element_located((By.TAG_NAME)))
        return self.driver.find_elements(*PoliciesElements.table)[2]

    def get_approve_button(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, "tbody button[class$='btn btn-success text-light btn-sm me-2']")))

    def get_approve_buttonn(self):
        return self.driver.find_elements(*PoliciesElements.approve_button)[0]





