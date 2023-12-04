
class ClickElement:
    @staticmethod
    def click_element_by_title(elements, target):
        for i in elements:
            if i.get_attribute('title') == target:
                if i.get_attribute('class').find('disabled') == -1:
                    i.click()
                else:
                    raise ValueError('element is being disabled date is out of applicable range')
                return i.get_attribute('title')
        return

    @staticmethod
    def click_element_by_text(element, target):
        for i in element:
            if i.text == target:
                i.click()
                return i.text
        return
