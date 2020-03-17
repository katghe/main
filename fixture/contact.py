from selenium.webdriver.support.ui import Select
import re
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def selected_element(self, field_name, selected):
        wd = self.app.wd
        if selected is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(selected)
            wd.find_element_by_name(field_name).click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("email", contact.email)
        self.selected_element("bday", contact.bday)
        self.selected_element("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.selected_element("aday", contact.aday)
        self.selected_element("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("Last name")) > 0):
            wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name('td')
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname, address=address,
                                                  all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_name("//input[@value='Delete']").click() 
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        middlename = wd.find_element_by_name("middlename").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        nickname = wd.find_element_by_name("nickname").get_attribute("value")
        title = wd.find_element_by_name("title").get_attribute("value")
        company = wd.find_element_by_name("company").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        text = wd.find_element_by_id("content").text
        all_phones_edit = re.search("Home:(.*)\nMobile:(.*)\nWork:(.*)", text).group(1, 2, 3)
        all_emails_edit = re.search("E-mail: (.*)\nE-mail2: (.*)\nE-mail3: (.*)", text).group(1, 2, 3)
        bday = wd.find_element_by_name("bday").get_attribute("value")
        bmonth = wd.find_element_by_name("bmonth").get_attribute("value")
        byear = wd.find_element_by_name("byear").get_attribute("value")
        aday = wd.find_element_by_name("aday").get_attribute("value")
        amonth = wd.find_element_by_name("amonth").get_attribute("value")
        ayear = wd.find_element_by_name("ayear").get_attribute("value")
        address2 = wd.find_element_by_name("address2").get_attribute("value")
        return Contact(
            firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title,
            company=company, address=address, all_phones_from_edit_page=all_phones_edit,
            all_emails_from_edit_page=all_emails_edit, email=email, email2=email2, email3=email3, bday=bday,
            bmonth=bmonth, byear=byear, aday=aday, amonth=amonth, ayear=ayear, address2=address2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        all_phones_view = re.search("(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)", text).group(6, 7, 8, 14)
        all_emails_view = re.search("(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)", text).group(9, 10, 11)
        firstname = re.search("(.*)", text).group(1)
        middlename = re.search("(.*) (.*)", text).group(2)
        lastname = re.search("(.*) (.*) (.*)", text).group(3)
        nickname = re.search("(.*)\n(.*)", text).group(2)
        title = re.search("(.*)\n(.*)\n(.*)", text).group(3)
        company = re.search("(.*)\n(.*)\n(.*)\n(.*)", text).group(4)
        address = re.search("(.*)\n(.*)\n(.*)\n(.*)\n(.*)", text).group(5)
        bday = re.search("(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*) (.*)", text).group(13)
        bmonth = re.search("(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*) (.*) (.*)", text).group(14)
        byear = re.search("(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*) (.*) (.*) (.*)", text).group(15)
        aday = re.search("(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*) (.*) (.*) (.*) (.*)\n(.*) (.*)", text).group(18)
        amonth = re.search("(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*) (.*) (.*) (.*) (.*)\n(.*) (.*) (.*)", text).group(19)
        ayear = re.search("(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*) (.*) (.*) (.*) (.*)\n(.*) (.*) (.*) (.*)", text).group(20)
        address2 = re.search("(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*) (.*) (.*) (.*) (.*)\n(.*) (.*) (.*) (.*) (.*)\n(.*)", text).group(22)
        return Contact(
            firstname=firstname, middlename=middlename,  lastname=lastname, nickname=nickname, title=title,
            company=company, address=address, all_phones_from_view_page=all_phones_view,
            all_emails_from_view_page=all_emails_view, bday=bday, bmonth=bmonth, byear=byear, aday=aday, amonth=amonth,
            ayear=ayear, address2=address2)















