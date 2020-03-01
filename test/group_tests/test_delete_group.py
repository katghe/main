from model.group import Group


def test_delete_first_group(app):
    if app.group.count() ==0:
        app.group.create(Group(name="ggg", header="djjdj", footer="jdfhkjhkj"))
    app.group.delete_first_group()
