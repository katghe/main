from model.group import Group


def test_edit_first_group(app):
    app.session.login(login_name="admin", password="secret")
    app.group.edit_first_group(Group(name="Group2", header="Gro", footer="up"))
    app.session.logout()