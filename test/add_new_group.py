import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.session.login(login_name="admin", password="secret")
    app.group.create(Group(name="Group2", header="Gro", footer="up"))
    app.session.logout()


def test_add_new_empty_group(app):
    app.session.login(login_name="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

