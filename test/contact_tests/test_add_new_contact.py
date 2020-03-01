from model.contact import Contact


def test_add_new_contact(app):
    app.contact.create(
        Contact(firstname="Kate", middlename="Kat2", lastname="Yoffe", nickname="katghe", title="new user",
                company="addr", address="Saint - Petersburg", home="888888", mobile="89600765656",
                work="99999", email="email@am.com", bday="16", bmonth="October", byear="1992", aday="16",
                amonth="December", ayear="1990", address2="dfedgafgfda", phone2="dafdfafggag", notes="123455677"))



def test_add_new_contact_empty(app):
    app.contact.create(
        Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                mobile="", work="", email="", bday="-", bmonth="-", byear="", aday="-", amonth="-",
                ayear="", address2="", phone2="", notes=""))

