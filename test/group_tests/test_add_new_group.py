from model.group import Group
from sys import maxsize
import pytest

testdata = [
        Group(name="Group2", header="Gro", footer="up"),
        Group(name="", header="", footer="")
    ]


@pytest.mark.parametrize("group", testdata, ids = [repr(x) for x in testdata])
def test_add_new_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


