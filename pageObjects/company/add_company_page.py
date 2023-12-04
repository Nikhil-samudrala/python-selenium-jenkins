from selenium.webdriver.common.by import By

from elementLocators.company.add_company_locators import AddCompanyElements, AddCompanyModalElements


class AddCompany:

    def __init__(self, driver):
        self.driver = driver

    def get_add_company_button(self):
        return self.driver.find_element(*AddCompanyElements.add_company_button)

    def get_add_company_modal(self):
        return self.driver.find_element(*AddCompanyModalElements.add_company_modal)

    def get_legal_name(self):
        return self.driver.find_element(*AddCompanyModalElements.legal_name)

    def get_short_name(self):
        return self.driver.find_element(*AddCompanyModalElements.short_name)

    def get_short_code_one(self):
        return self.driver.find_element(*AddCompanyModalElements.short_code_one)

    def get_short_code_two(self):
        return self.driver.find_element(*AddCompanyModalElements.short_code_two)

    def get_cin(self):
        return self.driver.find_element(*AddCompanyModalElements.cin)

    def get_gstin(self):
        return self.driver.find_element(*AddCompanyModalElements.gstin)

    def get_address_line1(self):
        return self.driver.find_element(*AddCompanyModalElements.address_line1)

    def get_address_line2(self):
        return self.driver.find_element(*AddCompanyModalElements.address_line2)

    def get_locality(self):
        return self.driver.find_element(*AddCompanyModalElements.locality)

    def get_pincode(self):
        return self.driver.find_element(*AddCompanyModalElements.pincode)

    def get_phone(self):
        return self.driver.find_element(*AddCompanyModalElements.phone)

    def get_parent_company(self):
        return self.driver.find_element(*AddCompanyModalElements.parent_company)

    def get_parent_company_options(self):
        return self.driver.find_elements(*AddCompanyModalElements.parent_company_options)

    def get_company_logo_file(self):
        return self.driver.find_element(*AddCompanyModalElements.company_logo_file)

    def get_select_state(self):
        return self.driver.find_element(*AddCompanyModalElements.select_state)

    def get_select_city(self):
        return self.driver.find_element(*AddCompanyModalElements.select_city)

    def get_state_options_list_holder(self):
        return self.driver.find_elements(*AddCompanyModalElements.options_list_holder)[0]

    def get_city_options_list_holder(self):
        return self.driver.find_elements(*AddCompanyModalElements.options_list_holder)[-1]

    def get_options(self):
        return self.driver.find_elements(*AddCompanyModalElements.options)

    def get_errors(self):
        return self.get_add_company_modal().find_elements(*AddCompanyModalElements.errors)

    def get_submit_button(self):
        return self.driver.find_element(*AddCompanyModalElements.submit_button)

    def get_failed_alert(self):
        return self.driver.find_element(*AddCompanyModalElements.failed_alert)

    def get_window_modal(self):
        return self.driver.find_element(*AddCompanyModalElements.window_modal)

    def get_failed_alert_close(self):
        return self.get_window_modal().find_element(*AddCompanyModalElements.close_failed_alert)

    def get_success_alert(self):
        return self.driver.find_element(*AddCompanyElements.success_alert)

    def get_close_success_alert(self):
        return self.get_success_alert().find_element(*AddCompanyElements.close_success_alert)

    def get_my_requests(self):
        return self.get_success_alert().find_element(*AddCompanyElements.my_reqeust_tab)

    def get_all_requests_tab(self):
        return self.driver.find_element(*AddCompanyElements.all_requests_tab)

    def get_approve_request_button(self, request_company_name=None):
        return self.get_request_approve_or_reject_button(AddCompanyElements.ACTION_APPROVE, request_company_name)

    def get_approve_comment_box(self):
        return self.driver.find_elements(*AddCompanyElements.approve_comment_box)[0]

    def get_approve_modal_submit_button(self):
        return self.driver.find_elements(*AddCompanyElements.approve_modal_submit_button)[4]

    def get_approve_modal_cancel_button(self):
        return self.driver.find_elements(*AddCompanyElements.approve_modal_cancel_button)[0]

    def get_reject_request_button(self, request_company_name=None):
        return self.get_request_approve_or_reject_button(AddCompanyElements.ACTION_REJECT, request_company_name)

    def get_reject_comment_box(self):
        return self.driver.find_elements(*AddCompanyElements.reject_comment_box)[1]

    def get_reject_modal_submit_button(self):
        return self.driver.find_elements(*AddCompanyElements.reject_modal_submit_button)[4]

    def get_reject_modal_cancel_button(self):
        return self.driver.find_elements(*AddCompanyElements.reject_modal_cancel_button)[0]

    def get_all_requests_table(self):
        return self.driver.find_elements(*AddCompanyElements.all_requests_table)[2]

    def get_all_requests_table_rows(self):
        return self.get_all_requests_table().find_elements(*AddCompanyElements.requests_table_row)

    def get_all_requests_table_cell(self, row):
        return row.find_elements(*AddCompanyElements.requests_table_cell)

    def get_requests_table_action_button(self, row):
        return row.find_elements(*AddCompanyElements.approve_or_reject_action_button)

    def get_request_approve_or_reject_button(self, action, request_company_name=None):
        table_rows = self.get_all_requests_table_rows()
        response_element = None
        if request_company_name:
            for each in range(1, len(table_rows)):
                if self.get_all_requests_table_cell(table_rows[each])[0].text == request_company_name:
                    if action == AddCompanyElements.ACTION_APPROVE:
                        response_element = self.get_requests_table_action_button(table_rows[each])[0]
                    else:
                        response_element = self.get_requests_table_action_button(table_rows[each])[1]
                    break
        if not response_element and action == AddCompanyElements.ACTION_APPROVE:
            response_element = self.get_requests_table_action_button(table_rows[1])[0]
        elif not response_element and action == AddCompanyElements.ACTION_REJECT:
            response_element = self.get_requests_table_action_button(table_rows[1])[1]
        return response_element

