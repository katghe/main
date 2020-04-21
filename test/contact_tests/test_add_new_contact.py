from model.contact import Contact
import pytest
import allure





def test_add_new_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    with allure.step('Шаг 1'):
        old_contacts = db.get_contact_list()
    with allure.step('Шаг 2'):
        app.contact.create(contact)
    with allure.step('Шаг 3'):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


