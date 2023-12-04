

from elementLocators.leaves.leave_elements import ApproveLeaveElements


class ApproveLeaveObjects:

    def __init__(self, driver):
        self.driver = driver

    def get_all_leave_requests_table(self):
        return self.driver.find_element(*ApproveLeaveElements.all_requests_table)

    def get_all_leave_requests(self):
        return self.driver.find_elements(*ApproveLeaveElements.requests_table_row)

    def get_all_row_cells(self, row):
        return row.find_elements(*ApproveLeaveElements.requests_table_cell)

    def get_requests_table_action_button(self, row):
        return row.find_elements(*ApproveLeaveElements.action_buttons)

    def get_employee_details_link(self, row):
        return self.get_all_row_cells(row)[1].find_element(*ApproveLeaveElements.employee_details_link)

    def get_requesting_leave_type(self, row):
        return self.get_all_row_cells(row)[2]

    def get_file_link(self):
        return self.driver.find_elements(*ApproveLeaveElements.file_link)[0]

    def get_file_download_button(self):
        return self.driver.find_elements(*ApproveLeaveElements.file_download_button)[0]

    def get_view_subordinate_leave_modal_close_button(self):
        return self.driver.find_element(*ApproveLeaveElements.view_subordinate_leave_modal).\
            find_element(*ApproveLeaveElements.modal_close_button)

    def get_view_document_close_button(self):
        return self.driver.find_element(*ApproveLeaveElements.view_document_modal).\
            find_element(*ApproveLeaveElements.modal_close_button)

    def get_approve_comment_box(self):
        return self.driver.find_elements(*ApproveLeaveElements.approve_comment_box)[0]

    def get_approve_submit_button(self):
        return self.driver.find_elements(*ApproveLeaveElements.approve_modal_submit_button)[1]

    def get_request_approve_or_reject_button(self, employee_name=None, action='reject'):
        table_rows = self.get_all_leave_requests()
        response_element = None
        employee_details_link = None
        leave_type = None
        if employee_name:
            for each in range(1, len(table_rows)):
                emp_data_link = self.get_employee_details_link(table_rows[each])
                leave_type_name = self.get_requesting_leave_type(table_rows[each])
                if emp_data_link.text == employee_name:
                    employee_details_link = emp_data_link
                    leave_type = leave_type_name
                    if action == 'approve':
                        response_element = self.get_requests_table_action_button(table_rows[each])[0]
                    else:
                        response_element = self.get_requests_table_action_button(table_rows[each])[1]
                    break
        if not response_element and action == 'approve':
            response_element = self.get_requests_table_action_button(table_rows[1])[0]
        elif not response_element and action == 'reject':
            response_element = self.get_requests_table_action_button(table_rows[1])[1]
        if employee_details_link is None:
            employee_details_link = self.get_employee_details_link(table_rows[1])

        if leave_type is None:
            leave_type = self.get_requesting_leave_type(table_rows[1])
        return employee_details_link, leave_type, response_element
