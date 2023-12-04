import random
import datetime
import xlrd


class SickLeaveData:
    ADD_LEAVE_DATA = [
        {'hrms_id': 'MED006271',
         'from_date': '2023-02-24',
         'to_date': '2023-02-26 ',
         'from_date_leave_mode': 'Full Day',
         'to_date_leave_mode': 'Full Day',
         'purpose': '"testing for automated sick leave for 3 days',
         'document': '/home/mphs/Downloads/lambo_1_100x63_10.jpg',
         },
    ]
    LEAVE_MODES = ['Full Day', 'First Half', 'Second Half']

    def __init__(self, count):
        self.ADD_LEAVE_DATA += self.get_random_leave_data(count)
        self.read_hrms_ids_from_excel(count)

    def get_random_leave_data(self, count):
        data_list = []
        hrms_ids = self.read_hrms_ids_from_excel(count)

        if len(hrms_ids) > count:
            loop_count = count
        else:
            loop_count = len(hrms_ids)
        for i in range(loop_count):
            from_date, to_date = self.get_random_date()
            data = {'hrms_id': hrms_ids[i],
                    'from_date': from_date,
                    'to_date': to_date,
                    'from_date_leave_mode': self.get_random_leave_mode(),
                    'to_date_leave_mode': self.get_random_leave_mode(),
                    'purpose': '"testing for automated sick leave for 3 days',
                    'document': '/home/mphs/Downloads/lambo_1_100x63_10.jpg',
                    }
            data_list.append(data)
        return data_list

    def get_random_date(self):
        # date = 'YYYY-MM-DD' | '%Y-%m-%d'
        from_date = ''
        from_date += str(random.randint(2022, 2023))
        from_date += '-'
        from_date += str(random.randint(5, 6)).zfill(2)
        from_date += '-'
        from_date += str(random.randint(1, 29)).zfill(2)
        to_date = datetime.datetime.strptime(from_date, '%Y-%m-%d').date() + datetime.timedelta(days=2)

        return from_date, to_date.strftime('%Y-%m-%d')

    def get_random_leave_mode(self):
        return random.choice(self.LEAVE_MODES)

    def read_hrms_ids_from_excel(self, count):
        user_id = []
        try:
            wb = xlrd.open_workbook('/home/mphs/practice_excel.xls')
            sheet = wb.sheet_by_index(0)
            rows = sheet.nrows
            if count > rows - 1:
                loop_count = rows
            else:
                loop_count = count + 1
            last_appeared_id = None
            for i in range(1, loop_count):
                cell_data = sheet.cell_value(i, 0)
                if cell_data:
                    last_appeared_id = cell_data
                user_id.append(cell_data or last_appeared_id)
        except Exception as e:
            print(e)
        return user_id
