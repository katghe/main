import pymysql
from model.contact import Contact
from model.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        glist = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                glist.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return glist

    def get_contact_list(self):
        clist = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, work, home, mobile, phone2, email, email2, email3"
                           " from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, work, home, mobile, phone2, email, email2, email3) = row
                clist.append(Contact(id=str(id), firstname=firstname, lastname=lastname, work=work, home=home,
                                     mobile=mobile, phone2=phone2, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return clist

    def get_contacts_in_group(self):
        contacts_in_group = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                contacts_in_group.append(Contact(id=str(id)))
        finally:
            cursor.close()
        return contacts_in_group

    def get_groups(self):
        groups = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                groups.append(Group(id=str(group_id)))
        finally:
            cursor.close()
        return groups






    def get_groups_in_ab(self):
        groups1 = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from address_in_groups")
            for row in cursor:
                (id) = row
                groups1.append(Group(id=str(id)))
        finally:
            cursor.close()
        return groups1

    def get_group_list_with_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT DISTINCT group_id FROM address_in_groups")
            for row in cursor:
                (id,) = row
                list.append(str(id))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()
