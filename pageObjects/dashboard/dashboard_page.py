from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from elementLocators.dashboard.dashboard_elements import DashboardElements
from selenium.webdriver.support import expected_conditions as ec

class Dashboard:
    def __init__(self, driver):
        self.driver = driver

    def get_profile_details(self):
        return self.driver.find_element(*DashboardElements.profile_details)

    def logout_user(self):
        return self.driver.find_element(*DashboardElements.logout)

    def get_configurations(self):
        return self.driver.find_element(*DashboardElements.configuration)

    def get_companies(self):
        return self.driver.find_element(*DashboardElements.companies)

    def get_policy_pop_over(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(ec.presence_of_element_located((By.ID, "view_utility_default")))

    def get_pop_over_close_button(self, popover):
        return popover.find_element(*DashboardElements.popover_close_button)

    def get_leaves_menu_tab(self):
        return self.driver.find_element(*DashboardElements.leaves_menu_tab)

    def get_my_leaves_tab(self):
        return self.driver.find_element(*DashboardElements.my_laves_tab)

    def get_hr_groups_tab(self):
        return self.driver.find_element(*DashboardElements.hr_group_tab)

    def get_regional_leaves_tab(self):
        return self.driver.find_element(*DashboardElements.regional_leave_requests_tab)

    def get_policies_tab(self):
        return self.driver.find_element(*DashboardElements.policies_tab)

    def get_home_tab(self):
        return self.driver.find_element(*DashboardElements.home)

    def get_dashboard_tab(self):
        return self.driver.find_element(*DashboardElements.dashboard)

    def get_reporting_manager_id(self):
        return self.driver.find_elements(*DashboardElements.reporting_manager_id)[-1]
