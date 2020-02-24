


def test_edit_first_contact(app):
    app.session.login(login_name="admin", password="secret")
    app.contact.edit_first_contact()
    app.session.logout()