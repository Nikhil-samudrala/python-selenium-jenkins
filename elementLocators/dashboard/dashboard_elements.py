from selenium.webdriver.common.by import By

class DashboardElements:

    profile_details = (By.CSS_SELECTOR, 'li[class="nav-item dropdown has-arrow main-drop"]')
    logout = (By.LINK_TEXT, 'Logout')
    configuration = (By.LINK_TEXT, 'Configuration')
    companies = (By.LINK_TEXT, 'Companies')
    policy_pop_over = (By.ID, "carousel_slider")
    popover_close_button = (By.CSS_SELECTOR, "div[id='view_utility_default'] button[class='close']")
    leaves_menu_tab = (By.LINK_TEXT, 'Leaves')
    my_laves_tab = (By.LINK_TEXT, 'My Leaves')
    hr_group_tab = (By.LINK_TEXT, 'HR Group')
    regional_leave_requests_tab = (By.LINK_TEXT, 'Leave Requests')
    regional_comp_off_requests = (By.LINK_TEXT, 'Regional CompOff')
    policies_tab = (By.LINK_TEXT, "Policies")
    home = (By.LINK_TEXT, "Home")
    dashboard = (By.LINK_TEXT, "Dashboard")
    reporting_manager_id = (By.CSS_SELECTOR, "div[class='staff-id']")

