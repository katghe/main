from model.group import Group



def test_add_new_group(app):
    app.group.create(Group(name="Group2", header="Gro", footer="up"))



def test_add_new_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


