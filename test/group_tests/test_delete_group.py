



def test_delete_first_group(app):
    app.session.login(login_name="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()