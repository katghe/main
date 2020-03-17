from model.contact import Contact
from sys import maxsize


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname", title="title", company="company",
                 address="address", home="home", mobile="mobile", work="work", email="email", email2="email2", email3="email3", bday="16", bmonth="October", byear="1900",
                 aday="20", amonth="July", ayear="1920", address2="address2", phone2="phone2", notes="notes")
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