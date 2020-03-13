from model.contact import Contact
from sys import maxsize


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Kate", lastname="Yoffe")
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