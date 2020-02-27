from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(login_name="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="имя", middlename="отчество", lastname="фамилия", nickname="вввв", title="пользователь",
                company="addr", address="Saint - Petersburg", home_phone="888888", mobile_phone="89600765656",
                work_phone="99999", main_email="email@am.com", bday="16", bmonth="October", byear="1992", aday="16",
                amonth="December", ayear="1996", address2="олвыарлорлор", phone2="апфвпавп", notes="123455677"))
    app.session.logout()