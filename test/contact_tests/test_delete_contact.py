from model.contact import Contact
import random



def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="fjfjfj", middlename="отчество", lastname="фамилия", nickname="вввв", title="пользователь"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

#def test_delete_first_contact(app):
 #   if app.contact.count() == 0:
  #      app.contact.create(Contact(firstname="fjfjfj", middlename="отчество", lastname="фамилия", nickname="вввв", title="пользователь"))
   # old_contacts = app.contact.get_contact_list()
    #app.contact.delete_first_contact()
    #assert len(old_contacts) - 1 == app.contact.count()
    #new_contacts = app.contact.get_contact_list()
    #old_contacts[0:1] = []
    #assert old_contacts == new_contacts






