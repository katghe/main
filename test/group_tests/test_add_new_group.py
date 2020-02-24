from model.group import Group



def test_add_new_group(app):
    app.session.login(login_name="admin", password="secret")
    app.group.create(Group(name="Group2", header="Gro", footer="up"))
    app.session.logout()


def test_add_new_empty_group(app):
    app.session.login(login_name="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

