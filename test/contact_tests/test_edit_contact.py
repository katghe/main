from model.contact import Contact
from random import randrange

def test_edit_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="kdfkfkf"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="kfjfjf", middlename="jdjddj", lastname="jdfhskjh")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_contact_phone(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(home="1111111"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(home="888888", mobile="89600765656", work="99999")
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



def test_edit_contact_bday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(byear="4444"))
    index = randrange(len(old_contacts))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(bday="16", bmonth="October", byear="1992", aday="16", amonth="December", ayear="1996")
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


