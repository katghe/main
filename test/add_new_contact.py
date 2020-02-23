import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_new_contact(app):
    app.login(login_name="admin", password="secret")
    app.create_contact(Contact(firstname="Kate", middlename="Kat2", lastname="Yoffe", nickname="katghe", title="new user", company="addr", address="Saint - Petersburg", home_phone="888888", mobile_phone="89600765656", work_phone="99999", main_email="email@am.com", bday="16", bmonth="October", byear="1992", aday="16", amonth="December", ayear="1990", address2="dfedgafgfda", phone2="dafdfafggag", notes="123455677"))
    app.logout()

def test_add_new_contact_empty(app):
    app.login(login_name="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home_phone="", mobile_phone="", work_phone="", main_email="", bday="-", bmonth="-", byear="", aday="-", amonth="-", ayear="", address2="", phone2="", notes=""))
    app.logout()
