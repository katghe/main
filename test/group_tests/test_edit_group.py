from model.group import Group
from random import randrange


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="sdfsdf"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Group21")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="sdfsdf"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(header="Group2")
    app.group.edit_group_by_index(index, group)
    group.id = old_groups[index].id
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)



def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="sdfsdf"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(footer="dfsdfsdf")
    app.group.edit_group_by_index(index, group)
    group.id = old_groups[index].id
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
