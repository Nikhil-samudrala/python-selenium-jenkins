

from elementLocators.leaves.leave_elements import SickLeaveElements


class SickLeavePage:

    def __init__(self, driver):
        self.driver = driver

    def get_apply_leave_button(self):
        return self.driver.find_element(*SickLeaveElements.apply_leave_button)

    def get_apply_leave_modal(self):
        return self.driver.find_element(*SickLeaveElements.apply_leave_modal)

    def get_sick_leave_radio_button(self):
        return self.get_apply_leave_modal().find_element(*SickLeaveElements.sick_leave_radio_button)

    def get_from_date_input(self):
        return self.get_apply_leave_modal().find_element(*SickLeaveElements.from_date)

    def get_to_date_input(self):
        return self.get_apply_leave_modal().find_element(*SickLeaveElements.to_date)

    def get_date_selector_calendar_body(self):
        return self.driver.find_elements(*SickLeaveElements.dates_table_body)

    def get_date_selector_calendar_header(self):
        return self.driver.find_elements(*SickLeaveElements.dates_table_header)

    def get_from_date_previous_month_button(self):
        return self.get_date_selector_calendar_header()[0].find_elements(*SickLeaveElements.change_month_button)[1]

    def get_from_date_next_month_button(self):
        return self.get_date_selector_calendar_header()[0].find_elements(*SickLeaveElements.change_month_button)[4]

    def get_to_date_previous_month_button(self):
        return self.get_date_selector_calendar_header()[1].find_elements(*SickLeaveElements.change_month_button)[1]

    def get_to_date_next_month_button(self):
        return self.get_date_selector_calendar_header()[1].find_elements(*SickLeaveElements.change_month_button)[4]

    def get_from_date_elements(self):
        return self.get_date_selector_calendar_body()[0].find_elements(*SickLeaveElements.dates)

    def get_to_date_elements(self):
        return self.get_date_selector_calendar_body()[1].find_elements(*SickLeaveElements.dates)

    def get_from_date_leave_mode(self):
        return self.get_apply_leave_modal().find_elements(*SickLeaveElements.leave_mode)[0]

    def get_to_date_leave_mode(self):
        return self.get_apply_leave_modal().find_elements(*SickLeaveElements.leave_mode)[1]

    def get_leave_mode_holders(self):
        return self.driver.find_elements(*SickLeaveElements.leave_mode_holder)

    def get_from_date_leave_modes(self):
        return self.get_leave_mode_holders()[0].find_elements(*SickLeaveElements.leave_mode_options_parent)

    def get_leave_mode_element(self, parent):
        return parent.find_elements(*SickLeaveElements.child_div)[0]

    def get_to_date_leave_modes(self):
        return self.get_leave_mode_holders()[1].find_elements(*SickLeaveElements.leave_mode_options_parent)

    def get_purpose_input(self):
        return self.get_apply_leave_modal().find_element(*SickLeaveElements.purpose)

    def get_document_upload_input(self):
        return self.get_apply_leave_modal().find_element(*SickLeaveElements.sick_leave_document)

    def get_modal_window(self):
        return self.driver.find_element(*SickLeaveElements.modal_window)

    def get_modal_close_button(self):
        return self.get_modal_window().find_element(*SickLeaveElements.modal_close_button)

    def get_submit_button(self):
        return self.get_apply_leave_modal().find_element(*SickLeaveElements.submit)

    def get_failed_alert(self):
        return self.driver.find_element(*SickLeaveElements.failed_alert)

    def get_success_alert(self):
        return self.driver.find_element(*SickLeaveElements.success_alert)

    def get_close_success_alert(self):
        return self.get_success_alert().find_element(*SickLeaveElements.close_success_alert)

    def get_from_date_mode_input(self):
        return self.driver.find_element(*SickLeaveElements.from_date_leave_mode_input)

    def get_to_date_mode_input(self):
        return self.driver.find_element(*SickLeaveElements.to_date_leave_mode_input)
