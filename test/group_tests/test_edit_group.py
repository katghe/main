from model.group import Group
import random

def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="sdfsdf"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group_data = Group(name="Group21")
    app.group.edit_group_by_id(group.id, new_group_data)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_edit_group_header(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(header="sdfsdf"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group_data = Group(header="header21")
    app.group.edit_group_by_id(group.id, new_group_data)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)




def test_edit_group_footer(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(footer="sdfsdf"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group_data = Group(footer="footer21")
    app.group.edit_group_by_id(group.id, new_group_data)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
