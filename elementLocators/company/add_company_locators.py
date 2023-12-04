from selenium.webdriver.common.by import By


class AddCompanyElements:
    add_company_button = (By.CLASS_NAME, 'submit-btn')
    success_alert = (By.CSS_SELECTOR, 'div[class ="alert alert-dismissible fade show alert-success"]')
    close_success_alert = (By.CSS_SELECTOR, 'button[class="btn-close"]')
    my_reqeust_tab = (By.LINK_TEXT, 'My Requests')
    all_requests_tab = (By.PARTIAL_LINK_TEXT, 'All Requests')
    approve_request_button = (By.CSS_SELECTOR, 'button[class="btn btn-success text-light btn-sm m-r-5"]')
    approve_comment_box = (By.CSS_SELECTOR, 'textarea[placeholder="Enter comment here"]')
    approve_modal_submit_button = (By.CSS_SELECTOR, 'button[class="btn btn-primary submit-btn"]')
    approve_modal_cancel_button = (By.LINK_TEXT, 'Cancel')
    reject_request_button = (By.CSS_SELECTOR, 'button[class="btn btn-danger text-light btn-sm"]')
    reject_comment_box = (By.CSS_SELECTOR, 'textarea[placeholder="Enter comment here"]')
    reject_modal_submit_button = (By.CSS_SELECTOR, 'button[class="btn btn-primary submit-btn"]')
    reject_modal_cancel_button = (By.LINK_TEXT, 'Cancel')
    all_requests_table = (By.CLASS_NAME, 'ant-table')
    requests_table_row = (By.TAG_NAME, 'tr')
    requests_table_cell = (By.TAG_NAME, 'td')
    approve_or_reject_action_button = (By.XPATH, './/td[9]/div/button')
    ACTION_APPROVE = 'approve'
    ACTION_REJECT = 'reject'
    ACTION_CANCEL = 'cancel'
    ACTION_SUBMIT = 'submit'


class AddCompanyModalElements:
    add_company_modal = (By.CSS_SELECTOR, 'div[class="modal-content"]')
    legal_name = (By.NAME, 'legalName')
    short_name = (By.NAME, 'shortName')
    short_code_one = (By.NAME, 'shortCodeOne')
    short_code_two = (By.NAME, 'shortCodeTwo')
    cin = (By.NAME, 'cin')
    gstin = (By.NAME, 'gstin')
    address_line1 = (By.NAME, 'line1')
    address_line2 = (By.NAME, 'line2')
    locality = (By.NAME, 'locality')
    pincode = (By.NAME, 'pinCode')
    phone = (By.NAME, 'phone')
    parent_company = (By.NAME, 'parentCompany')
    parent_company_options = (By.TAG_NAME, 'option')
    company_logo_file = (By.ID, "uploadCaptureInputFile")
    submit_button = (By.CSS_SELECTOR, 'button[type="submit"]')
    select_state = (By.CSS_SELECTOR, 'span[title="-- Select State --"]')
    select_city = (By.CSS_SELECTOR, 'span[title="-- Select City --"]')
    options_list_holder = (By.CSS_SELECTOR, 'div[class="rc-virtual-list-holder"]')  # for state and city
    options = (By.CSS_SELECTOR, 'div[class="ant-select-item ant-select-item-option"]')
    errors = (By.TAG_NAME, 'small')
    failed_alert = (By.CLASS_NAME, 'alert-danger')
    window_modal = (By.ID, 'add_company')
    close_failed_alert = (By.CSS_SELECTOR, 'button[class="close"]')

