


def test_delete_first_contact(app):
    app.session.login(login_name="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()
