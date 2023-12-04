from selenium.webdriver.common.by import By


class PoliciesElements:
    add_policy_button = (By.CSS_SELECTOR, "div[class='page-header'] button[class='btn btn-primary submit-btn']")
    policy_radio_buttons = (By.CSS_SELECTOR, "label[class*='ant-radio-button-wrapper']")
    add_action_button = (By.CSS_SELECTOR, "button[class='ant-btn ant-btn-dashed']")
    action_inputs = (By.CSS_SELECTOR, "input[name*='consentActions']")
    company_element = (By.CSS_SELECTOR, "div[name='companyId'] div")
    virtual_list = (By.CSS_SELECTOR, "div[class='rc-virtual-list-holder']")
    options = (By.CSS_SELECTOR, 'div[class="ant-select-item ant-select-item-option"]')
    department = (By.CSS_SELECTOR, "div[name='departmentId'] div")
    effective_from = (By.CSS_SELECTOR, "div[class='ant-picker-input']")
    today_link = (By.LINK_TEXT, "Today")
    policy_owner_input = (By.CSS_SELECTOR, "div[class='ant-select-selector'] input")
    policy_title = (By.CSS_SELECTOR, "input[name='policyTitle']")
    workplace = (By.CSS_SELECTOR, "div[class='jodit-workplace'] div")
    submit = (By.CSS_SELECTOR, "div[class='submit-section'] button")
    success_alert = (By.CSS_SELECTOR, "div[class*='alert']")
    all_requests = (By.LINK_TEXT, "All Requests")
    approve_button = (By.CSS_SELECTOR, "tbody button[class$='btn btn-success text-light btn-sm me-2']")


