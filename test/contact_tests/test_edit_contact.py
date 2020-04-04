from model.contact import Contact
import random


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(lastname="fgsgfgsfgsd", firstname="ngd111jnhgd"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact_data = Contact(lastname="fgsgfg11sfgsd", firstname="ngd111jn111hgd")
    app.contact.edit_contact_by_id(contact.id, new_contact_data)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


# def test_edit_contact_phone(app):
#    if app.contact.count() == 0:
#   app.contact.create(Contact(home="1111111"))
# old_contacts = app.contact.get_contact_list()
# index = randrange(len(old_contacts))
# contact = Contact(home="888888", mobile="89600765656", work="99999")
# app.contact.edit_contact_by_index(index, contact)
# new_contacts = app.contact.get_contact_list()
# assert len(old_contacts) == len(new_contacts)
# new_contacts = app.contact.get_contact_list()
# old_contacts[index] = contact
# assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_edit_contact_bday(app):
#   if app.contact.count() == 0:
#   app.contact.create(Contact(byear="4444"))
# old_contacts = app.contact.get_contact_list()
# index = randrange(len(old_contacts))
# contact = Contact(bday="16", bmonth="October", byear="1992", aday="16", amonth="December", ayear="1996")
# app.contact.edit_contact_by_index(index, contact)
# new_contacts = app.contact.get_contact_list()
# assert len(old_contacts) == len(new_contacts)
# new_contacts = app.contact.get_contact_list()
# old_contacts[index] = contact
# assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
