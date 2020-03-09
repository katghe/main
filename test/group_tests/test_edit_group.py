from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="sdfsdf"))
    old_groups = app.group.get_group_list()
    group = Group(name="Group21")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="sdfsdf"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="Group2"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)



def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="sdfsdf"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(footer="Group2"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
