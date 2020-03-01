from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="sdfsdf"))
    app.group.edit_first_group(Group(name="Group2"))



def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="sdfsdf"))
    app.group.edit_first_group(Group(header="Group2"))



def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="sdfsdf"))
    app.group.edit_first_group(Group(footer="Group2"))

