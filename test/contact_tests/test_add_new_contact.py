from model.contact import Contact
from sys import maxsize


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Kate", middlename="Kat2", lastname="Yoffe", nickname="katghe", title="new user",
                      company="addr", address="Saint - Petersburg", home="888888", mobile="89600765656",
                      work="99999", email="email@am.com", bday="16", bmonth="October", byear="1992", aday="16",
                      amonth="December", ayear="1990", address2="dfedgafgfda", phone2="dafdfafggag", notes="123455677")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_new_contact_empty(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                mobile="", work="", email="", bday="-", bmonth="-", byear="", aday="-", amonth="-",
                ayear="", address2="", phone2="", notes="")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)