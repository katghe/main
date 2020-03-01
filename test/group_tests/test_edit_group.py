from model.group import Group


def test_edit_group_name(app):
    app.group.edit_first_group(Group(name="Group2"))



def test_edit_group_header(app):
    app.group.edit_first_group(Group(header="ggg"))



def test_edit_group_footer(app):
    app.group.edit_first_group(Group(footer="fff"))

