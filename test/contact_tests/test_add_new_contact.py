from model.contact import Contact
from sys import maxsize
import pytest
import random
import string
from random import randint


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    symbols = string.digits + " "
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_bday():
    day = randint(0, 30)
    return day


def random_month():
    month_list = ["January ", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
    return random.choice(month_list)


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                    mobile="", work="", email="", bday="-", bmonth="-", byear="", aday="-", amonth="-",
                    ayear="", address2="", phone2="", notes="")] + [
               Contact(firstname=random_string("firstname", 6), lastname=random_string("lastname", 6),
                       company=random_string("company", 5),
                       address=random_string("address", 10), home=random_string("home", 10),
                       mobile=random_string("mobile", 10),
                       work=random_string("work", 10),
                       phone2=random_string("phone2", 10),
                       email=random_string("email1", 10),
                       email2=random_string("email2", 10),
                       email3=random_string("email3", 10))

               for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
