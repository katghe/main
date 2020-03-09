from model.contact import Contact


def test_edit_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="kdfkfkf"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="kfjfjf", middlename="jdjddj", lastname="jdfhskjh")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_contact_phone(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(home="kdfkfkf"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(home="888888", mobile="89600765656", work="99999"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_bday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(byear="4444"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(bday="16", bmonth="October", byear="1992", aday="16", amonth="December", ayear="1996"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


