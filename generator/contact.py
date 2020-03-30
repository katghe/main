
import random
import string
from model.contact import Contact
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n: f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                    mobile="", work="", email="", bday="-", bmonth="-", byear="", aday="-", amonth="-",
                    ayear="", address2="", phone2="", notes="")] + [
               Contact(firstname=random_string("firstname", 6), lastname=random_string("lastname", 6),
                       company=random_string("company", 5),
                       address=random_string("address", 10), home=random_string("home", 10),
                       mobile=random_string("mobile", 10),
                       work=random_string("work", 10),
                       phone2=random_string("phone2", 10),
                       email=random_string("email1", 10),
                       email2=random_string("email2", 10),
                       email3=random_string("email3", 10))

               for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))