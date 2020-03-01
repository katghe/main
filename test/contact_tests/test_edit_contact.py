from model.contact import Contact


def test_edit_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="kdfkfkf"))
    app.contact.edit_first_contact(Contact(firstname="kfjfjf", middlename="jdjddj", lastname="jdfhskjh"))



def test_edit_contact_phone(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(home="kdfkfkf"))
    app.contact.edit_first_contact(Contact(home="888888", mobile="89600765656", work="99999"))



def test_edit_contact_bday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(byear="4444"))
    app.contact.edit_first_contact(Contact(bday="16", bmonth="October", byear="1992", aday="16", amonth="December", ayear="1996"))

